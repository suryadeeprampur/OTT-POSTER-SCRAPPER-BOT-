# fsub.py
import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0 Safari/537.36"
    )
}

def fsub_scraper(url: str) -> dict:
    """
    Scrape Fsub-style pages to extract download links.
    Returns a dict with {'title': ..., 'links': [...]}.
    """

    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        res.raise_for_status()
    except Exception as e:
        return {"error": f"❌ Failed to fetch page: {e}"}

    soup = BeautifulSoup(res.text, "html.parser")

    # Extract title
    title = soup.title.string.strip() if soup.title else "Fsub File"

    # Find download links (usually in <a> tags)
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if "fsub" in href or "drive.google" in href or "gdlink" in href:
            links.append(href)

    # If no links found, fallback to regex
    if not links:
        links = re.findall(r"https?://[^\s'\"]+", res.text)
        links = [l for l in links if "fsub" in l or "drive.google" in l or "gdlink" in l]

    return {
        "title": title,
        "links": links if links else ["❌ No links found"]
    }


# ----------------- For Testing ----------------- #
if __name__ == "__main__":
    test_url = "https://fsub.link/example"  # Replace with real Fsub URL
    result = fsub_scraper(test_url)
    print(result)
