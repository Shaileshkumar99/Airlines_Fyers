import csv
import json
with open('airlines.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 count = {}
 for row in data:
     count[row['Airport.Name']] = count.get(row['Airport.Name'], 0) + 1

json_object = json.dumps(count, indent = 4)
print(json_object)

maximum = max(count, key=count.get)
print(maximum,count[maximum])


minimum = min(count, key=count.get)
print(minimum,count[minimum])