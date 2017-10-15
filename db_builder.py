'''
Helen Ye
SoftDev1 pd7
HW09 -- No Treble
2017-10-13
'''
import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def create_table(table_name, columns):
    return "CREATE TABLE " + table_name + " (" + columns + ")"

def insert_data(csvfile, table_name):
    f = open(csvfile, 'rU')
    reader = csv.DictReader(f)
    for row in reader:
        comm = "INSERT INTO " + table_name + ' VALUES ('
        for field in row:
            comm += '"' + row[field] + '",'
        comm = comm[0:-1]
        comm += ")"
        c.execute(comm)
    f.close()

c.execute(create_table('courses', 'code TEXT, mark INTEGER, id INTEGER'))
c.execute(create_table('peeps', 'name TEXT, age INTEGER, id INTEGER'))
insert_data('courses.csv', 'courses')
insert_data('peeps.csv', 'peeps')

#==========================================================
db.commit() #save changes
db.close()  #close database
