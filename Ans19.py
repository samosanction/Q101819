from operator import itemgetter

li = []
while True:
    user_input = input('Input details here: ')
    if not user_input:
        break
    li.append(user_input.split(","))
print(sorted(li, key=itemgetter (0,1,2)))
