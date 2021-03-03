import requests
import datetime
import pymongo
import time
import bs4

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bicing_stations_database
collection = db.stations_data

#db.stations_data.remove({})


r = requests.get("http://www.aemet.es/es/eltiempo/prediccion/municipios/barcelona-id08019")
soup = bs4.BeautifulSoup(r.content, 'html.parser')


franjasTempTR = soup.find("tr",class_="cabecera_loc_niv2")
franjasTempTH = franjasTempTR.find("th",class_="borde_izq_dcha_estado_cielo")
temperatura = franjasTempTH.find(class_="no_wrap").text[:-2]

print(temperatura)


while True:
    r = requests.get('http://api.citybik.es/v2/networks/bicing')
    bicingJson = r.json()
    listOfStations = []
    for station in bicingJson['network']['stations']:
        listOfStations.append({"stationId":station['id'],
                               "time":datetime.datetime.now(),
                               "name":station['name'],
                               "latitude":station['latitude'],
                               "longitude":station['longitude'],
                               "empty_slots":station['empty_slots'],
                               "ebikes":station['extra']['ebikes'],
                               "normal_bikes":station['extra']['normal_bikes'],
                               "temperatura":temperatura})
    print(len(listOfStations))
    print(listOfStations)
    collection.insert_many(listOfStations)
    time.sleep(60)

