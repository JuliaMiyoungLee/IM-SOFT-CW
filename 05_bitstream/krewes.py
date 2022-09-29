'''
Julia Lee
SoftDev
K05 -- bitstream
2022-09-29
time spent:
DISCO:
QCC:

'''
krewes = {}
file = open("krewes.txt", "r")
string = file.read()
alls = string.split("@@@")
for person in alls:
    tempList = person.split("$$$")
    if tempList[0] not in list(krewes.keys()):
        krewes[int(tempList[0])] = [tempList[1:]]
    else:
        krewes[int(tempList[0])].append(tempList[1:])
    print(tempList)
print(krewes)