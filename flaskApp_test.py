from flask import Flask,render_template
#from google.cloud import language
#from google.cloud.language import enums
#from google.cloud.language import types

app = Flask(__name__)
# Instantiates a client
#client = language.LanguageServiceClient()

# The text to analyze
#text = u'Hello, world!'
#document = types.Document(
    #content=text,
    #type=enums.Document.Type.PLAIN_TEXT)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/npl')
def npl():
  #  response= client.analyze_sentiment(
  #  document=document,
  #  encoding_type='UTF32',
  #  )
    report=[]
  #  for sent in response.sentences:
  #     print sent.text.content
  #     print sent.sentiment.magnitude
  #    print sent.sentiment.score
    return render_template('nplTest.html', data=report)
