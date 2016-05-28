import csv

infile = 'input_partslist.txt'

with open(infile) as f:
    lines = f.read().splitlines()
    c = []
    u = []
    t = []
    out = []
    for line in lines:
	    part = ','.join(line.split())
	    part = part.split(',')
	    partall = [part[1],part[2]]
	    t.append(partall)
    for i in t:
    	if i not in u:
    		u.append(i)
    		n = t.count(i)
    		o = i
    		cou = t.count(i)
    		couval = [i, cou]
    		c.append(couval)
f.close()
with open("tel_v_03_outlist.csv", "wb+") as s:
	for x in c:
		oline = ",".join([x[0][0],x[0][1],str(x[1])])
		s.write(bytes(oline, 'UTF-8'))
		s.write(bytes('\n', 'UTF-8'))

s.close()



