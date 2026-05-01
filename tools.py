import requests

SERP_API_KEY = "Your SERP API key"

def search_serp(query):
    url = "https://serpapi.com/search"

    params = {
        "q": query,
        "api_key": SERP_API_KEY
    }

    res = requests.get(url, params=params).json()

    results = []
    for r in res.get("organic_results", [])[:3]:
        results.append(r.get("snippet", ""))

    return "\n".join(results)