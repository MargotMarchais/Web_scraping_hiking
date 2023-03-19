import requests
from bs4 import BeautifulSoup
import html
import pandas as pd
import csv

# Website 
url = "https://www.decathlontravel.com/voyages/sport-randonnee-trekking"

# Empty lists that will receive the scraped information
name_list = []
destination_list = []
URL_list = []
travel_image_list = []
duration_list = []
price_list = []
#difficulty_level_list = []
activity_list = []
travel_type_list = []

# We can only get 12 results per page -> We repeat the same operation for several pages
for x in range(1,30):

    # Get request (obtained from INSOMNIA)
    querystring = {"page":f"{x}","theme^%^5B0^%^5D":"13"}

    payload = ""
    headers = {
        "authority": "www.decathlontravel.com",
        "accept": "text/html, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "cookie": "aaa=QcQ6EuWintOc1a^%^2FumaAtmK2c4rSvJkgTpVaF43fm32lasRDP6bwLZtmM^%^2F3diis4m1UjD5^%^2FFmWGZMCugB^%^2BDKdzBwqCWxMpFouIhWwkgE9yscJTHw^%^2F7wANLElE0Q8WjHknuDorwcTmZhWMmWJa49iIPps8U4blhF6CN6eyoTDjpbI^%^3D; PHPSESSID=d8f391489d145af59b9927e6840426b3; didomi_token=eyJ1c2VyX2lkIjoiMTg2ZjRjYTAtMWY3Yy02MjI1LWJmNzctMGM0MDhmNzllOWZiIiwiY3JlYXRlZCI6IjIwMjMtMDMtMThUMTI6NTU6MjYuNzU3WiIsInVwZGF0ZWQiOiIyMDIzLTAzLTE4VDEyOjU1OjI2Ljc1N1oiLCJ2ZW5kb3JzIjp7ImRpc2FibGVkIjpbImdvb2dsZSIsImM6ZmFjZWJvb2thLVF5TURMR0pRIiwiYzphZHZlbnR1cmUtcXhlZ2F5SFQiLCJjOmdvb2dsZWFuYS00VFhuSmlnUiIsImM6em9oby1iVWFEY3BhRCIsImM6Y29va2llc2FuLWFZN1dla0tyIiwiYzpob3RqYXItamV5aUZQZ0UiLCJjOmdvb2dsZWFkcy1BazMyVFBEQSIsImM6Y29udGVudHNxLVZ4UWNNenBIIl19LCJwdXJwb3NlcyI6eyJkaXNhYmxlZCI6WyJtYXJrZXRpbmctTVJaVnByZWEiLCJwZXJzb25hbGlzLVZqWVVyYkxYIiwiYW5hbHl0aWNzLUdNZ0JXR1RoIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIiwiYzphZHZlbnR1cmUtcXhlZ2F5SFQiXX0sInB1cnBvc2VzX2xpIjp7ImVuYWJsZWQiOlsicGVyc29uYWxpcy1WallVcmJMWCJdfSwidmVyc2lvbiI6MiwiYWMiOiJBQUFBLkFVYUFDQVVZIn0=; euconsent-v2=CPo0fYAPo0fYAAHABBENC7CgAAAAAE7AAAAAAAALzgAgLzAA.YAAACdgAAAAA; newsletter_opened=true; _uetsid=265920f0c58c11ed819d45c05d118dca; _uetvid=26595a20c58c11edb40bb9907b677233",
        "referer": "https://www.decathlontravel.com/voyages/sport-randonnee-trekking",
        "sec-ch-ua": "^\^Chromium^^;v=^\^110^^, ^\^Not",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "^\^Windows^^",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    #print(response.text)

    # BeautifulSoup to parse HTML results from the response
    soup = BeautifulSoup(response.text, 'lxml')

    for item in soup.find_all('article', attrs= {'class': 'result travel-search-engine-result'}):
        try:
            name = item.find("h2", "heading").text.strip()
            destination= item.find("div", "destination").text.strip()
            URL= item.find("h2", "heading").find("a").attrs["href"]
            travel_image= item.find("img").attrs["src"]
            duration= item.find("li", "feature is-duration").find("span", "value").text.strip()
            price= item.find("div", "minprice").find("strong")
            #difficulty_level : item.find("li", "feature is-level").find("span", "value").text
            activity= item.find("li", "feature is-theme").find("span", "value").text
            travel_type= item.find("li", "feature is-group").find("span", "value").text
        
        # In case the information is missing:
        except Exception as e:
            activity_type = None
        
        # Append the results in the corresponding lists
        name_list.append(name)
        destination_list.append(destination)
        URL_list.append(URL)
        travel_image_list.append(travel_image)
        duration_list.append(duration)
        price_list.append(price)
        #difficulty_level_list.append(difficulty_level)
        activity_list.append(activity)
        travel_type_list.append(travel_type)

#print(travel_name_list, destination_list)

# Create a dictionary from lists
dict = {'name': name_list,
        'destination': destination_list, 
        'URL': URL_list,
        'travel_image': travel_image_list,
        'duration': duration_list,
        'price': price_list,
        #'difficulty_level': difficulty_level_list,
        'activity': activity_list,
        'travel_type': travel_type_list
}

# Create a Pandas dataframe from the dictionary and then export the results to csv format
decathlon_travel_df = pd.DataFrame(dict)
decathlon_travel_df.to_csv("decathlon_travel.csv", sep = ';', encoding='utf-8')

