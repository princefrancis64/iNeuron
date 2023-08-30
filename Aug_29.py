# class person:
#     _name = 'prince'
#     __surname = "francis"
#     yob = 1996
#
#     def _age(self,current_year):
#         return current_year - self.yob
#
#     def __age1(self,current_year):
#         return current_year - self.yob
#
# obj = person()
# # print(obj._age(2023))
# # print(obj._person__age1(2023))
# print(obj._person__surname)
#
# class employee(person):
#     _name ="priya"
#     __surname = "annies"
#     yob = 1999
#
# obj1 = employee()
# print(obj1._name)
# print(obj1._employee__surname)
# print(obj1._person__surname)
#
#
# class car:
#     def __init__(self,body,engine,tyre):
#         self.body = body
#         self.engine = engine
#         self.tyre = tyre
#
#     def mileage(self):
#         print("mileage of this car")
#
# c = car("hard","1.5 turbo",'radial')
#
#
# class tata(car):
#     pass
#
# t = tata("ALPHA","V12","radial")
# t.mileage()
#
# class bank:
#     def transaction(self):
#         print("total transaction value")
#
#     def account_opening(self):
#         print("this will show you your account opening status")
#
#     def deposit(self):
#         print("this will show your deposited amount")
#
# class HDFC_bank(bank):
#
#     def hdfc_to_icic(self):
#         print("this will show you all the transaction happened to icici through hdfc")
#
# class icici(HDFC_bank):
#     pass
#
# i = icici()
# i.hdfc_to_icic()
# i.deposit()
# i.transaction()
# i.account_opening()
#
#
# class bank:
#
#     def transaction(self):
#         print("total transaction value")
#
#     def account_opening(self):
#         print("this will show you your account opening status")
#
#     def deposit(self):
#         print("this will show your deposited amount")
#
#     def test(self):
#         print("this is a test method from bank class")
#
# class HDFC_bank:
#
#     def hdfc_to_icici(self):
#         print("this will show you all transaction happened to icici bank through hdfc")
#
#     def test(self):
#         print("this is a test method from HDFC_bank class")
#
# class ineuron_bank:
#
#     def account_status_icici(self):
#         print("print an account status in icici")
#
#
# class icici(HDFC_bank,bank,ineuron_bank):
#     pass
#
# i = icici()
# i.test()
#
#
# class SIB:
#
#     def transactions_list(self):
#         print("this shows the transaction list from SIB bank")
#
#
# class ineuron:
#     def student(self):
#         print("get all the details of all students")
#
#     def acheivers(self):
#         print("get all the list of acheivers")
#
#     def hall_of_fame(self):
#         print("print everyone from hall of fame")
#
# class ineuron_vision(ineuron):
#     def student(self):
#         print("get all the details of filtered students")
#
#
# iv = ineuron_vision()
# iv.student()
# i = ineuron()
# i.student()
#
# # ---------------------------------------------------------------
# class ineuron:
#     __students = 'data science'
# # Abstraction of hiding of data
#     def students(self):
#         print("print the class of students",ineuron.__students)
#
# i = ineuron()
# i.students()
# print(i._ineuron__students)
#
# # ---------------------------------------------------------------------------
# class ineuron:
#
#     students1 = "data science"
#
#     def students(self):
#         print(self.students1)
#
# i = ineuron()
# i.students()
# i.students1 = "data analytics"
# i.students()
#
#
# class ineuron1:
#
#     __students1 = "data science"
#
#     def students(self):
#         print(self.__students1)
#
#
#     def student_change(self):
#         self.__students1 = input()
#
# i1 = ineuron1()
# i1.students()
# # i1.__students1 = "big data"
# # i1.students()
# i1.student_change()
# i1.students()


# Image scrapper
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as bs

search = input("enter what would you like to search")
url = f"https://www.google.com/search?tbm=isch&q={search}"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get(url)
wait = WebDriverWait(driver, 10)


page_height = driver.execute_script("return document.body.scrollHeight")
def scroll_down():
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

        new_page_height = driver.execute_script("return document.body.scrollHeight")

        if new_page_height == page_height:
            break


scroll_down()
#
# def getting_url():
#     data = requests.get(url)
#     arranged_data = bs(data.text,"html.parser")
#     elements = arranged_data.find_all('img')
#     for i in elements:
#         print(i.get('src'))

def getting_url1():
    actual_images = driver.find_elements_by_css_selector('img.rg_i.Q4LuWd"')
    for actual_image in actual_images:
        if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
            print(actual_image.get_attribute('src'))

getting_url1()