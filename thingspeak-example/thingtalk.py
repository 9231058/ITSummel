#!/usr/bin/env python
import requests

response = requests.get('http://thingtalk.ir/channels/75/feed.json?key=4W8IN7UU92XNWKWQ')
response = response.json()
print(response['feeds'][0])
