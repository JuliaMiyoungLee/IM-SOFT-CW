#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2022

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >

# c.execute(".mode csv")
''' You aren't able to change the mode with c.execute because c.execute is running commands with the database open in relation to a sepcific table. If you think about sqlite in the
terminal, the mode is always changed outside of having the table open and it's meant to change how the table is stored. Thus, it's not actually runnable code in the same area that
the create table or insert into commands are.
'''

def createTable(csvFile): #Takes in a csv file and creates a table based on the csv file you're reading data from.
    with open(csvFile, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        name = csvFile[:-4] #creates table name based on csv file name.
        command = "create table " + name + "(" + reader.fieldnames[0] + " text, " + reader.fieldnames[1] + " int, " + reader.fieldnames[2] + " int);" #plugs in fieldnames from reader. The first line of the csv file wil always be the list of fieldnames unless otherwise specified.
        c.execute(command)    # run SQL statement
        for row in reader: # you could also run the command only once by utilizing executescript and simply creating a longer string with all the relevant commands you want.
            command = "insert into " + name + " values('" + row[reader.fieldnames[0]] + "', " + row[reader.fieldnames[1]] + ", " + row[reader.fieldnames[2]] + ");"
            c.execute(command)

createTable('students.csv') #creates student table in db
createTable('courses.csv') #creates courses table in db
#==========================================================

db.commit() #save changes
db.close()  #close database
