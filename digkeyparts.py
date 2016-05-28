from bs4 import BeautifulSoup
import urllib
import re
import xml
import requests
from urllib import parse
import json

filename = "dkcost.json"
infile = "input_partslist.csv"

urls = []

with open(infile) as f:
    lines = f.read().splitlines()
    for line in lines:
        l = line.split(',')
        addlist = [l[3],l[2]]
        urls.append(addlist)
    f.close()


jsonlib = {}

for item in urls:
    url = item[0]
    url = url.strip()
    print (url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    organic = soup.find("table", {"id": "product-dollars"})
    idnum = soup.find('td', {"id": "reportPartNumber"})
    idnum = idnum.text.strip()
    desc = soup.find('td', {"itemprop": "description"})
    manpartno = soup.find('h1', {"itemprop": "model"})

    rows = organic.find_all("tr") #, {"class": "info"})

    vals = []
    datalib = {}
    prices = {}
    datalib['DKnumber'] = idnum
    datalib['quantity'] = item[1]
    datalib['description'] = desc.text.strip()
    datalib['ManPartNo'] = manpartno.text.strip()
    datalib['URL'] = url
    for row in rows:
        col = row.find_all('td')
        for ind in col:
            vals.append(ind.text)
    i = 0
    while i < len(vals):
        prices[str(vals[i])] = str(vals[i+1])
        i = i + 3
    datalib['Prices'] = prices

    jsonlib[idnum] = datalib

jsondict = {"PartsList": jsonlib}
json_data = json.dumps(jsondict)
print (json_data)
with open(filename, "a") as myfile:
    myfile.write(json_data)
    myfile.close()
