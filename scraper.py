import requests
from bs4 import BeautifulSoup

def scrape_data(source):
    response = requests.get(source)

    soup = BeautifulSoup(response.text, 'html.parser')
    judul_komik = soup.find_all("div", {"class": "ls2j"})

    judul_komik_terpopuler = []

    # Iterate through each element in judul_komik and extract the text from <a> tags
    for komik in judul_komik:
        for a in komik.find_all('h3'):
            for judul in a:
                # if judul.get_text() == '\n':
                #     continue
                judul_komik_terpopuler.append(judul.get_text())

    return judul_komik_terpopuler