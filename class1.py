class Person:
    def __init__(self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


prince = Person("Prince","Francis","prince.francis64@gmail.com",1996)
# print(prince.name)
# print(prince.surname)
# print(prince.emailid)
# print(prince.year_of_birth)

import os
s = os.getcwd()
print(s)