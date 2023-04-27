import re

password = input('Input password: ').split(",")
count = 0
li = []
for items in password:
    count += bool(re.search("\d", items))
    count += bool(re.search("\w", items))
    count += bool(re.search("\W", items))
    count += bool(re.search("\w", items))
    count += bool(len(items) > 6 and len(items) < 12)
    if count == 5:
        li.append(items)
print(",".join(li))









