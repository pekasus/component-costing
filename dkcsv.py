import csv
import json

with open('dkcost.json') as data_file:
    x = json.load(data_file)

f = csv.writer(open("dkcost.csv", "wt"))
f.writerow(["Description", "DigiKey Code", "Qty", "1", "25", "50", "100", "500", "1000"])

qtylist = [1, 25, 50, 100, 500, 1000]
for l in x["PartsList"]:
    plist = list(x["PartsList"][l]["Prices"])
    for t in range (0, len(plist)):
        plist[t] = int(plist[t].replace(',', ''))
    plist.sort()
    print(plist)
    xlist = []
    xlist.append(x["PartsList"][l]["description"].encode('ascii', 'ignore'))
    xlist.append(x["PartsList"][l]["DKnumber"])
    xlist.append(x["PartsList"][l]["quantity"])
    print (x["PartsList"][l]["DKnumber"])
    for q in qtylist:
        px = 0
        while px < (len(plist) - 1):
            if q > plist[px]:
                px += 1
            else:
                break
        pkey = plist[px]
        print (pkey)
        print (x["PartsList"][l]["Prices"][str("{:,}".format(pkey))])
        xlist.append(x["PartsList"][l]["Prices"][str("{:,}".format(pkey))])
    print (xlist)
    f.writerow(xlist)


