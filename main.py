import csv


### CSV reader ###

with open('pcbanking.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

print(csv_reader)
