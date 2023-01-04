from flask import Flask
import requests
from lxml import html
#Load Libraries
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import httplib2


app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello_world():
    prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250903244-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'UA-250903244-1');
</script>
<a href="/logger">Logger</a>
<a href="/visitors"> Number of visitors</a>
<a href="/trend"> Trend</a>
 """
    print("watch out!")
    return prefix_google + "Hello World"


@app.route('/logger', methods=["GET"])
def logger():
    prefix_google = """
 <!-- Google tag (gstag.js) -->
<script>
 console.log('Watch out!')
</script>
<input id="textbox" type="text", size="40">
<button id="enter">enter</button>

<script>
const element = document.getElementById("enter")

element.addEventListener("click", myFunction)

function myFunction(){
    console.log(document.getElementById("textbox").value)
}
</script>

 """
 
    return prefix_google

#####################################       TP2         ################################################""


from flask import Flask, render_template
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
import os

VIEW_ID = os.getenv('VIEW_ID')

SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = 'data-sources-373514-95e8e4622a9d.json'


def initialize_analyticsreporting():
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      KEY_FILE_LOCATION, SCOPES)
  analytics = build('analyticsreporting', 'v4', credentials=credentials)

  return analytics


def get_report(analytics):
  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': '30daysAgo', 'endDate': 'today'}],
          'metrics': [{'expression': 'ga:pageviews'}],
          'dimensions': []
        }]
      }
  ).execute()


def get_visitors(response):
  visitors = 0 # in case there are no analytics available yet
  for report in response.get('reports', []):
    columnHeader = report.get('columnHeader', {})
    metricHeaders = columnHeader.get('metricHeader', {}).get('metricHeaderEntries', [])

    for row in report.get('data', {}).get('rows', []):
      dateRangeValues = row.get('metrics', [])

      for i, values in enumerate(dateRangeValues):
        for metricHeader, value in zip(metricHeaders, values.get('values')):
          visitors = value

  return str(visitors)

@app.route('/visitors', methods=["GET"])
def visitors():
  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  visitors = get_visitors(response)

  prefix_google = """
    <!-- Google tag (gtag.js) -->
    <script async
    src="https://www.googletagmanager.com/gtag/js?id=UA-250903244-1"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-250903244-1');
    </script>"""

  return prefix_google + "The number of visitors this last month is " + str(visitors)




if __name__ == '__main__':
    app.run()


