import os,sys,traceback
import pymongo,pandas as pd
from sensor.config import mongoclient
# print(os.getcwd())
# try:
#     a = int(input("enter the number"))

# except Exception as e:
#     a,b,c = sys.exc_info()
#     print("Exception class",a)
#     print("Exception message",b)
#     print("Traceback object",c)
#     print("Line no",c.tb_lineno)

# try:
#     a = int(input("enter the number"))

# except Exception as e:
#     print( traceback.format_exc())


# df = pd.DataFrame(mongoclient["aps"]["sensor"].find())
# print(df.head())
# print(type(df))

# # print(os.path.dirname(os.getcwd()))

# def square_fun(n):
#     x = [i*i for i in range(n)]
#     return x

# print(square_fun(7))


df = pd.read_csv(r"C:\Users\Prince\Downloads\aps_failure_training_set1.csv")
null_report = df.isna().sum()/df.shape[0]
cols = null_report[null_report>0.2]
cols