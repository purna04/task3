import requests
from bs4 import BeautifulSoup

#url of the webpage to scrape
url='https://www.geeksforgeeks.org/what-is-web-scraping-and-how-to-use-it/' #Replace with the URL of the web page you want to scrape

# send a GET request to the web page
response = request.get(url)

# check if the request was successful
if response.status_code ==200:
    # parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract all the text from the page
    page_text = soup.get_text()

    #Extract all the links from the page
    links = [a['href'] for a in soup.find_all('a',href=True)]

    # Extract all the images from the page
    images = [img['src'] for img in soup.find_all('img', src=True)]

    # Print the extacted data
    print("page Text:")
    print(page_text)

    print("\nLinks:")
    for link in links:
        print(link)

        print("\nImages:")
        for image in images:
            print(image)
else:
    print(f"Faileed to retrive the web page.Status code:{response.status_code}")
                