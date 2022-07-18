import re

#https://leetcode.com/problems/valid-phone-numbers/
def checkphone(file):
    f = open(f'{file}','r')
    f1 = f.readlines()
    valids = []
    ex1 = re.compile("^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$")
    for i in f1:
        if ex1.match(i):
            valids.append(i)
    return valids
print(checkphone('file.txt'))

############  bash variant  ############
# cat file.txt | grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt