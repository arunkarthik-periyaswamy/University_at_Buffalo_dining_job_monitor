import requests
from bs4 import BeautifulSoup
import time
import http.client, urllib
from datetime import datetime

def check_website(url, keyword, not_in_key):
    try:
        # Send a GET request to the website
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find the keyword in the page content
            if keyword.lower() in soup.get_text().lower():
                notify(keyword, url)
            elif not_in_key.lower() not in soup.get_text().lower():
                notify(keyword, url)
        else:
            print(f"Error: {response.status_code}")
            notify(keyword="!Error!", url=url)
    except Exception as e:
        print(f"An error occurred: {e}")
        notify(keyword="!Eexception!", url=url)

def notify(keyword, url):
    print()
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "afy2w5389dvunczpv5eruedztxaa3v",
        "user": "u78zwq6gfm5pvz6hxgvr1819vvno4k",
        "message": f"UB part time job {keyword} at time {datetime.now} ",
        "priority": 1,
        "title": "UB Dining",
        "url": url,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

if __name__ == "__main__":
    website_url = "https://ubdining.com/jobs/student-jobs"
    keyword_to_monitor = "closed"
    not_in_key = "opened"
    
    while True:
        check_website(website_url, keyword_to_monitor, not_in_key)
        time.sleep(60)  # Check every 60 seconds (adjust as needed)