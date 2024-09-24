# Rough Guides Destination Book Recommendations

## Overview

This project scrapes travel destination information from the **Rough Guides** website and uses the **Open Library Search API** to fetch related books for each destination. It generates a CSV file that contains destination names, their URLs on Rough Guides, and two recommended books for each destination with details such as title, author, and the year of first publication.

### Features

- Scrapes travel destinations and URLs from the Rough Guides website.
- Fetches related books for each destination using the Open Library Search API.
- Saves the results in a CSV file with book titles, authors, publication years, and cover image URLs.

## Technologies Used

- **Python**: The main programming language for this project.
- **BeautifulSoup**: For web scraping travel destinations from the Rough Guides website.
- **Requests**: To make HTTP requests to both the Rough Guides website and the Open Library Search API.
- **Pandas**: For structuring the scraped data and saving it to a CSV file.

## Installation

- Python 3.x
- Install the required Python libraries:
  ```bash
  pip install requests beautifulsoup4 pandas
  ```

## Usage

1. **Scraping Destinations**:
   - The script sends a request to the **Rough Guides** destination page and extracts the destination names and their URLs.
2. **Fetching Books**:
   - For each destination, it uses the **Open Library Search API** to find books related to that destination and returns up to 2 books for each location.
3. **Saving Data**:
   - The data is saved in a CSV file containing the following columns:
     - `destination_name`: The name of the travel destination.
     - `destination_url`: The Rough Guides URL for that destination.
     - `book_title`: The title of a related book.
     - `book_author`: The author(s) of the book.
     - `first_publish_year`: The year the book was first published.

### Example CSV Output:

```csv
destination_name,destination_url,book_title,book_author,first_publish_year,
Albania,https://www.roughguides.com/albania/,Albania: A Modern History,Fisher Bernd J,199
Brazil,https://www.roughguides.com/brazil/,Brazil on the Rise,Larry Rohter,2010
...
```

## API Used

- **Open Library Search API**:
  - The Open Library API is used to search for books by querying the destination name. The search results return book details, including title, author, publication year, and cover image if available.
  - More details: [Open Library Search API Documentation](https://openlibrary.org/dev/docs/api/search)
