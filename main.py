from flask import Flask, render_template, request
import requests
import json
import pandas as pd
import sqlite3

app = Flask(__name__)
conn = sqlite3.connect('./database/animes_vistos.db')

class Anime():
    def __init__(self, id_anime, name_anime, chap_anime, stat_anime):
        self.id_anime = id_anime
        self.name_anime = name_anime
        self.chap_anime = chap_anime
        self.stat_anime = stat_anime
    
    def anime_info(self):
        print(self.id_anime)
        print(self.name_anime)
        print(self.chap_anime)
        print(self.stat_anime)

@app.route('/index.html')
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
    
@app.route('/anime_list', methods=['GET', 'POST'])
def anime_list():
    if request.method == 'GET':
        return render_template('anime_list.html')
    
    if request.method == 'POST':
        url = "https://api.jikan.moe/v4/anime?q=" + request.form['search']
        data = requests.get(url)
        results = json.loads(data.text)
        animes = results['data']
    
        anime = Anime(animes['mal_id'], animes['title'], animes['episodes'], animes['status'])
        anime.anime_info

if __name__ == '__main__':
    app.run(debug=True, port=4000)
