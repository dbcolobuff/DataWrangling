import csv
with open(r'C:\\projects\\data_wrangling\\affiliations.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        print(row)