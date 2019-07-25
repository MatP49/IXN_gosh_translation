#!/usr/bin/env python3

from urllib.request import urlopen
import re
from Crypto.Cipher import AES
import base64

html = urlopen("http://babelraspberry.ddns.net/")

scraping = html.read().decode('utf-8')

result = re.search('<p>(.*)</p>', scraping)


key = 'ASSWJDWHJ9748hJSJWK8983jJKJS990S'
data = result.group(1)
cipher = AES.new(key,AES.MODE_ECB)
decoded = cipher.decrypt(base64.b64decode(data))
decoded = decoded.decode("utf-8") 

print(decoded.strip())