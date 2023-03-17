import requests
from bs4 import BeautifulSoup
import urllib.parse as up
import re
import time


def fetch_pages(page_data):
    for i in page_data.find_all_next('a'):
        uri = i['href']
        if re.search(r'/page_[0-9]+', uri):
            page = up.urljoin('https://www.jobspider.com', uri)
            yield page


def resume_links(page_data, d):
    # print(*[i['href']for i in page_data.find_all('a')], sep='\n')
    for i in page_data.find_all('a'):
        uri = i['href']
        if re.search(r'^/job/view-resume+', uri):
            resume = up.urljoin('https://www.jobspider.com', uri)
            soup = BeautifulSoup(requests.get(resume).text, 'lxml')
            print('---->     Extracting page: ', resume, '\n    ......')
            d.setdefault('Role', []).append(soup.find('h1').text)
            for key, value in get_resume(soup):
                # print(f'{key=}\n{value=}')
                d.setdefault(key, []).append(value)
    return d

def get_resume(soup):
    for i in soup.find_all('font', attrs={'size': ['1', '2']}):
        if re.search(r'Candidate|JobSpider', i.text) or not i.text or i['color'] == '#6F6F6F':
            continue
        if i['color'] == '#000f99':
            value = i.find_next('font').get_text(separator='\n', strip=True)
            yield i.b.string[:-1], value
        elif i['color'] == '#000000':
            # field = re.search(r'[a-zA-Z]+:', i.text)
            # if field and not field.group()[0].islower():
            #     yield field.group()[:-1], re.sub(r'[a-zA-Z]+:', '', i.text)
            content = i.text.strip().split(':')
            if not content[1]:
                yield content[0], None
            else:
                yield content[0], content[1].strip()


# string = '/job/resume-search-results.asp/words_engineer/searchtype_1/page_4'
# s = '/job/resume-search-results.asp/words_engineer/searchtype_1/sort_5'
# s = '/job/view-resume-83943.html'
# print(re.match(r'^/job/view-resume+', s).string)
def scrape(search='engineer', category=False, cat_no=None):
    start = time.time()
    if category:
        url = f'https://www.jobspider.com/job/resume-search-results.asp/category_{cat_no}'
    else:
        url = f'https://www.jobspider.com/job/resume-search-results.asp/words_{search}/searchtype_1'
    print('SITE: ', url)
    site = requests.get(url)
    check_pages = {}
    # resume_doc = up.urljoin('https://www.jobspider.com', '/job/view-resume-78327.html')
    soup = BeautifulSoup(site.text, "lxml")
    links = soup.find_all('font')[13]
    d = resume_links(links, {})
    for page in fetch_pages(links):
        if not check_pages.get(page, None):
            print('\nPage: ', page)
            soup = BeautifulSoup(requests.get(page).text, 'lxml')
            features = soup.find_all('font')[13]
            d = resume_links(features, d)
            print('Resumes fetched: ', d['SpiderID'].__len__())
            check_pages[page] = 1
    del check_pages
    end = time.time() - start
    # print(d['Role'])
    print(f"Total features: {d.keys()}\nTotal Resumes Extracted: {d['SpiderID'].__len__()}\nTotal time: {end/60.0} min")
    return d

# d = scrape(')