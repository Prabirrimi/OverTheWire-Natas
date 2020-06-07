import requests
import re

username = "natas8"
password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

url = "http://natas8.natas.labs.overthewire.org/"

session = requests.session()

respones = session.post(url, data={"secret" : "oubWYf2kBq", "submit" : "submit"}, auth=(username, password))
content = (respones.text)

flag = re.findall("The password for natas9 is (.*)", content)[0]
print(flag)