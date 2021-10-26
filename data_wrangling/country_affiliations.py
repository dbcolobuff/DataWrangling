import csv

with open(r'C:\\projects\\data_wrangling\\affiliations.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter = ",")
    next(reader)
    for row in reader:
        country = row[0].split(',')
        print(country[len(country)-1])
file.close


