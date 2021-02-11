import requests
import datetime
import pymongo
import time

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bicing_stations_database
collection = db.stations_data


#elements = collection.find()
#for element in elements:
#    print(element)


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
                               "normal_bikes":station['extra']['normal_bikes']})
    print(listOfStations)
    collection.insert_many(listOfStations)
    time.sleep(60)
