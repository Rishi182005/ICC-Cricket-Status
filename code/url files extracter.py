import requests
from bs4 import BeautifulSoup
import time

def fetch_and_display_data():
    # URL of the web page you want to scrape
    base_url = 'https://www.cricketworldcup.com/match/102763#overview'
    
    # Send a GET request to the URL
    response = requests.get(base_url)

    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Locate the <div> element with a specific class
        div_with_class = soup.find('div', class_='mc-scorebox__team-flags-container')  # Replace with the actual class name

        if div_with_class:
            # Print the content of the <div> element
            print(div_with_class.text)
        else:
            print('Div with class not found.')

    else:
        print('Failed to retrieve the web page. Status code:', response.status_code)

while True:
    fetch_and_display_data()
    time.sleep(5)  # Sleep for 5 seconds before fetching data again
