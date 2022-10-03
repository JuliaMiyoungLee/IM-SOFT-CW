'''
RANDO: Julia Lee, Fang Chen
Soft Dev, Pd 2
K06 -- Divine your Destiny!
2022-10-02
Time Spent:

DISCO:
After setting a variable in the file to a value, calling a defined function (which changes the value of the variable of the same name)
    does not overwrite the value of said variable set outside the function. (Only tested with ints)
    Example:
        x = 1
        def change():
            x = 2
        change()
        print(x)    # Output = 1

Utilizing strip() helps to get rid of unwanted newlines
There is a built in csv library
 QCC:
    How can we update the value of an initialized variable by calling a function?
    Maybe we would have to set x = function call.
    Is there a way to ignore commas within "" built into the split function? I couldn't find any, but it seems like it would be useful...

HOW THIS SCRIPT WORKS:

'''
import random

jobs = {}
file = open("occupations.csv").read().strip()
listOfJobs = file.split("\n") #List of each "occupation",%
counter = 0.0 #Keeps track of rollover percentages

for job in listOfJobs:
    temp = job[::-1].split(",",1)
    counter = counter + float(temp[0][::-1])
    print(counter)
#     counter = counter + float(temp[-1])
#     jobstr = ""
#     for i in range(0, len(temp) - 1):
#         jobstr += temp[i]
#     jobs[counter] = jobstr
#
# print(jobs)
