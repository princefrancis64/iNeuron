##variable declaration without using init method
import test1
print(test1)
obj3 = test1.Person("Prince","Francis",1990)
print(obj3.yob1)

class person:
    _name = "Prince"
    __surname = "Francis"
    yob = 1996

    def _age(self,current_year):
        return current_year - self.yob

    def __age1(self,current_year):
        return current_year - self.yob
    

obj = person()
# print(obj)
# print(obj._age(2023))
# print(obj._person__age1(2023))

class employee(person):
    _name ="Francis"
    __surname = "AL"
    yob = 1966


obj1 = employee()
# print(obj1._age(2023))
# print(obj1._person__age1(2023))
# print(obj1)
# print(obj1.yob)
# print(obj1._person__surname)
# print(obj1._name)
# print(obj1._employee__surname)