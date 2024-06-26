# -*- coding: utf-8 -*-
"""Web_Scraping.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11CM4e-bjmPIV9A4kW5hLZLoJ1HOnQHO7
"""

pip install beautifulsoup4

import requests
from bs4 import BeautifulSoup

def get_filmography(actor):

    formatted_actor = '_'.join(actor.split())
    url = f"https://en.wikipedia.org/wiki/{formatted_actor}_filmography"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        filmography_table = soup.find('table', class_='wikitable')
        if filmography_table:
            filmography = []
            rows = filmography_table.find_all('tr')[1:]  # Skip the header row
            for row in rows:
                cells = row.find_all(['td', 'th'])
                title = cells[0].text.strip()
                year = cells[1].text.strip()
                filmography.append((title, year))
            return filmography
        else:
            print("Error: Filmography table not found on Wikipedia.")
            return None
    else:
        print("Error: Unable to fetch data from Wikipedia.")
        return None

actor_name = input("Enter the name of the actor: ")
filmography = get_filmography(actor_name)
if filmography:
    print(f"Filmography of {actor_name}:")
    for movie, year in filmography:
        print(f"{movie} ({year})")