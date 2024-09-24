import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.roughguides.com/destinations/' #Rough Guides page

#http request to the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

#find all recommended destination links
destination_elements = soup.find_all('a', class_='text-20 duration-150 hover:text-primary')

#extract destinations
destination_data = []

for element in destination_elements:
    destination_name = element.get_text(strip=True)
    destination_url = 'https://www.roughguides.com' + element['href']  # Append the base URL
    destination_data.append({
        'destination_name': destination_name,
        'destination_url': destination_url
    })

#search for books using the Open Library Search api (limit to 2 books)
def search_books(destination_name):
    #use the destination as query to find related books
    search_url = f"https://openlibrary.org/search.json?q={destination_name.replace(' ', '+')}&limit=5"
    response = requests.get(search_url)
    
    if response.status_code == 200:
        books_data = response.json().get('docs', [])
        books = []
        for book in books_data[:2]:  
            books.append({
                'title': book.get('title', 'No Title'),
                'author': ', '.join(book.get('author_name', ['No Author'])),
                'first_publish_year': book.get('first_publish_year', 'Unknown'),
                'cover_url': f"https://covers.openlibrary.org/b/id/{book.get('cover_i', '')}-M.jpg" if book.get('cover_i') else 'No Cover',
                'olid': book.get('key', '').split('/')[-1] if book.get('key') else 'No OLID'
            })
        return books
    else:
        print(f"Error fetching books for {destination_name}")
        return []


book_data = []  

for destination in destination_data:
    destination_name = destination['destination_name']
    print(f"Fetching books for: {destination_name}")
    
    books = search_books(destination_name)
    
    for book in books:
        book_data.append({
            'destination_name': destination_name,
            'destination_url': destination['destination_url'],
            'book_title': book['title'],
            'book_author': book['author'],
            'first_publish_year': book.get('first_publish_year', 'Unknown'),
        })
    
    time.sleep(1)


df = pd.DataFrame(book_data)
df.to_csv('destinations__books.csv', index=False)

print("Data saved to 'destinations__books.csv'")

