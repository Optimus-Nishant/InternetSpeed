from matplotlib import pyplot as plt
import datetime
import csv
f = open('results.csv','rb')
reader = csv.reader(f,delimiter=' ', quotechar='|')
ts = []
val = []

for row in reader:
	ts.append(row[0]+' '+row[1])
	val.append(row[2])

for i in range(len(val)):

	val[i] = (5)/float(val[i])

print val

for i in range(len(ts)):
	ts[i] = datetime.datetime.strptime(ts[i], "%Y-%m-%d %H:%M:%S.%f")
plt.plot(ts,val,lw=0.5,color="blue")
plt.gca().set_ylim([0,10])
plt.gcf().autofmt_xdate()
plt.fill_between(ts,0,val,facecolor='blue', alpha=1.6)
plt.show()
