import json
import datetime
import scraper
import emailer

def entry(event, context):
    
    result = scrapeForJobsAndEmail()
    
    body = {
        "message": "Go Serverless v1.0!!! Your function executed successfully!",
        "input": json.dumps(result)
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def schedule(event, context):
    currTime = datetime.datetime.now().time()
    
    scrapeForJobsAndEmail()
    
    print(currTime)

def endpoint(event, context):
    
    result = scrapeForJobsAndEmail()
    
    body = {
        "message": result        
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    
    return response

def scrapeForJobsAndEmail():
     # Scrape jobs
    jobs = scraper.scrape_site("https://au.indeed.com/jobs?q=software+engineer&l=Canberra+ACT&sort=date")
    
    # Subject
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
        <b>Link:</b> %s </p>
        <br> """ %(j.get("title"), j.get("company"), j.get("description"), 
        j.get("location"), j.get("date"), j.get("salary"), j.get("link"))

    display += """
        </body>
        </html>
        """

    emailer.ses_email(SUBJECT, BODY_TEXT, display, "markmonteno@gmail.com", "markmonteno@gmail.com")
    
    return jobs
