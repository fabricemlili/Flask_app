from flask import Flask
import logging

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
<button class="favorite styled"
        type="button">
    Connect you bitches
</button>
<a href="logger" target="_self">Logger</a>
 """
 print("watch out!")
 return prefix_google + "Hello World"




@app.route('/logger', methods=["GET"])

def logger():
 prefix_google = """
 <!-- Google tag (gstag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250903244-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', 'UA-250903244-1');
</script>
<script>
 console.log('Watch out!')
</script>

 """
 print("watch out!")
 return prefix_google