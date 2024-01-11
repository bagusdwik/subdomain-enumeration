import requests
from bs4 import BeautifulSoup

main_domain = "umsida.ac.id"
response = requests.get(f"https://{main_domain}")

soup = BeautifulSoup(response.content, "html.parser")
subdomains = set()

for link in soup.find_all("a", href=True):
    href = link["href"]
    if main_domain in href:
        parts = href.split("//")
        if len(parts) > 1:
            subdomain = parts[1].split(".")[0]
            subdomains.add(subdomain)

print("Subdomains:")
for subdomain in subdomains:
    print(subdomain)
