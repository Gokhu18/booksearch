# booksearch 0.1 developed by matthew lyons

from bs4 import BeautifulSoup
import requests

def cap_data():
    response = requests.get("https://www.alibris.com/booksearch?title=" + terms)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find_all('div', {'class': 'product-title'})
    synopsis = soup.find_all('p', {'id': 'synopsis-detail'})
    for result in title:
        print(result.find('h1').get_text())
        print(result.find('h2').get_text())

    for result in synopsis:
        print(result.get_text())

def bn():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get("https://www.barnesandnoble.com/s/" + terms)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'product-shelf-info'})

    for result in results:
        print(result.find('div', 'product-shelf-pricing').get_text())

def strand():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get("http://www.strandbooks.com/index.cfm?fuseaction=search.results&searchString=" + terms)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'product-summary'})
    
    for result in results:
        print(result.find('div', 'price').get_text())

def bam():
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get("http://www.booksamillion.com/search?query=" + terms + "&filter=product_type%3Abooks")
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'meta'})

    for result in results:
        print(result.find('span', 'ebook-price').get_text())

def multisearch(store):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(store)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'abaproduct-details'})

    for result in results:
        print(result.find('h3').get_text())

search = input("What book are you looking for? ")
terms = search.replace(" ", "+")

greenlight = "http://www.greenlightbookstore.com/search/site/" + terms 
tatteredcover = "http://www.tatteredcover.com/search/site/" + terms
unabridged = "http://www.unabridgedbookstore.com/search/site/" + terms
literati = "http://www.literatibookstore.com/search/site/" + terms
bookpeople = "http://www.bookpeople.com/search/site/" + terms

print()
cap_data()
print()
print("Barnes & Noble:")
bn()
print("Strand (New York, NY): ")
strand()
print("Books-A-Million:")
bam()
print()

print("Tattered Cover Bookstore (Denver, CO):")
multisearch(tatteredcover)
print()
print("Unabridged Books (Chicago, IL):")
multisearch(unabridged)
print()
print("Greeenlight Bookstore (Brooklyn, NY):")
multisearch(greenlight)
print()
print("Literati Bookstore (Ann Arbor, MI):")
multisearch(literati)
print()
print("Bookpeople (Austin, TX):")
multisearch(bookpeople)
print()
