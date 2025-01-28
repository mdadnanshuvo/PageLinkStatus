import requests
from scraper.meta_scraper import scrape_meta_content
from config import BASE_URL

def main():
    print(f"Starting to scrape {BASE_URL}")

    # Fetch the page content
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        page_content = response.text

        # Scrape and print meta content
        meta_data = scrape_meta_content(page_content)
        for key, value in meta_data.items():
            print(f"{key}: {value}")   
    else:
        print("Failed to retrieve the page")

if __name__ == "__main__":
    main()
