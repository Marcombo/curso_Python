import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client.test_database
collection=db.test_collection
documento={"nombre":"pepe","telefono":"2222"}
collection.insert_one(documento)
print(client.list_database_names())
print(db.list_collection_names())
print(collection.find_one({"nombre":"pepe"}))
