import sqlite3
connection=sqlite3.connect('D:/New folder/sql/addressbook.db')
print('database openned successfully')
connection.execute("create table contactdetails(id integer primarykey autoincrementt,name varchar not null,email text unique not null,address text not null)")
print('table created successffully')
connection.close()