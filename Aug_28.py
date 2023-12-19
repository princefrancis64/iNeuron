# OOPS

class Person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


prince_var = Person("prince", "francis", "prince.francis64@gmail.com", 1996)
print(prince_var.name)
print(prince_var.surname)
print(prince_var.year_of_birth)
print(prince_var.emailid)


# ////////////////////////////////////////////////////////////////////////////////////////////
class Person:
    def __init__(prince, name, surname, emailid, year_of_birth):
        prince.name1 = name
        prince.surname = surname
        prince.emailid = emailid
        prince.year_of_birth = year_of_birth

    def age(prince, current_year):
        return current_year - prince.year_of_birth


prince_var = Person('prince', 'francis', 'prince.francis64@gmail.com', 1996)
print(prince_var.age(2023))
print(prince_var.name1)


# /////////////////////////////////////////////////////////////////////////////////////////////////////

class Person:
    def __init__(self, name, surname, emailid, year_of_birth):
        self.name1 = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def age(self, current_year):
        return current_year - self.year_of_birth


var = Person('priya', 'francis')
print(var.name)

# ////////////////////////////////////////////////////////////////////////////////////////////
class Person:
    def age(self,current_year,year_of_birth):
        return current_year-year_of_birth

    def email_id_input(self,email_id):
        print(f'the email id entered is {email_id}')


    def ask_name(self):
        name = input("tell me your name -")
        return name

    def ask_dob(self):
        dob = int(input('ask the date of birth'))
        return dob

prince = Person()
# print(prince.age(2023,1996))
# prince.email_id_input("prince.francis64@gmail.com")
# print(prince.ask_name())
# print(prince.ask_dob())



# DAY 2 of OOPS

class person1:
    def __init__(self,name,surname,yob):
        self._name1= name
        self.__surname1 = surname
        self.yob1 = yob

prince = person1("prince","francis",1996)
print(prince._name1)
print(prince._person1__surname1)


x = "banana"
y =x.lstrip("ban")
print(y)
