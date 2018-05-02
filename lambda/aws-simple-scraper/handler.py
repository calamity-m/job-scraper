# ************************************
# Authors: Mark Monteno (u3154816)
# Assignment 1 Term project: Serverless Computing
# Built using Python 3.6
# ************************************

# Import the python libraries we will need
import json
import datetime
import scraper
import emailer

# Lambda handler for API Gateway Events
def api_entry(event, context):
    
    # Get the scraped data from au.indeed.com and put it into result
    result = scraper.scrape_site("https://au.indeed.com/jobs?q=software+engineer&l=Canberra+ACT&sort=date")
    
    # Form the body of our HTTP RESTful reply
    body = {
        "message": result        
    }
    
    # Form the final response of our HTTP RESTful reply
    response = {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin" : "*", "Access-Control-Allow-Credentials" : True},
        "body": json.dumps(body)
    }
    
    # Return our response for the API Gateway to send back
    return response

# Lambda handler for CloudWatch Events
def schedule_entry(event, context):
    # What is the current time the lambda function is being run?
    currTime = datetime.datetime.now().time()
        
    # Print the current time this function was run
    print(currTime)
    
    # Get the scraped data from au.indeed.com and put it into result
    jobs = scraper.scrape_site("https://au.indeed.com/jobs?q=software+engineer&l=Canberra+ACT&sort=date")
    
    # Create our email Subject
    SUBJECT = "Daily Web Job Scraping"
    
    # The email body for recipients with non-HTML email clients.
    BODY_TEXT = ( "Daily Web Job Scraping\r\n"
             "You cannot receive HTML emails, sorry. "
             "Generated with AWS SDK for Python (Boto)."
                )

    # Create our HTML body for HTML email clients
    body = """ <html> <body>
        <h1> Daily Web Job Scraping </h1>
        <p> Hi There, here's your daily job list update! </p> """
    
    # Cycle through each job we found and append it to the body
    for j in jobs:
        body += """
        <p> <b>Job:</b> %s <br>
        <b>Company:</b> %s <br>
        <b>Description:</b> %s <br>
        <b>Location:</b> %s <br>
        <b>Date:</b> %s <br>
        <b>Salary:</b> %s </p>
        <b>Link:</b> %s </p>
        <br> """ %(j.get("title"), j.get("company"), j.get("description"), 
        j.get("location"), j.get("date"), j.get("salary"), j.get("link"))

    # End the body with final closing markers
    body += """
        </body>
        </html>
        """

    # Send the email with given parameters
    emailer.ses_email(SUBJECT, BODY_TEXT, body, "markmonteno@gmail.com", "markmonteno@gmail.com")
    
    # Return the scrapped data for debugging purposes
    return jobs
