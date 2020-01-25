from investigadores.models import Periodo
import datetime

def my_scheduled_job():
    dateNow = datetime.datetime.now()
    if dateNow.month <= 6:
        nombrePeriodo = str(dateNow.year)+"A: "+"ene-jun"
    else: 
        nombrePeriodo = str(dateNow.year)+"B: "+"ene-dic"
    
    print("El nombre del periodo es: "+nombrePeriodo)
    #p = Periodo(nombrePeriodo, dateNow, dateNow+6)
