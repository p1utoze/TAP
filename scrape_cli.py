from scrape import scrape
import argparse, pandas as pd
parser = argparse.ArgumentParser(prog='scraper',
                                 description='A script to scrape Resumes of various domains'
                                             'listed in www.jobspider.com',
                                 allow_abbrev=True,)

# no_args_group = parser.add_mutually_exclusive_group(required=False)
# no_args_group.add_argument('-d', '--description', action='store_true', help='Print program description')

myargs_group = parser.add_mutually_exclusive_group(required=False)
myargs_group.add_argument('-d', '--domain', type=str, action='store')
myargs_group.add_argument('-c', '--category', type=int, action='store')
args = parser.parse_args()


if args.domain:
    print(f'Extracting resumes in domain: {args.domain}\n......')
    d = scrape(args.domain)
    df = pd.DataFrame.from_dict(d, orient='index').T
    df.to_csv(f"resume_data_{args.domain}")

elif args.category:
    print(f'Extracting resumes in category: {args.category}\n......')
    d = scrape(category=True, cat_no=args.category)
    df = pd.DataFrame.from_dict(d, orient='index').T
    df.to_csv(f"resume_data_category_{args.category}")

else:
    print(parser.description)
    print('Running default search: engineer.....')
    d = scrape()
    exit()