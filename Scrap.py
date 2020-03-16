import urllib.request
import urllib.parse
import re

url = "https://patient.info/forums/index-a"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
resp = urllib.request.urlopen(req)

respData = resp.read()

print(respData)