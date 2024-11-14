# Mandatory components to be imported
from flask import Flask, render_template, request
# To view the flask response, which contains json data
import json
# Used for fetching URLs
import urllib.request

# Name the current component
app = Flask(__name__)


# This route method binds URL only when submit button is clicked in the POST or GET method. This route URL will be mentioned in form action of html template.
@app.route('/', methods=['POST', 'GET'])
def details():
    location = input("Enter the location here: ")
    api_key = '6735c15fe12e6074928577lere6a5be'
    
    try:
        src = 'https://geocode.maps.co/search?q='+location+'&api_key='+api_key
        #print(src)
        source = urllib.request.urlopen(src).read()
        #print(source)
        responseData = json.loads(source)
        print(responseData[0]['lat'])
        print(responseData[0]['lon'])
        data = {
			#"latitute" : str(responseData['items'][0]['position']['lat']),
			#"longitute" : str(responseData['items'][0]['position']['lng']),
            "latitute" :  str(responseData[0]['lat']),
            "longitute" : str(responseData[0]['lon']),
		}
        return render_template('index.html',data=data,apikey=api_key)    # exception handling
    except (Exception):
        # pass the error message that need to be displayed in html template
        return render_template('index.html',error="Give the correct location") 


# route method that need to be called on first hit to render empty html template
#@app.route('/')
#def index():
#    return render_template('index.html')