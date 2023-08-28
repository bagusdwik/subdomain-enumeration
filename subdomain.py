import requests
from bs4 import BeautifulSoup

main_domain = "<YOUR_DOMAIN>"
response = requests.get(f"https://{main_domain}")

soup = BeautifulSoup(response.content, "html.parser")
subdomains = set()

for link in soup.find_all("a", href=True):
    href = link["href"]
    if main_domain in href:
        subdomain = href.split("//")[1].split(".")[0]
        subdomains.add(subdomain)
print("Subdomains:")
for subdomain in subdomains:
    print(subdomain)
