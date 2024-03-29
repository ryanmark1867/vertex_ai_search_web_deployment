# example of using Flask to serve a simple web page
import json
import os
import urllib.request
from io import StringIO
import requests
from flask import Flask, render_template, request





app = Flask(__name__)


@app.route('/')
def index():   
    ''' render index.html - page that is served at localhost'''
    title_text = "Test widget generated for Vertex AI Search app"
    title = {'titlename':title_text}
    return render_template('index.html',title=title) 
    

    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')