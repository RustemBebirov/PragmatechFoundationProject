import sqlite3

con = sqlite3.connect("homework.db")

cursor = con.cursor()

# Create table
# cursor.execute("Create table if not exists users(ID INTEGER PRIMARY KEY AUTOINCREMENT,NAME TEXT NOT NULL,SALARY INT NOT NULL)")

#Insert table
# cursor.execute("Insert into users (Name,SALARY) values('eli',450) ")

#Update table
# cursor.execute("Update users set Name ='orxan' where id = 5")

# cursor.execute("Select * from users")

# cursor.execute("Select id,name from users")

# cursor.execute("Select * from users where salary > 500")

users=cursor.fetchall()

for i in users:
    print(i)

cursor.execute("Delete from users where name = 'subhan' ")

con.commit()

con.close()