import http.client

conn = http.client.HTTPSConnection("wordsapiv1.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "SIGN-UP-FOR-KEY",
    'X-RapidAPI-Host': "wordsapiv1.p.rapidapi.com"
    }

conn.request("GET", "/words/hatchback/typeOf", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))