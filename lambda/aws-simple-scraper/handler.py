import json
import requests
import bs4
from bs4 import BeautifulSoup



def hello(event, context):
    
    html = requests.get("https://au.indeed.com/jobs?q=software+engineer&l=Canberra+ACT&sort=date")
    soup = BeautifulSoup(html.text, 'html.parser')
    
    jobs = []

    for div in soup.find_all(name="div", attrs={"class": "result"}):
        
        # Title
        title = div.find(name="a", attrs={"data-tn-element":"jobTitle"})["title"]
        
        # Company
        company = div.find(name="span", attrs={"class":"company"}).text.strip()
        # Location
        location = div.find(name="span", attrs={"class":"location"}).text.strip()
        
        # Description
        description = div.find(name="span", attrs={"class":"summary"}).text.strip()
        
        # Date
        date = ""
        try: 
            date = div.find(name="span", attrs={"class":"date"}).text.strip()
        except AttributeError as e:
            date = "N/A"
        
        # Salary
        salary = ""
        try:
            salary = div.find(name="span", attrs={"class":"no-wrap"}).text.strip()
        except AttributeError as e:
            salary = "N/A"
        
        jobs.append({'title': title,
               'company': company,
               'location': location,
               'description': description,
               'date': date,
               'salary': salary,})

    print(jobs)
    
    body = {
        "message": "Go Serverless v1.0!!! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
