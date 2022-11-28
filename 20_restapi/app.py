'''
The Unkowns: JULIA LEE, AARON
SoftDEV
K20 restapi
11-22-2022
time spent: 30 minutes
'''

from flask import Flask
from flask import render_template
import requests #Make sure to pip install requests before using it!

app = Flask(__name__)

key = open("key_nasa.txt").read().strip() # Saves the key from key_nasa.txt

@app.route("/")
def image():
    web = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={key}") # Requests the html data
    url = web.json().get('url') # Gets the url from the data
    return render_template('main.html', url=url) # Returns template with url replaced

if __name__ == "__main__":
    app.debug = True
    app.run()
