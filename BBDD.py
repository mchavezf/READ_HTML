import sqlite3

def f_ireserva(row):
    id,FECHA_RESERVADA,FECHA_RESERVACION=row[0],row[1].strftime('%Y-%m-%d'),row[2].strftime('%Y-%m-%d')
    con=sqlite3.connect("AIRBNB")
    cursor=con.cursor()
    valida="select * from RESERVA where ID_ROOM=%s and FECHA_RESERVADA=%s"%(id,FECHA_RESERVADA)
    cursor.execute(valida)
    if cursor.fetchone() is None:
        sql="insert into RESERVA values (%s,%s,%s)"%(id,FECHA_RESERVADA,FECHA_RESERVACION)
        cursor.execute(sql)
        con.commit()
    con.close()

def f_ireserva2(id,FECHA_RESERVADA,FECHA_RESERVACION):
    con=sqlite3.connect("AIRBNB")
    cursor=con.cursor()
    valida="select * from RESERVA where ID_ROOM=%s and FECHA_RESERVADA=%s"%(id,FECHA_RESERVADA)
    cursor.execute(valida)
    if cursor.fetchone() is None:
        sql="insert into RESERVA values (%s,%s,%s)"%(id,FECHA_RESERVADA,FECHA_RESERVACION)
        cursor.execute(sql)
        con.commit()
    con.close()

def f_sidroom():
    con=sqlite3.connect("AIRBNB")
    cursor=con.cursor()
    valida="select * from ROOM "
    cursor.execute(valida)
    salida=[x[0] for x in cursor.fetchall()]
    con.close()
    return salida


def f_iidroom(id):
    valida="select * from ROOM where ID_ROOM=%s"%id
    cursor.execute(valida)
    if cursor.fetchone() is None:
        sql="insert into ROOM values (%s)"%id
        cursor.execute(sql)
        con.commit()
