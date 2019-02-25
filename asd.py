import csv


filename = "/Users/Mubarak/Documents/temp/pyml/filereading/xas.csv"


fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)


    fields = csvreader.next()


    for row in csvreader:
        rows.append(row)


    print("Total no. of rows: %d" % (csvreader.line_num))


print("          "+', '.join(field for field in fields))



for row in rows:
    for col in row:
        print("%10s" % col),
    print('\n')