from bs4 import BeautifulSoup
import time
import random
import requests
from docx import Document
from textblob import TextBlob
from retrieveComment import retrieveComment
    
with open("truspilot_data.csv", "w") as fichier:
    fichier.write("time;;company;;name;;rating;;comment\n")
compagnies = ["google.com", "microsoft.com", "ea.com", "apple.com", "nvidia.com", "amazon.com", "facebook.com", "teslamotors.com", "walmart.com", "www.samsung.com/uk", "coca-cola.com", "netflix.com", "adobe.com", "nike.com", "uber.com", "dior.com", ""]
with open("truspilot_data.csv", "a") as fichier:
    for company in compagnies:
        for page_number in range(1, 6):
            url = f"https://fr.trustpilot.com/review/www.{company}?page={page_number}"
            headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/122.0.0.0 Safari/537.36'
            ),
            'Accept-Language': 'fr-FR,fr;q=0.9,en;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://www.google.com/',
            'Connection': 'keep-alive'
            }
            try: 
                response = requests.get(url, headers=headers, timeout=10)
                response.raise_for_status()
                response = response.text
                soup = BeautifulSoup(response, "lxml")
                company_name = soup.find(
                    "span",
                    class_="typography_display-s__pKPhT typography_appearance-default__t8iAq title_displayName__9lGaz",
                ).text
                commentsSection = soup.find("div", class_="styles_wrapper__Fi9KX")
                articles = soup.findAll("div", class_="styles_cardWrapper__g8amG styles_show__Z8n7u")
                comments = []
                notesTotal = 0
                retrieveComment(company, fichier, articles)
                print("1tour\n")
                time.sleep(random.uniform(2, 5))
            except requests.exceptions.RequestException as e:
                break
