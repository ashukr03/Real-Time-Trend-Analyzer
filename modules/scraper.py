import requests
from bs4 import BeautifulSoup

URL = "https://news.google.com/rss?hl=en-IN&gl=IN&ceid=IN:en"

def get_headlines():
    headlines = []

    try:
        response = requests.get(URL, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "xml")

        items = soup.find_all("item")

        for item in items:
            title = item.title.get_text(strip=True)
            if len(title) > 10:
                headlines.append(title)

    except Exception as e:
        print("Scraping Error:", e)

    return headlines


# TEST Total Headlines
if __name__ == "__main__":
    data = get_headlines()
    print("TOTAL HEADLINES:", len(data))
    for h in data[:15]:
        print("-", h)
