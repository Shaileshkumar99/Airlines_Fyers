s = input().split()
lst = []

for i in s:
    i = i.lower()
    i = i[:: -1]
    i = i.capitalize()
    lst.append(i)

str1 = " "

print(str1.join(lst))
