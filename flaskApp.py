from flask import Flask,render_template
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import pandas as pd

app = Flask(__name__)
# Instantiates a client
client = language.LanguageServiceClient()

# Takes response from google language and sorts for top 3 sentiment phrases as summary
def createSummary(response,title):
    report={
            'words':    [],
            'mags':     [],
            'scores':   []
        }
    for sent in response.sentences:
        words=sent.text.content
        mag=sent.sentiment.magnitude
        score=sent.sentiment.magnitude
        report['words'].append(words)
        report['mags'].append(mag)
        report['scores'].append(score)
    repDF=pd.DataFrame(report).sort_values('mags',ascending=False)
    summary=[title,repDF['words'][0],repDF['words'][1],repDF['words'][2]]
    return summary


    
    

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/npl')
def npl():
    # The text to analyze
    with open('article.txt','r') as article:
        text=article.read()
        title=text[0:text.find('\n')]
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT
        )

        response= client.analyze_sentiment(
            document=document,
            encoding_type='UTF32',
        )

    summary=createSummary(response,title); 

    return render_template('nplTest.html', data=summary)
