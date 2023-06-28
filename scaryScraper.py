import requests
from bs4 import BeautifulSoup
import pandas as pd
# import der erfordelichen Module
# Beispiel einer sehr vereinfachten scraping Anwendung
# URL der Website, die gescraped werden soll
url = 'https://www.amazon.com/dp/B07PZZ4S2L'

# HTTP GET-Anfrage senden
response = requests.get(url)

# BeautifulSoup-Objekt erstellen
soup = BeautifulSoup(response.text, 'html.parser')

# Titel des Produkts extrahieren
title = soup.find(id='productTitle').get_text().strip()

# Preis des Produkts extrahieren
price = soup.find(id='priceblock_ourprice').get_text()

# Daten in ein DataFrame speichern
data = {'Title': [title], 'Price': [price]}
df = pd.DataFrame(data)

# DataFrame anzeigen
print(df)