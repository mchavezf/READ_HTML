import urllib2,json,datetime,time
from Correo import Correo
from BBDD import f_ireserva2
from BBDD import f_sidroom



def f_leerfecha(id):
    url_base="https://www.airbnb.cl/api/v2/calendar_months?key=d306zoyjsyarp7ifhu67rjxn52tv0t20&count=12"
    hoy=datetime.date.today()
    url_fecha="&year=%s&month=%s"%(hoy.year,hoy.month)
    url_id="&listing_id="+str(id)
    url=url_base+url_id+url_fecha
    headers = { 'User-Agent' : 'Mozilla/5.0' }
    req = urllib2.Request(url, None, headers)
    try:
        html=urllib2.urlopen(req).read()
        data = json.loads(html)
        for m in data["calendar_months"]:
            for i in m["days"]:
                dia=datetime.datetime.strptime(i["date"],'%Y-%m-%d').date()
                dia_nyear=dia+datetime.timedelta(days=365)
                if i["available"]==False and dia>=hoy  and dia_nyear<=hoy:
                    f_ireserva2(id,dia["date"],hoy.strftime('%Y-%m-%d'))
    except:
        print str(id)
        #cursor_mysql.execute('INSERT INTO RESERVA VALUES ('+str(id)+",'"+str(i["date"])+"','"+datetime.date.today().strftime("%Y-%m-%d")+"')")
        #connexion.commit()



ROOMS=f_sidroom()
inicio=time.time()
for i in ROOMS:
    f_leerfecha(i)

Correo("Ejecutado Correctamente. Tiempo de Ejecucion:"+str(time.time()-inicio))
