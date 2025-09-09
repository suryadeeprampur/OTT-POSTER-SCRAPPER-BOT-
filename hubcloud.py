# hubcloud.py
import re
import requests
from bs4 import BeautifulSoup

# Headers to mimic a browser
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0 Safari/537.36"
    )
}

def hubcloud_scraper(url: str) -> dict:
    """
    Scrape HubCloud / GDLink style pages to extract download links.
    Returns a dict with {'title': ..., 'links': [...]}.
    """

    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        res.raise_for_status()
    except Exception as e:
        return {"error": f"❌ Failed to fetch page: {e}"}

    soup = BeautifulSoup(res.text, "html.parser")

    # Title
    title = soup.title.string.strip() if soup.title else "HubCloud File"

    # Find links (HubCloud often stores links inside <a> tags with "download" or "hubcloud" text)
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "hubcloud" in href or "gdlink" in href or "download" in href:
            links.append(href)

    # If no links found, try regex
    if not links:
        links = re.findall(r"https?://[^\s'\"]+", res.text)
        links = [l for l in links if "hubcloud" in l or "gdlink" in l]

    return {
        "title": title,
        "links": links if links else ["❌ No links found"]
    }


# ----------------- For Testing ----------------- #
if __name__ == "__main__":
    test_url = "https://hubcloud.link/example"  # Replace with real
    result = hubcloud_scraper(test_url)
    print(result)
