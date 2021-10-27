import csv

with open(r'C:\\projects\\data_wrangling\\affiliations.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter = ",")
    next(reader)
    for row in reader:
        row = row[0].split(',')
        # print(row[len(row)-1])
        countries = []
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
        #print(countries[0][len(countries[0])-1])
        with open(r'C:\\projects\\data_wrangling\\usa_states.csv', 'r', errors='ignore') as f:
            reader2 = csv.reader(f)
            next(reader2)
            data = list(reader2)
            #print(data[1][0])
            #print(countries[0])
            i = 0
            while i < len(data):
                if countries[0] == data[i][0]:
                    countries = [countries[0].replace(countries[0], 'United States') for countries[0] in countries]
                elif countries[0] == data[i][1]:
                    countries = [countries[0].replace(countries[0], 'United States') for countries[0] in countries]
                elif countries[0][len(countries[0])-1].isnumeric() == True:
                    countries = [countries[0].replace(countries[0], 'Canada') for countries[0] in countries]
                elif len(countries) >= 2 and countries[len(countries)-1][0] == 'U':
                    countries.remove(countries[0])
                if countries[0][0] == 'U' and countries[0][1] == '.':
                    if countries[0][2] == 'S':
                        countries = [countries[0].replace(countries[0], 'United States') for countries[0] in countries]
                    elif countries[0][2] == 'K':
                        countries = [countries[0].replace(countries[0], 'United Kingdom') for countries[0] in countries]
                elif countries[0][1] == 'S':
                    countries = [countries[0].replace(countries[0], 'United States') for countries[0] in countries]
                elif countries[0][1] == 'K':
                    countries = [countries[0].replace(countries[0], 'United Kingdom') for countries[0] in countries]
                i += 1
            print(countries)
        f.close() 
file.close()



