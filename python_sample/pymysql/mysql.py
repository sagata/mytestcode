
#coding:utf-8
import MySQLdb
conn=MySQLdb.connect(host="192.168.40.195",user="root",passwd="163a163@",db="mhcalendar",charset="utf8")    
cursor = conn.cursor()
n = cursor.execute("select * from session") 
print n     
for row in cursor.fetchall():      
    print row  
    print row[1].encode('utf-8')





conn=MySQLdb.connect(host="192.168.40.111",user="root",passwd="163a163@",db="popo_robot",charset="utf8")    
cursor = conn.cursor()
n = cursor.execute("select * from custom_serial where serial = 2711") 
print n     
for row in cursor.fetchall():      
    print row  
    print row[3].encode('utf-8')



#############插入的试验
conn=MySQLdb.connect(host="192.168.40.195",user="root",passwd="163a163@",db="resshow",charset="utf8")    
cur = conn.cursor()

#创建数据表
#cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")

#插入一条数据
cur.execute("insert into tuxiang_table(jinyi_id,ilast,cadd) values(111,11,'22')")
cur.execute("insert into tuxiang_table(jinyi_id,ilast,cadd) values(333,11,'22')")

#修改查询条件的数据
#cur.execute("update student set class='3 year 1 class' where name = 'Tom'")

#删除查询条件的数据
#cur.execute("delete from student where age='9'")

cur.close()
conn.commit()
conn.close()


