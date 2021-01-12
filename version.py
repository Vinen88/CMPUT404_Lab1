import requests
r = requests.get('https://raw.githubusercontent.com/Vinen88/CMPUT404_Lab1/main/version.py')
print(r.text)
print("Requests version:",requests.__version__)