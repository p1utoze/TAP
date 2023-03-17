# TAP
*Test, Apply, Progress!*

TAP is a Two-Way AI Recruitment Platform AI-powered platform designed to solve the challenges faced by both job seekers and recruiters. In the current job market, candidates struggle to find the right job openings and recruiters face challenges in finding the right talent for their job openings. TAP aims to bridge this gap by providing a two-way recommendation system that connects the job seekers and recruiters in a seamless and efficient manner.

# Business Scope

- Recruitment agencies: TAP can help recruitment agencies streamline their operations and improve the quality of their candidate searches, reducing the time and cost associated with finding the right candidates.

-  HR departments automate the initial stages of the recruitment process, reducing the workload on HR staff and ensuring that the most qualified candidates are shortlisted for further consideration.

- Filtered Resume parsing for effective job recommendation to the candidates.

# System Architecture


<a href="https://imgbb.com/"><img align='right' width='450' height='550' src="https://i.ibb.co/cDTXfxw/SAPCase-Study-drawio.png" alt="SAPCase-Study-drawio" border="0"></a>

### Student side: 
- Candidate asked for inputs like: salary, work-location, resume/CV, etc and quick assessment for the domain he/she selects.
- The personalized AI shows the percentage match in various domains in the job market and its statistical visualization.
- This AI powered by: Resume OCR using NLP, web scrape of candidate’s facts and a Recommender System.
- The Bot subscribes for mailing list in suitable companies for job recruitment using Robotic Process Automation
- Gives Regular updates on job but on an exchange for another skill test.

### Recruiter side:
- Recruiter is asked to post interview-like questions and job requirements.
- An analysing tool on past recruiting performance and success factors of past hired candidates
- An AI bot assisted Talent pipeline customised for the recruiter with tools like Referral Analysis, marketing automation on social media platforms, inter-bot word of mouth communication.
- The AI bot uses recommendation system and advanced filtering algorithms to match with the Student AI bot profile.
- Requirement-to-Skill match visualization for enhanced analysis. 
<br>

### Process

<img align='left' width='700' height='400' src='https://user-images.githubusercontent.com/80112729/128816859-87e061da-b9e1-4880-ba1a-6e38122ff412.png'>

 * **For job seeker**: Firstly, Input the CV and then it will be processed by OCR. After that, the CV and job posts will undergo NLP process. And then both CV and job post will be compared by varies methods to find the similarity. Lastly, the system will list out recomendation of jobs.

  * **For recruiter**: Firstly, Input the job post and it will undergo NLP process along with CV in database. And then both CV and job post will be compared by varies methods to find the similarity. Lastly, the system will list out recomendation of candidates.
 
<br>
<hr>

# Technologies Used:

- Web scrapping
- Natural Language Processing
- Optical Character Recognition
- Recommendation System


# Navigation:

- The web scrapping script for collecting datasets is written in a python file: `scrapper.py`. A CLI interface is also available> Refer to the documentation for more details: [Job resume scrapper](https://github.com/p1utoze/Resume_scrapper).
- The Resume and job requirement data processing files is in [preprocess](https://github.com/p1utoze/TAP/tree/main/preprocess) folder.
- All the final datasets are in [data](https://github.com/p1utoze/TAP/tree/main/data)
- The demo recommendation and the main model are jupyter notebooks in [models](https://github.com/p1utoze/TAP/tree/main/models)

# WORKING
Libraries & Frameworks:
- OneDAL (daal4py python API)
- BeautifulSoup
- sklearnex
- pandas 
- requests
- kneed
- spaCy

# Progress:
* Currently the datasets have been scrapped




