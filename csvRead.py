
import csv

class csvRead:
         filename = "/Users/Mubarak/Documents/temp/pyml/filereading/xas.csv"
         fields=[]
         rows=[]
         with open(filename,"r") as file:
            csvreader=csv.reader(file)

            fields=csvreader.next()
            for row in csvreader:
                rows.append(row)

            s="  ".join(field for field in fields)

            print s

            for col in rows:
                print("%10s"%col)









