from bs4 import BeautifulSoup
import requests


response = requests.get("https://books.toscrape.com/")
soup = BeautifulSoup(response.text, features="html.parser")

book = soup.find('h3')


print(book.text)

