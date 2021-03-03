import matplotlib.pyplot
import pymongo
import csv

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bicing_stations_database
collection = db.stations_data


# nos devuelve las estaciones que han tenido en algun momento 6 o mas huecos libres.
stations = collection.find({"empty_slots":{"$gte":6}},{"_id":0,"time":1,"ebikes":1,"normal_bikes":1,"empty_slots":1,"name":1})
print(stations.count())
with open("bicing.output", 'w') as output_file:
    w = csv.DictWriter(output_file, stations[0].keys())
    w.writeheader()
    for station in stations:
        w.writerow(station)
