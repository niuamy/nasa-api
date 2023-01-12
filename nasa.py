import requests
from urllib.request import urlretrieve

apiKey = 'DEMO_KEY'

def chooseDate():
    date = input("Enter the date you would like an image from in YYYY-MM-DD format: ")
    return date


def getPic(date):
  url = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key': apiKey,
      'date': date
  }
  response = requests.get(url, params=params).json()
  print(response)


def main():
    date = chooseDate()
    getPic(date)


if __name__ == "__main__":
    main()
