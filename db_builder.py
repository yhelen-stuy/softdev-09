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

def read_csv(filename):
    return csv.DictReader(filename)

courses = read_csv('courses.csv')
peeps = read_csv('peeps.csv')

def create_table(table_name, columns):
    return "CREATE TABLE " + table_name + " (" + columns + ")"

def insert_data(csv_dict, table_name):
    return

c.execute(create_table('courses', 'code TEXT, mark INTEGER, id INTEGER'))
c.execute(create_table('peeps', 'name TEXT, age INTEGER, id INTEGER'))

#==========================================================
db.commit() #save changes
db.close()  #close database


