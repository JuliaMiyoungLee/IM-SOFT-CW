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
There is a built in csv module.
round(number, number of decimal places to round to)
string[::-1] will splice the string backwards. It starts from the back of the string and moved forward by -1, going backwards.
random.uniform(start, end) returns a float inclusive of both parameters.

 QCC:
    How can we update the value of an initialized variable by calling a function?
    Maybe we would have to set x = function call.
    Is there a way to ignore commas within "" built into the split function? I couldn't find any, but it seems like it would be useful...

HOW THIS SCRIPT WORKS:
    00. Converts data from csv file to a dictionary by splitting on newlines and commas(frmom the back).
    01. Selects a random float from 0 to 99.8 using random.uniform()
    02. Return the value given when the percentage(key) of the dictionary value is greater than or equal to the random value.
'''
import random

jobs = {}
file = open("occupations.csv").read().strip()
listOfJobs = file.split("\n") #List of each "occupation",%
counter = 0.0 #Keeps track of rollover percentages

for job in listOfJobs:
    temp = job[::-1].split(",",1) #Reverses the string and then splits the string on the first comma
    counter = round(counter + float(temp[0][::-1]), 1) #rollover the percentages
    jobs[counter] = temp[1][::-1].strip('"') #set job at given percent(counter) value

def getJob(data): #Takes in a dictionary and returns a random job from it
    rand = round(random.uniform(0, 99.8), 1) #Generates a random value from 0 to 99.8
    for key in list(jobs.keys()): #Goes through the list of jobs %s
        if key >= rand: #returns the job once the job % is >= the generated random value
            return jobs[key]

#Testing
jobTest = {}
numOfTests = 10000

for job in jobs.values(): #Creates a dictionary of jobs
    jobTest[job] = 0

for trial in range(numOfTests): #Keeps track of how many times each job has been selected
    jobTest[getJob(jobs)] += 1

for job in list(jobTest.keys()): #Finds the percentages at which each job was selected
    jobTest[job] = round(float(jobTest[job]*100 / numOfTests), 1)

print(listOfJobs)
print(jobTest)
