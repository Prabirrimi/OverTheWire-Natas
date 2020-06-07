import requests
import re

username = "natas6"
password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

url = "http://natas6.natas.labs.overthewire.org"

session = requests.session()

respones = session.post(url, data={"secret" : "FOEIUWGHFEEUHOFUOIU", "submit" : "submit"}, auth=(username, password))
content = (respones.text)

flag = re.findall("The password for natas7 is (.*)", content)[0]
print(flag)