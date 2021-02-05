import csv
file = open('new.csv')
reader = csv.DictReader(file)
print('name\t\tage\t\tsalary')
for i in reader:
    print(f'{i["name"]}\t{i["age"]}\t\t{i["salary"]}')
file.close()
