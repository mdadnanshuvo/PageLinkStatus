import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import random

async def check_url_status(url, session):
    """Asynchronously check the HTTP status code of a URL with error handling"""
    try:
        async with session.get(url, timeout=10) as response:
            return url, response.status
    except asyncio.TimeoutError:
        return url, "Timeout"
    except aiohttp.ClientError as e:
        return url, f"Client Error: {e}"
    except Exception as e:
        return url, f"Error: {e}"

async def check_url_sequentially(urls):
    """Check all URLs sequentially with delays between each request"""
    async with aiohttp.ClientSession() as session:
        for url in urls:
            result = await check_url_status(url, session)
            print(f"URL: {result[0]}, Status: {result[1]}")
            # Introduce a small delay between requests to avoid overloading the server
            await asyncio.sleep(random.uniform(0.5, 2.0))  # Random delay between 0.5 and 2 seconds

def scrape_anchors_and_check_urls(page_url):
    """Scrape anchor tags from a page and check their URLs sequentially with proper rate-limiting"""
    # Step 1: Fetch the page content
    response = requests.get(page_url)
    if response.status_code == 200:
        html_content = response.text
        
        # Step 2: Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Step 3: Find all anchor tags (<a>) and extract the href attribute
        anchor_tags = soup.find_all('a', href=True)  # This finds all <a> tags with href attribute
        
        # Step 4: Extract the URLs from the href attributes
        urls_to_check = [anchor['href'] for anchor in anchor_tags if anchor['href'].startswith('http')]
        
        # Step 5: Check the URLs one by one
        asyncio.run(check_url_sequentially(urls_to_check))
    else:
        print(f"Failed to retrieve the page: {page_url}")
