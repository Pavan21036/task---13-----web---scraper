
import requests
from bs4 import BeautifulSoup
import csv

URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    with open("data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Quote", "Author", "Author Link"])

        for quote in quotes:
            text = quote.find("span", class_="text")
            author = quote.find("small", class_="author")
            link = quote.find("a")

            # Handle missing tags safely
            text = text.text if text else "N/A"
            author = author.text if author else "N/A"
            link = link["href"] if link else "N/A"

            writer.writerow([text, author, link])

    print("Data scraped and saved to data.csv")

else:
    print("Failed to fetch page. Status code:", response.status_code)
