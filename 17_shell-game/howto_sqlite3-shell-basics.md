## QR Code Generators: Julia Lee, William V, Jeffrey Zou

### DISCO:

sqlite3 [database name]
- No database name will make a temp database.

create table [name](colName type, colName type)  
insert into [name] values(val, val)

select * from [name]  
select * from [name] where [condition]

.open [database]  
* You can put the database location to specify
.save [database]  

.mode [mode]  
- Changes the way the table is displayed
.separator [separator]  

.output [file]  
- Changes output for whole session
.once [file]  
- Outputs to this file only for this command

- You should change the mode before outputting to a file.
'''
.import --csv --skip 1 --schema temp C:/work/somedata.csv tab1
'''
imports a csv file, skips the first line because the tab1 already has colNames.
