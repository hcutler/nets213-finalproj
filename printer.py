import csv

with open('countries.csv') as data:
	reader = csv.reader(data)
	for row in reader:
		if not row[2]:
			row[2] = 0
		print "['{}',{},{}],".format(row[0], row[1], row[2])