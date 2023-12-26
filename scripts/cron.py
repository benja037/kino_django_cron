import requests
from apps.kinoprincipal.models import Kinodb, Rekinodb, Chanchitodb, Combodb, Chao1db, Chao2db, Chao3db
from bs4 import BeautifulSoup
import datetime

def run():
    print("aaaaat")
    fetch_kino_results()

def fetch_kino_results():
    #print("HOLAAA")
    fecha_hoy = datetime.date.today()
    fecha_ayer = fecha_hoy - datetime.timedelta(days=1)
    resp = requests.get('https://chileresultados.com/kino/ultimosorteo')
    numeros = []
    texto = resp.text
    soup = BeautifulSoup(texto, "lxml")

    # Filtro a html encuentra números de los 7 sorteos principales
    soup_numeros = soup.find_all(
        "span", class_="badge rounded-pill bg-warning text-dark")
    for elemento in soup_numeros:
        numerito = elemento.get_text()
        numeros.append(int(numerito))

    # Filtro a html encuentra data de la imagen donde el titulo contiene el numero de sorteo
    soup_sorteo = soup.find_all("img", class_="img-fluid me-2")
    titulo = soup_sorteo[0].get('title')
    sorteo = int(titulo.split(" ")[1])

    resultados_kino = numeros[0:14]
    resultados_rekino = numeros[14:28]
    resultados_chanchito = numeros[28:42]
    resultados_combo = numeros[42:56]
    resultados_chao1 = numeros[56:70]
    resultados_chao2 = numeros[70:84]
    resultados_chao3 = numeros[84:98]
    print("kino")
    pasar_modelo(Kinodb, resultados_kino, sorteo, fecha_ayer)
    print("rekino")
    pasar_modelo(Rekinodb, resultados_rekino, sorteo, fecha_ayer)
    print("chanchito")
    pasar_modelo(Chanchitodb, resultados_chanchito, sorteo, fecha_ayer)
    print("combo")
    pasar_modelo(Combodb, resultados_combo, sorteo, fecha_ayer)
    print("chao1")
    pasar_modelo(Chao1db, resultados_chao1, sorteo, fecha_ayer)
    print("chao2")
    pasar_modelo(Chao2db, resultados_chao2, sorteo, fecha_ayer)
    print("chao3")
    pasar_modelo(Chao3db, resultados_chao3, sorteo, fecha_ayer)


def pasar_modelo(tipo_sorteo_db, tipo_numeros, numero_sorteo, fecha):
    number1 = tipo_numeros[0]
    number2 = tipo_numeros[1]
    number3 = tipo_numeros[2]
    number4 = tipo_numeros[3]
    number5 = tipo_numeros[4]
    number6 = tipo_numeros[5]
    number7 = tipo_numeros[6]
    number8 = tipo_numeros[7]
    number9 = tipo_numeros[8]
    number10 = tipo_numeros[9]
    number11 = tipo_numeros[10]
    number12 = tipo_numeros[11]
    number13 = tipo_numeros[12]
    number14 = tipo_numeros[13]
    tipo_ingreso = "Cron2"

    print(tipo_sorteo_db, fecha, numero_sorteo, number1, " ", number2, " ", number3, " ", number4, " ", number5, " ", number6, " ", number7, " ",
          number8, " ", number9, " ", number10, " ", number11, " ", number12, " ", number13, " ", number14, " ", tipo_ingreso)

    tipo_sorteo_db.objects.create(id_sorteo=numero_sorteo, fecha=fecha, number1=number1, number2=number2, number3=number3, number4=number4, number5=number5, number6=number6,
                                  number7=number7, number8=number8, number9=number9, number10=number10, number11=number11, number12=number12, number13=number13, number14=number14, tipo_ingreso=tipo_ingreso)
