'''
Julia Lee
SoftDev
K05 -- bitstream
2022-09-29
time spent:
1 class period + 5 minutes outside of class for debugging
DISCO:
list.append()
dictionary[key] = value

QCC:
I remember being told to close files after reading them, but I don't really remember or understand why that's important.
Is there a way to split along various characters at once? For example, to split on the condition of there being $$$ or @@@?
What exactly is the function of "open". 
'''
krewes = {}
file = open("krewes.txt", "r")
string = file.read()
alls = string.split("@@@")
for person in alls:
    tempList = person.split("$$$")
    if int(tempList[0]) not in list(krewes.keys()):
        krewes[int(tempList[0])] = [tempList[1:]]
    else:
        krewes[int(tempList[0])].append(tempList[1:])
print(krewes)