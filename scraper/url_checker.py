import aiohttp
import asyncio
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
