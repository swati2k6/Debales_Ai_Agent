import requests
from bs4 import BeautifulSoup

URLS = [
    "https://debales.ai/",
]

def scrape():
    texts = []

    for url in URLS:
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            for p in soup.find_all("p"):
                texts.append(p.get_text())
        except:
            pass

    return "\n".join(texts)


if __name__ == "__main__":
    data = scrape()

    with open("debales.txt", "w", encoding="utf-8") as f:
        f.write(data)

    print("✅ Scraping done")