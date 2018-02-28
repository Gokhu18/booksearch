# booksearch 0.1 developed by matthew lyons

from bs4 import BeautifulSoup
import requests
import re
import webbrowser

headers = {'User-Agent': 'Mozilla/5.0'}
search = input("What book are you looking for? ")
terms = search.replace(" ", "+")
response = requests.get("http://www.booksamillion.com/search?id=7186925041035&query=" + terms)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.find('span', {'class': 'byline'})
info_a = results.get_text(strip=True)
isbn = re.sub('[^0-9]','', info_a)[:-4]

def cap_data():
    response = requests.get("https://www.barnesandnoble.com/w/?ean=" + isbn)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find('header', {'id': 'prodSummary-header'})
    results2 = results.find('h1', {'itemprop': 'name'})
    results3 = results.find('span', {'itemprop': 'author'})
    print()
    print(results2.get_text())
    print(f"by", results3.get_text())
    print()

def bn():
    response = requests.get("https://www.barnesandnoble.com/w/?ean=" + isbn)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find('div', {'id': 'commerce-zone'})
    results2 = results.find('div', {'class': 'hidden'})
    results3 = results2.find('span', {'itemprop': 'price'})
    print()
    print(results3.get_text())
    print()

def strand():
    response = requests.get("http://www.strandbooks.com/index.cfm?fuseaction=search.results&searchString=" + isbn)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'product-summary'})
    
    for result in results:
        print(result.find('div', 'price').get_text())

def bam():
    response = requests.get("http://www.booksamillion.com/search?query=" + isbn + "&filter=product_type%3Abooks")
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'meta'})

    print()
    for result in results:
        print(result.find('span', 'ebook-price').get_text())

greenlight = "http://www.greenlightbookstore.com/book/" + isbn 
tatteredcover = "http://www.tatteredcover.com/book/" + isbn
unabridged = "http://www.unabridgedbookstore.com/book/" + isbn
literati = "http://www.literatibookstore.com/book/" + isbn
bookpeople = "http://www.bookpeople.com/book/" + isbn

def multisearch(store):
    response = requests.get(store)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all('div', {'class': 'abaproduct-page-details'})

    for result in results:
        print(result.find('div', 'abaproduct-price').get_text())

print()
cap_data()
print()
print("Barnes & Noble:")
bn()
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
print("Strand (New York, NY): ")
strand()
print()

barnes_ = ["barnes & noble", "barnes and noble", "barnes", "b&n", "bn"]
booksamillion_ = ["bam", "books a million", "booksamillion", "books-a-million"]
tatteredcover_ = ["tattered cover", "tattered cover bookstore", "tattered", "denver", "co", "denver, co", "denver co"]
unabridged_ = ["unabridged", "unabridged bookstore", "chicago", "il", "chicago, il", "chicago il"]
greenlight_ = ["greenlight", "greenlight bookstore", "brooklyn", "brooklyn, ny", "brooklyn ny"]
literati_ = ["literati", "literati bookstore", "ann arbor", "mi", "ann arbor, mi", "ann arbor mi"]
bookpeople_ = ["bookpeople", "austin", "tx", "austin, tx", "austin tx"]
strand_ = ["strand", "new york", "ny"]

def purchase():
    mystore = input("Where would you like to buy your book? ")
    print()
    print("Redirecting...")
    print()
    if mystore.lower() in barnes_:
        webbrowser.open(f"https://www.barnesandnoble.com/w/?ean=" + isbn, new=1)
    elif mystore.lower() in booksamillion_:
        webbrowser.open(f"http://www.booksamillion.com/search?query=" + isbn + "&filter=product_type%3Abooks", new=1)
    elif mystore.lower() in tatteredcover_:
        webbrowser.open(f"http://www.tatteredcover.com/book/" + isbn, new=1)
    elif mystore.lower() in unabridged_:
        webbrowser.open(f"http://www.unabridgedbookstore.com/book/" + isbn, new=1)        
    elif mystore.lower() in greenlight_:
        webbrowser.open(f"http://www.greenlightbookstore.com/book/" + isbn, new=1)  
    elif mystore.lower() in literati_:
        webbrowser.open(f"http://www.literatibookstore.com/book/" + isbn, new=1)  
    elif mystore.lower() in bookpeople_:
        webbrowser.open(f"http://www.bookpeople.com/book/" + isbn, new=1)  
    elif mystore.lower() in strand_:
        webbrowser.open(f"http://www.strandbooks.com/index.cfm?fuseaction=search.results&searchString=" + isbn, new=1)     
    else:
        print("Not found.")
        purchase()

purchase()
