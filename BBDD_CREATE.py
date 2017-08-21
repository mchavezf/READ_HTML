
import sqlite3
con=sqlite3.connect("AIRBNB")
cursor=con.cursor()

sql="create table ROOM (ID_ROOM INT PRYMARY KEY)"
cursor.execute(sql)

sql="create table RESERVA (ID_ROOM INT NOT NULL,FECHA_RESERVADA DATE NOT NULL,FECHA_RESERVACION DATE,primary key(ID_ROOM,FECHA_RESERVADA) )"
cursor.execute(sql)

con.close()
