import json
import requests
import boto3
from botocore.exceptions import ClientError
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
    
    jobs = scrape_site()
    print(jobs)
    
    SUBJECT = "Daily Web Job Scraping"
    
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ( "Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
                )

    display = """ <html> <body>
        <h1> Daily Web Job Scraping </h1>
        <p> Hi There, here's your daily job list update! </p> """
    
    for j in jobs:
        display += """
        <p> <b>Job:</b> %s <br>
        <b>Company:</b> %s <br>
        <b>Description:</b> %s <br>
        <b>Location:</b> %s <br>
        <b>Date:</b> %s <br>
        <b>Salary:</b> %s </p>
        <br> """ %(j.get("title"), j.get("company"), j.get("description"), 
        j.get("location"), j.get("date"), j.get("salary"))

    display += """
        </body>
        </html>
        """

    ses_email(SUBJECT, BODY_TEXT, display, "markmonteno@gmail.com", "markmonteno@gmail.com")
    
    body = {
        "message": "Go Serverless v1.0!!! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
