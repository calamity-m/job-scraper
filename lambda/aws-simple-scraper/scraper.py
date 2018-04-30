import requests
from bs4 import BeautifulSoup

def resolve_span(div, attr):
    try:
        rtn = div.find(name="span", attrs=attr)
        return rtn.text.strip()
    except:
        return None

def scrape_site(url):
    # HTML page from requests
    html = requests.get(url)
    
    # Inital soup object from bs4
    soup = BeautifulSoup(html.text, 'html.parser')
    
    # Initalize our jobs array
    jobs = []

    # Scrape through all divs that we want and get job information
    for div in soup.find_all(name="div", attrs={"class": "result"}):
        # Title
        title = div.find(name="a", attrs={"data-tn-element":"jobTitle"})["title"]
        # Link
        link = "https://au.indeed.com"
        link += div.find(name="a")['href']
        # Company
        company = div.find(name="span", attrs={"class":"company"}).text.strip()
        # Location
        location = div.find(name="span", attrs={"class":"location"}).text.strip()
        # Description
        description = div.find(name="span", attrs={"class":"summary"}).text.strip()
        # Date
        date = resolve_span(div, {"class":"date"})
        if date is None:
            date = "Not Specified"
        # Salary
        salary = resolve_span(div, {"class":"no-wrap"})
        if salary is None:
            salary = "Not Specified"
        
        # Add a new compiled job to our dict
        jobs.append({'title': title,
               'company': company,
               'location': location,
               'description': description,
               'date': date,
               'salary': salary,
               'link': link,})

    # Return our jobs dict
    return jobs