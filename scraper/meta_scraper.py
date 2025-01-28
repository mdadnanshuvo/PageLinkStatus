from bs4 import BeautifulSoup


def scrape_meta_content(page_content):
    """Extract meta tags (title, description, og:title, og:description)"""
    soup = BeautifulSoup(page_content, "lxml")

    # Extract meta title using <title> tag
    meta_title = soup.title.string if soup.title else "Not available"

    # Extract meta description and Open Graph tags
    meta_description = soup.find("meta", attrs={"name": "description"})
    og_title = soup.find("meta", attrs={"property": "og:title"})
    og_description = soup.find("meta", attrs={"property": "og:description"})

    meta_data = {
        "meta_title": meta_title,
        "meta_description": (
            meta_description.get("content") if meta_description else "Not available"
        ),
        "og_title": og_title.get("content") if og_title else "Not available",
        "og_description": (
            og_description.get("content") if og_description else "Not available"
        ),
    }

    return meta_data
