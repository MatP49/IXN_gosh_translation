#!/usr/bin/env python3

from urllib.request import urlopen
import re

html = urlopen("http://babelraspberry.ddns.net/")

scraping = html.read().decode('utf-8')

result = re.search('<h1>(.*)</h1>', scraping)

print(result.group(1))

