import requests

websites = [
    "https://google.com",
    "https://github.com",
    "https://python.org"
]

for website in websites:
    try:
        response = requests.get(website, timeout=5)

        if response.status_code == 200:
            print(f"{website} -> ONLINE")
        else:
            print(f"{website} -> STATUS {response.status_code}")

    except requests.RequestException:
        print(f"{website} -> OFFLINE")
