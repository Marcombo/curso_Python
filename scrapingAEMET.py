import requests
import bs4

# leemos el contenido de la web
# Reto: ¿podriamos hacer algun tipo de selector para que la ciudad a buscar sea dinamica en base a lo que introduzca
# el usuario en el programa de Python?
r = requests.get("http://www.aemet.es/es/eltiempo/prediccion/municipios/barcelona-id08019")
soup = bs4.BeautifulSoup(r.content, 'html.parser')

# NOTA: no vamos a hacer este ejemplo de código eficiente, ni vamos a asumir que tenemos conocimientos relevantes de diseño web
# vamos a seguir los pasos que alguien "novato" seguiria para sacar la información, aunque eso implique más código
# con eso mantendremos la lógica lo más intuitiva y simple posible.

# buscamos todos los dias, vemos que los dias estan almacenados en un TR de la clase "cabecera_loc_niv1"
diasTR = soup.find("tr",class_="cabecera_loc_niv1")

# hago esto (mirar solo dentro del TR de "cabecera_loc_niv1", ya que en general, con unas clases y atributos tan genericos,
# si no analizamos bien el código fuente de la web, no podemos estar seguros que no aparecen en otro sitios de la misma
dias = diasTR.findAll("th",class_="borde_izq_dcha_fecha")

# Dias es una lista de elementos, en el que su variable "text" contiene el dia. Podemos verlo con el codigo:

#for dia in dias:
#    print(dia.text)

# creamos una variable para tener un indice de los dias (nos servirá para asociar las franjas a los dias)
numero_dia = 0

# ahora vamos a por las franjas horarias y la temperatura
franjasTempTR = soup.find("tr",class_="cabecera_loc_niv2")

# seguimos con el mismo ejemplo de los dias, esto aunque es en realidad innecesario dividirlo en tantos pasos, creo que permite
# una mejor comprensión paso a paso del código, si nos guiamos por el contenido de la web.
franjasTempTH = franjasTempTR.findAll("th",class_="borde_izq_dcha_estado_cielo")

# iteramos todas las franjas
for elemento in franjasTempTH:
    # recumeramos el valor del texto de la fraja ...
    franja = elemento.find(class_="fuente09em")
    # ... y la temperatura
    temperatura = elemento.find(class_="no_wrap")
    # como hay franjas que no tienen temperatura, solo mostramos las que temperatura contiene algun valor
    if temperatura:
        # en dias[numero_dia].text tenemos el texto del numero del dia, comenzamos por el primer dia que tenemos disponible
        print(dias[numero_dia].text,"de",franja.text,"Temp:",temperatura.text)
        if "24" in franja.text:
            numero_dia = numero_dia + 1
            # en el caso que la franja.text contenga el valor 24, aumentamos el contador de dias
