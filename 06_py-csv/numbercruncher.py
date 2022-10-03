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
round(number, number of decimal places to round to)
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
    temp = job[::-1].split(",",1) #Reverses the string and then splits the string on the first comma
    counter = round(counter + float(temp[0][::-1]), 1)
    jobs[counter] = temp[1][::-1].strip('"')

def getJob(data): #Takes in a dictionary and returns a random job from it
    rand = round(random.uniform(0, 99.8), .1)
    print("random number: " + str(rand) + "\n")
    for key in list(jobs.keys()):
        if key >= rand:
            return jobs[key]

print(jobs)
