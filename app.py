import requests
import json
import pandas as pd

anime_name = "mashle"

data = requests.get(f'https://api.jikan.moe/v4/anime?q={anime_name}')
results = json.loads(data.text)
df = pd.json_normalize(results)

# df2 = df.data # Éste es un objeto de Pandas
# df2 = df.data[0] # Ésta es una lista
df2 = df.data[0][0] # Éste es un diccionario

anime_title = df2['title']
anime_airing = df2['airing']
anime_NoChapters = df2['episodes']

if anime_airing == True:
    print(f'{anime_title} sigue vigente y tiene {anime_NoChapters} capítulos')
else:
    print(f'{anime_title} ya terminó y tuvo {anime_NoChapters} capítulos')
