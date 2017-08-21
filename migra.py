import MySQLdb
from BBDD import f_iidroom
from BBDD import f_ireserva
import multiprocessing as mp

DB_HOST = 'localhost'
DB_USER = 'python'
DB_PASS = 'asas'
DB_NAME = 'AIRBNB'

datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
mysql_conn = MySQLdb.connect(*datos) # Conectar a la base de datos
mycursor = mysql_conn.cursor()

def migra_room():
    mycursor.execute("SELECT  ID_ROOMS FROM AIRBNB.ROOMS ")
    ROOMS=mycursor.fetchall()
    ROOMS=[x[0] for x in ROOMS]
    map(f_iidroom,ROOMS)
#migra_room()

def migra_reserva():
    mycursor.execute("SELECT * FROM AIRBNB.RESERVA")
    data = mycursor.fetchall()
    pool = mp.Pool(4)
    pool.map(f_ireserva,data)
migra_reserva()
