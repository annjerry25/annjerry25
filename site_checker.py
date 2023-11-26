import requests

def check_website_connectivity(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx status codes)
        print(f"{url} is accessible (Status Code: {response.status_code})")
    except requests.RequestException as e:
        print(f"{url} is not accessible. Error: {e}")

websites = ["http://www.ajaysspecialtees.tech", "https://www.google.com", "https://www.blackpast.org/special-features/african-capitals/"]

for website in websites:
    check_website_connectivity(website)

