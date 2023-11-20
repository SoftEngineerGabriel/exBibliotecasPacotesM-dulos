#12. Escreva um programa que importe o pacote beautifulsoup4 e faça a raspagem de dados (web crawling) de uma página HTML.

import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

print(soup.title)