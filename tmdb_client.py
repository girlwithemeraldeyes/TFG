import requests 
import json

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = "a9c62b96ad835e5416068309082bbec9"

top_rated = "/movie/top_rated"
index = 1


list = []
for index in range(1,500):
    url = f"{BASE_URL}movie/top_rated?api_key={API_KEY}&language=es-ES&page={index}"
    print (url)

    response = requests.get(url)
    data = response.json()
    list.append(data)

    print(response)
    print(data)

with open("ratings.json","w") as archivo:
    json.dump(list, archivo, indent=4)








