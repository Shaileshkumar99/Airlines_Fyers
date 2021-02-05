import csv
file = open('new.csv','w')
head = ['name','age','salary']
writer = csv.DictWriter(file,fieldnames=head)
writer.writeheader()
for x in range(2):
    name=input('enter name')
    age = input('enter age')
    salary = input('enter salary')
    writer.writerow({'name':name,'age':age,'salary':salary})
file.close()
