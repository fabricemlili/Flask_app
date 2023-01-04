from flask import Flask, render_template


app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True

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
<a href="/trend">Google Trend</a><br>
<a href="/counter">Counter</a><br>
 """
    return prefix_google

###########################         Google trend        #############################################""

from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime

@app.route('/trend', methods=["GET"])
def trend():

    pytrends = TrendReq(hl='en-US', tz=360)

    kw_list=['Yahoo','Google']
    pytrends.build_payload(kw_list, timeframe='2022-01-09 2023-01-01', geo='US')
    df = pytrends.interest_over_time()
    yahoo_data = df['Yahoo'].values.tolist()
    google_data = df['Google'].values.tolist()
    dates = [datetime.fromtimestamp(int(date/1e9)).date().isoformat() for date in df.index.values.tolist()]

    params = {
        "type": 'line',
            "data": {
                "labels": dates,
                "datasets": [{
                    "label": 'Yahoo',
                    "data": yahoo_data,
                    "borderColor": '#3e95cd',
                    "fill": 'false',
                },
                {
                    "label": 'Google',
                    "data": google_data,
                    "borderColor": '#ffce56',
                    "fill": 'false',
                }
                ]
            },
            "options": {
                "title": {
                    "text": 'My Line Chart'
                },
                "scales": {
                    "yAxes": [{
                        "ticks": {
                            "beginAtZero": 'true'
                        }
                    }]
                }
            }
    }
    
    
    
    prefix_google = """

    <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>

    <canvas id="myChart" width="50" height="50"></canvas>""" + f"""
    <script>
    var ctx = document.getElementById('myChart');
    var myChart = new Chart(ctx, {params});
    </script>

    """

    return prefix_google


###########################        Timer Log        #############################################""

import time
from collections import Counter


@app.route('/counter')
def counter():
    prefix_google = """<a href="/">Home</a><br>"""
    # Download Shakespear artwork
    with open('shakespeare.txt', 'r') as f:
        text = f.read()
    start_time = time.time()
    word_count_dict = count_words_dict(text)
    f1 = f"The time to compute with dict is {time.time() - start_time}"
    start_time = time.time()
    word_count_counter = count_words_counter(text)
    f2 = f"The time to compute with Counter function is {time.time() - start_time}"
    return prefix_google + f"""{f1}<br><br><br>{f2}<br><br><br><br><br>{word_count_dict}<br><br><br><br><br>   {word_count_counter}"""


def count_words_dict(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def count_words_counter(text):
    return Counter(text.split())



if __name__ == '__main__':
    app.run()