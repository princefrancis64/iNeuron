# from utls.utill import person2

# obj = person2("Priya","Annies",1999)
# print(obj._name1)
# print(obj._person2__surname1)
# print(obj.yob1)

# class Person:
#     def __init__(self,name,surname,yob):
#         self._name1 = name
#         self.__surname1 = surname
#         self.yob1 = yob

# Prince = Person("Prince","Francis",1996)
# print(Prince._name1)
# print(Prince._Person__surname1)


# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:",spam)
#     do_nonlocal()
#     print("After nonlocal assignment:",spam)
#     do_global()
#     print("After gloabl assignment:",spam)

# scope_test()
# print("In global scope:",spam)

# class Dog:
#     def __init__(self,name):
#         self.name = name
#         self.tricks = [] 

#     def add_trick(self,trick):
#         return self.tricks.append(trick)
    
# d = Dog("Fido")
# e = Dog("Buddy")
# d.add_trick("roll over")
# e.add_trick("Play dead")
# print(d.tricks)
# print(e.tricks)

# from dataclasses import dataclass

# @dataclass
# class Employee:
#     name:str
#     dept:str
#     salary:int

# john = Employee("John","Mechanical",40000)
# print(john.dept)
# print(john.salary)

import pandas as pd
import json

# df = pd.read_csv("diabetes.csv")
# df = df.loc[:11,:]
# # print(df.T)
# s = list(json.loads(df.T.to_json()).values())
# print(s)


# data = {'Name': ['Alice', 'Bob', 'Charlie'],
#         'Age': [25, 30, 35],
#         'City': ['New York', 'San Francisco', 'Los Angeles']}

# df = pd.DataFrame(data)
# transposed_dict = df.T.to_json()

# python_obj = json.loads(transposed_dict)
# print(python_obj)

l = list({"name":"Prince","father":"Francis","dob":1996}.values())
print(l)