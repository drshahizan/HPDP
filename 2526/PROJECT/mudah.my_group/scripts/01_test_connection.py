import requests
import json

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json",
    "Referer": "https://www.mudah.my/malaysia/properties-for-sale"
}

url = "https://www.mudah.my/_next/data/ZZIvdMD681zu5P-pSGeHT/list.json?category=2000&type=sell&o=1"

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    ads = data["pageProps"]["initialStore"]["ads"]

    print("Number of records found:", len(ads))

    if len(ads) > 0:
        first = ads[0]
        print("\nFirst listing sample:")
        print(json.dumps(first, indent=2)[:2000])
else:
    print("Failed to access page.")
    print(response.text[:500])