import sqlite3
import os
cx = sqlite3.connect("test.db")
count = 0

def tt():
	print 'tes'
	global count
	count += 1

'''
CREATE TABLE Persons
(
Id_P int,
one varchar(255),
FirstName varchar(255),
Address varchar(255),
City varchar(255)
)
'''

#cx.execute("CREATE TABLE Persons(one varchar(255),two varchar(255))")


#cx.execute("insert into  Persons values('test','test2')")
#cx.commit()


'''
cx.execute("UPDATE Persons set one = '25000.00' where two='test2'")
cx.commit()
'''

cursor = cx.execute("select * from Persons") 
for row in cursor:
	print row[0],row[1] 


db_path = r"D:\Regress\3.0.141\data.db"
if os.path.exists(db_path):
	print 'yes###'


test = [11,23,'33',23]
test.append('asf')
print test
tt()
tt()
print count


print "%s"%('test')
print "His name is %s"%("Aviad")

OUTPUT_ROOT_DIR = r"D:\Regress\3.0.141\data.db"
testdb = sqlite3.connect(OUTPUT_ROOT_DIR)
cursor = testdb.execute("select * from Regressdata") 
for row in cursor:
	print row[0],row[1] 















