from logging import exception

import requests
import json

keyword = input("Enter keyword: ")

# Request template: https://api.tvmaze.com/search/shows?q=girls
request = "https://api.tvmaze.com/search/shows?q=" + keyword
try:
    response = requests.get(request)
    print(response.status_code)
    if response.ok:
        ##print(json.dumps(response, indent=2))
        tv_shows = response.json()
        for tv_show in tv_shows:
            print(tv_show["show"]["name"])

except requests.exceptions.RequestException as error:
    print(error)
