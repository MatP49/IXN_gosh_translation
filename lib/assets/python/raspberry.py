#!/usr/bin/env python3

from urllib.request import urlopen
import re

html = urlopen("http://babelraspberry.ddns.net/")

a1 = html.read().decode('utf-8')
a2 = a1


result1 = re.search('<h1>(.*)</h1>', a1)
result2 = re.search('<p>(.*)</p>', a2)


print(result1.group(1))
print(result2.group(1))
