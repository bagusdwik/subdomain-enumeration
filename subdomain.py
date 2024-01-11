import requests
from bs4 import BeautifulSoup

main_domain = input("Enter the main domain (e.g., example.com): ")

while not main_domain:
    print("Main domain cannot be empty.")
    main_domain = input("Enter the main domain (e.g., example.com): ")

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
    print("https://" + subdomain + "." + main_domain)
