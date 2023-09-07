import requests
from bs4 import BeautifulSoup

# Replace with the URL of the paper's Google Scholar page
url = "https://scholar.google.com/some-paper-url"

# Send an HTTP GET request to the Google Scholar page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, "html.parser")

    # Find the element containing the number of citations
    citations_element = soup.find("a", {"class": "gs_or_cit"})

    if citations_element:
        # Extract and print the number of citations
        citations_text = citations_element.text
        print("Number of Citations:", citations_text)
    else:
        print("Citation count not found on the page.")
else:
    print("Failed to retrieve the page. Status code:", response.status_code)
