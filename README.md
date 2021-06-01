# Job-Scraper
A simple, yet in-depth system that manages to gather and provide information on job offers in an easy to access format

- Integrates Amazon Web Services to create a 'back-end'
- Implements a Serverless Computing architecture
- Uses Serverless framework to help with deployment to AWS Lambda
- Uses Gatsby for static site generation to act as a front-end view
- Easily scalable and expandable

## Contents
- [Todo](#todo)
- [Architecutre](#architecutre)
- [Prerequisites](#prerequisites)
- [Deployment](#deployment)
- [Examples](#examples)
	- [Screenshots](#screenshots)
- [References](#references)

## Architecture
img to be added

## Prerequisites
Python required for the serverless portion of project

Required:
Serverless Framework
```
npm install serverless -g
```

Gatsby
```
npm install --global gatsby-cli
```

## Deployment
Deployment is fairly easy, but requires an existing AWS account and pre-configured Serverless credentials.

Step 1: Deploy to AWS Lambda using Serverless
```
serverless deploy
```
Examples output:
```
...
service: aws-simple-scraper
stage: dev
region: us-west-2
stack: aws-simple-scraper-dev
api keys:
  None
endpoints:
  GET - https://xxx.execute-api.us-west-2.amazonaws.com/dev/ping
functions:
  scheduled-cron: aws-simple-scraper-dev-scheduled-cron
  http-get: aws-simple-scraper-dev-http-get
...
```

Step 2: Change endpoint in web front-end from above step in pages/index.js
```javascript
axios.get('https://xxx.execute-api.us-west-2.amazonaws.com/dev/ping')
            .then(response => {
                this.setState({
                    apiData: response.data.message
                })
            })
            .catch(err => console.log(err))
```
Replace 'xxx' with your endpoint

Step 3: Change email information in Lambda function handler.py
```python
emailer.ses_email(SUBJECT, BODY_TEXT, body, "sender@domain.com", "receiver@domain.com")
```

Step 4: Test with Gatsby
```
gatsby build
gatsby serve
```
Example output:
```

   ┌──────────────────────────────────────────────────┐
   │                                                  │
   │   Serving!                                       │
   │                                                  │
   │   - Local:            http://localhost:9000      │
   │   - On Your Network:  http://192.168.20.2:9000   │
   │                                                  │
   │   Copied local address to clipboard!             │
   │                                                  │
   └──────────────────────────────────────────────────┘
```
Step 5: Deploy with your method of choice

## Examples

### Screenshots

Screenshot1:
![job-scraper](https://user-images.githubusercontent.com/11038569/39620113-6c4714a4-4fcd-11e8-8a52-4c3c9801f2c6.png)
Screenshot 2:
![job-scraper-email](https://user-images.githubusercontent.com/11038569/39620118-71380dd8-4fcd-11e8-81e1-bcb20a16de81.png)

## References

Amazon Web Services, Inc. 2018, _AWS Lambda Features_, accessed 1 May 2018, <https://aws.amazon.com/lambda/features/>.

Amazon Web Services, Inc. 2018, _AWS Lambda Function Versioning and Aliases_, accessed 1 May 2018, <https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html>.

Google, 2018, _Google Cloud Functions_, accessed 2 May 2018, <https://cloud.google.com/functions/>.

Google, 2018, Writing Cloud Functions, accessed 2 May 2018, <https://cloud.google.com/functions/docs/writing/>.

Microsoft, 2018, _Functions_, accessed 3 May 2018, <https://azure.microsoft.com/en-au/services/functions/>.

Microsoft, 2018, _SLA for Functions_, accessed 3 May 2018, <https://azure.microsoft.com/en-au/support/legal/sla/functions/v1_0/>.

Synergy Research Group, 2018, _Cloud Growth Rate Increased Again in Q1; Amazon Maintains Market Share Dominance_, accessed 1 May 2018, <https://www.srgresearch.com/articles/cloud-growth-rate-increased-again-q1-amazon-maintains-market-share-dominance>.
