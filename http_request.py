# Sending an HTTP GET Request
import requests
url = "https://en.wikipedia.org/wiki/Napoleon"
response = requests.get(url)
#Print the response content
print(response.text)