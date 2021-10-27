import csv

with open(r'C:\\projects\\data_wrangling\\affiliations.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter = ",")
    next(reader)
    for row in reader:
        row = row[0].split(',')
        # print(row[len(row)-1])
        countries = []
        #if row[0]
        countries.append(row[len(row)-1])
        #print(type(countries[0]))
        #print(countries[0])
        countries = countries[0].split()
        #print(countries[0])
        if countries[0].isnumeric() == True or '-' in countries[0]:
            countries.remove(countries[0])
        elif len(countries) > 1 and countries[len(countries)-2].isnumeric() == True:
            countries.remove(countries[len(countries)-2])
        elif len(countries) > 2:
            countries.remove(countries[0])
            countries.remove(countries[0])
        elif len(countries) == 2:
            countries.remove(countries[0])
        print(countries)
    file.close()
