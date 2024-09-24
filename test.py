# Step 1: Scraping TripAdvisor's Traveler's Choice Destination Data
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of TripAdvisor's Traveler's Choice Destinations
url = 'https://www.tripadvisor.com/TravelersChoice-Destinations'

# Send an HTTP request to the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all destination elements using the <h2> tag with the class 'biGQs _P fiohW EVnyE'
destinations = soup.find_all('h2', class_='biGQs _P fiohW EVnyE')
destination_data = []

for destination in destinations:
    try:
        # Get the destination name
        destination_name = destination.get_text(strip=True)
        destination_data.append({
            'destination_name': destination_name,
            'destination_description': 'N/A'  # Placeholder for now
        })
    except AttributeError:
        continue

# Print scraped destinations to verify
if destination_data:
    print("Successfully scraped destinations:")
    for i, dest in enumerate(destination_data[:5], 1):  # Show first 5 scraped destinations
        print(f"{i}. {dest['destination_name']}")
else:
    print("No destinations were scraped.")
