sentence = input('write your sencence here: '). split(" ")
my_sort = sorted(set(sentence))
print(" ".join(my_sort))