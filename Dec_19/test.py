# import os,sys,traceback
# import pymongo,pandas as pd
# from sensor.config import mongoclient
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


# df = pd.read_csv(r"C:\Users\Prince\Downloads\aps_failure_training_set1.csv")
# null_report = df.isna().sum()/df.shape[0]
# cols = null_report[null_report>0.2]
# cols
# import numpy as np

# file_path = r"C:\Users\Prince\Desktop\Practice\iNeuron\Dec_19\artifact\21122023__171243\data_transformation\transformed\train.npz"
# with open(file_path,"rb") as file_obj:
#     train_arr = np.load(file_obj)

# print(train_arr)
# print(train_arr.shape)


# class Person:
#     def __init__(self,name:str = "Prince",age=27):
#         self.name = name
#         self.age = age
# obj =Person()
# print(obj.name)
# print(obj.age)


# import os
# print(os.listdir('sensor'))



# dir_names = ['0','1']
# print(list(map(int,dir_names)))
# import dill
# file_path = r"C:\Users\Prince\Desktop\Practice\iNeuron\Dec_19\artifact\21122023__193032\data_transformation\transformer\transformer.pkl"
# with open(file_path,"rb") as file_obj:
#     obj = dill.load(file_obj)
# print(obj.feature_names_in_)

# import os
# print(os.path.join("prince"))
# print(os.listdir("hi"))

# if not os.path.exists("prince"):
#     print("hi")


# print(os.path.basename(os.getcwd()))
# import pandas as pd
# df = (pd.read_csv(r"C:\Users\Prince\Desktop\Practice\iNeuron\Dec_19\artifact\22122023__103040\data ingestion\dataset\train.csv").head())
# target_df = df['class']

# file_path = r"C:\Users\Prince\Desktop\Practice\iNeuron\Dec_19\artifact\21122023__193032\data_transformation\target_encoder\target_encoder.pkl"
# with open(file_path,"rb") as file:
#     file_content = dill.load(file)
# # print(file_content)
# # print(type(file_content))
# print(type(file_content))
# transformed_target_col = file_content.transform(target_df)
# print(transformed_target_col)
# print(type(transformed_target_col))


try:
    a = int(input())
    b = int(input())
    c = a/b
    d = a+b
    print(d)
except Exception as e:
    print(e)