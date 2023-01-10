import requests
from urllib.request import urlretrieve

apiKey = 'DEMO_KEY'

def chooseDate():
    date = input("Enter the date you would like an image from in YYYY-MM-DD format: ")
    return date


def printResults(response, date):
    link = response['url']
    explanation = response['explanation']
    title = response['title']

    print(f"On {date}, NASA's astronomy photo of the day was entitled \"{title}\".")
    print(f"\nAccompanied with the photo is the explanation: \"{explanation}\"")
    print(f"\nThe image can be seen here: {link}")



def getPic(date):
  URL_APOD = "https://api.nasa.gov/planetary/apod"
  params = {
      'api_key': apiKey,
      'date': date,
      'hd': 'True'
  }
  response = requests.get(URL_APOD, params=params).json()
  printResults(response, date)


def main():
    date = chooseDate()
    getPic(date)


if __name__ == "__main__":
    main()
