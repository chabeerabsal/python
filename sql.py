import sqlite3
connection=sqlite3.connect("D:/New folder/sql/python with sql.db")
cursor=connection.cursor()
try:
    sql_command='''create table student(
                roll no integer,
                sname varchar(20),
                grade char(1),
                gender char(1),
                average decimal(5,2),
                birthdate date);
              '''
    cursor.execute(sql_command)
    sql_command='''insert into student values(
                101,"chabeer","A","M",
                "95.5","30-10-2001");
                '''
    cursor.execute(sql_command)
    connection.commit()
    print("student table created")
except:
    connection.rollback()
    print('problem occurs')



























