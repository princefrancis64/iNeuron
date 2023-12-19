import pymongo

from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://princefrancis64:Oejb2e2l74Gz4NAK@cluster0.o5qm0dq.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db =client.test
database = client['myinfo5']
collection = database["prince"]

# record = collection.find()
# for i in record:
    # print(i)

# data = collection.find({"companyName": "iNeuron"})
data = collection.find({"courseOffered": {"$gt":"E"}})
for i in data:
    print(i)

