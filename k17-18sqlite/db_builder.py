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

c.execute(".mode csv")

# def createTable(csvFile):
#     with open(csvFile, newline='\n') as csvfile:
#         reader = csv.DictReader(csvfile)
#         name = csvFile[:-4]
#         command = "create table " + name + "(" + reader.fieldnames[0] + " text, " + reader.fieldnames[1] + " int, " + reader.fieldnames[2] + " int);"
#         c.execute(command)    # run SQL statement
#         for row in reader:
#             command = "insert into " + name + " values('" + row[reader.fieldnames[0]] + "', " + row[reader.fieldnames[1]] + ", " + row[reader.fieldnames[2]] + ");"
#             c.execute(command)
#
# createTable('students.csv')
# createTable('courses.csv')
#==========================================================

db.commit() #save changes
db.close()  #close database
