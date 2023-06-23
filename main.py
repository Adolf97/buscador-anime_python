from flask import Flask, render_template, request
import requests
import json
import pandas as pd
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('./database/animes_vistos.db')

@app.route('/', methods=['POST', 'GET'])
def index():
    
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.form['search']:
        url = "https://api.jikan.moe/v4/anime?q=" + request.form['search']
        data = requests.get(url)
        results = json.loads(data.text)
        return render_template('index.html', animes = results['data'])
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=4000)
