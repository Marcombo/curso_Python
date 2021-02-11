import matplotlib.pyplot
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client.bicing_stations_database
collection = db.stations_data

# nos devuelve las estaciones que han tenido en algun momento 6 o mas huecos libres.
stations = collection.find({"empty_slots":{"$gte":6}},{"empty_slots":1,"name":1})
for station in stations:
    print(station)


# grafico sobre el historico de huecos libres de C/ LLACUNA, 86
name="C/ LLACUNA, 86"
stations = collection.find({"name":name})
x = []
y = []
for station in stations:
    x.append(station['time'])
    y.append(station['empty_slots'])
    #print(station)

matplotlib.pyplot.plot(x,y)
matplotlib.pyplot.show()