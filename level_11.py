import requests
import re

username = "natas11"
password = "U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK"

url = "http://natas11.natas.labs.overthewire.org/"

session = requests.session()

cookies = { "data":"ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK"}
response = session.post(url, auth=(username, password), cookies=cookies)
content = (response.text)

flag = re.findall("The password for natas12 is (.*)<br>", content)[0]
print(flag)