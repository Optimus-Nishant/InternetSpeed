from datetime import datetime
import time
import requests
import csv
time_prev = 0
f = open('results.csv','wb')
writer = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)
url = "http://testmy.net/SmarTest/down"
while True:
	if (time.time() - time_prev) > 60:
		time_prev = time.time()
		l = []
		l=l+str(datetime.now()).split(' ')
		print "Downloading Started......."
		t1 = time.time()
		try:
			r = requests.get(url)	
			t2 = time.time()
			l.append(t2 - t1)	
		except :
			continue
		print "Downloaded 5 MB in %s seconds"%(t2-t1)
		print l
		writer.writerow(l)
