import requests
from urllib.request import urlretrieve

apiKey = 'DEMO_KEY'

def getPic():
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  date = '2020-01-22'
  params = {
      'api_key': apiKey,
      'date': date,
      'hd': 'True'
  }
  response = requests.get(URL_APOD, params=params).json()
  print(response)


getPic()
