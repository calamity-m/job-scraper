import json
import requests
import bs4
from bs4 import BeautifulSoup

def resolve_span(div, attr):
    try:
        rtn = div.find(name="span", attrs=attr)
        return rtn
    except:
        return ""

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
               'salary': salary,})

    return jobs

def ses_email(subject, body_text, body_html, sender, receiver):
    CHARSET = "UTF-8"
    # Create a new SES resource and specify a region.
    client = boto3.client('ses',region_name="us-west-2")
    
    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    receiver,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': body_html,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': body_text,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': subject,
                },
            },
            Source=sender,
        )
        
    # Display an error if something goes wrong.	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['ResponseMetadata']['RequestId'])


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
