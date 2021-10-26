import csv

with open('affiliations.csv', newline='') as csvfile:
    my_reader = csv.reader(csvfile, delimiter=',')
    for row in my_reader:
        print(row)  