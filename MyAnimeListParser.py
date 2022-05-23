import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
import random



page_limits = ['0', '50', '100', '150', '200']
header = {"Accept-Language": 'en-US'}

#creating csv file to store information
file = open('anime_rankings.csv', 'w', encoding="UTF-8_sig", newline='\n')
file_obj = csv.writer(file)



for limit in page_limits:

# parsing myanimelist.net anime rankings
    url = f"https://myanimelist.net/topanime.php?limit={limit}"
    result = requests.get(url, headers=header)
    content = result.text
    soup = BeautifulSoup(content, "html.parser")

    table = soup.find('table', class_="top-ranking-table")
    animes = table.find_all('tr', class_="ranking-list")

# from anime rankings selecting each anime title, IMDB score and ranking
    for anime in animes:
        ranking = anime.td.text.strip()
        title = anime.h3.text
        score = anime.find('td', class_='score ac fs14').text.strip()
        print(f'Anime: {title}, ranking: {ranking}, IMDB score: {score}')

# saving info in the csv file created above
        file_obj.writerow([title, ranking, score])

# sending requests with different time interval for different pages of the website
    sleep(random.randint(5, 10))

file.close()
