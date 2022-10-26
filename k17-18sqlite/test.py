import csv

with open('students.csv', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    print(reader.fieldnames[0])
    # for a in reader:
    #     print(a['name'], a['age'], a['id'])