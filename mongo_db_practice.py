import pandas as pd
import pymongo
# df = pd.read_csv("diabetes.csv")
# print(df.columns)
# print(df.shape)
client = pymongo.MongoClient("mongodb+srv://princefrancis64:Oejb2e2l74Gz4NAK@cluster0.o5qm0dq.mongodb.net/?retryWrites=true&w=majority")
db = client["ineuron"]
collection = db["api_task"]
data = collection.find()
df = pd.DataFrame(data)
df.drop("_id",axis = 1,inplace = True)
# print(df)
# print("hssib")
# print("hi is autosave on")
# print("i think it is on")


