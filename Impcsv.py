import csv
with open('new.csv') as csvfile:
    data= csv.reader(csvfile)
    for row in data:
        print(", ".join(row))
