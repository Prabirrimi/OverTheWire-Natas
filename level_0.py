import requests
import re

usernmae = "natas0"
password = "natas0"

url = "http://%s.natas.labs.overthewire.org" %usernmae

respons = requests.get(url, auth = (usernmae, password))
content = (respons.text)

flag = re.findall("<!--The password for natas1 is (.*) -->", content)[0]
print(flag)
