import re
import ply.lex as lex 
import sys
import requests
import urllib.request, urllib.error, urllib.parse

string = 'https://www.worldometers.info/coronavirus/'

lines = []
with open('worldometers_countrylist.txt') as f:
    lines = f.readlines()

count = len(lines)
ans = []
indicator = 0
for i in range(2, count):
    if lines[i].isspace():
        indicator = 2
    elif indicator == 1 or indicator == 2:
        indicator -= 1
    else:
        ans.append(lines[i].strip().replace(" ", "-"))

idx = 0
links = []
for ns in ans:
    idx += 1
    strp = string + 'country/' + ns + '/'
    strcnt = ns + '.html'
    r = requests.get(strp, allow_redirects=True)
    f = open(strcnt, 'wb').write(r.content)