# Nam Doan
# 1847037

import csv

input1 = input()

with open(input1, 'r') as textsfile:
    texts_reader = csv.reader(textsfile)
    for row in texts_reader:
        list_of_words = row

no_duplicates = list(dict.fromkeys(list_of_words))
listlength = len(no_duplicates)

for i in range(listlength):
    print(no_duplicates[i], list_of_words.count(no_duplicates[i]))
