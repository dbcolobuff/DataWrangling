import csv
# The only thing you need to change is the file path to wherever you keep the CSVs in your files for every open statement
with open(r'C:\\projects\\data_wrangling\\affiliations.csv', 'r', errors='ignore') as file:
    reader = csv.reader(file, delimiter = ",")
    next(reader)
    for row in reader:
        row = row[0].split(',')
        # This is where the list is made initially containing the info that proceeds the last comma of each row in affiliations.csv
        countries = []
        countries.append(row[len(row)-1])
        countries = countries[0].split()
        # This is where I check for postcodes and delete them
        if countries[0].isnumeric() == True or '-' in countries[0]:
            countries.remove(countries[0])
        elif len(countries) > 1 and countries[len(countries)-2].isnumeric() == True:
            countries.remove(countries[len(countries)-2])
        elif len(countries) > 2:
            countries.remove(countries[0])
            countries.remove(countries[0])
        elif len(countries) == 2:
            countries.remove(countries[0]) 
        with open(r'C:\\projects\\data_wrangling\\usa_states.csv', 'r', errors='ignore') as f:
            reader2 = csv.reader(f)
            next(reader2)
            data = list(reader2)
            # This is where I make all American  and British (and Canadian for special circumstances) all the same name (United States and United Kingdom)
            # For the USA this is where I took state names and acronyms and made them 'United States'
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
                elif countries[0][0] == 'U' and countries[0][1] == 'S':
                    countries = [countries[0].replace(countries[0], 'United States') for countries[0] in countries]
                elif countries[0][0] == 'U' and countries[0][1] == 'K':
                    countries = [countries[0].replace(countries[0], 'United Kingdom') for countries[0] in countries]
                i += 1
            with open(r'C:\\projects\\data_wrangling\\unique_countries.csv', 'r', errors='ignore') as fl:
                reader3 = csv.reader(fl)
                next(reader3)
                info = list(reader3)
                # This is where I check to see if the final list of countries matches the unique_countries.csv and should put a check mark next to the ones that do
                j = 0
                while j < len(info):
                    if countries[len(countries)-1] == 'Africa':
                        countries = [countries[0].replace(countries[0], 'South Africa') for countries[0] in countries]
                    if countries[len(countries)-1] == 'Zealand':
                        countries = [countries[0].replace(countries[0], 'New Zealand') for countries[0] in countries]
                    if countries[len(countries)-1] == 'Republic':
                        countries = [countries[0].replace(countries[0], 'Czech Republic') for countries[0] in countries]
                    if countries[len(countries)-1] == 'Rico':
                        countries = [countries[0].replace(countries[0], 'Puerto Rico') for countries[0] in countries]
                    if countries[len(countries)-1] == info[j][0]:
                        countries = [countries[0].replace(countries[0], info[j][0] + u'\u2713') for countries[0] in countries]
                    j += 1  
                print(countries[0])
            fl.close()
        f.close() 
file.close()



