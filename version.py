import requests
r = requests.get('http://www.google.com/')
print(r.text)
print("Requests version:",requests.__version__)