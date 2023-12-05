import sys
# while True:
#     try:
#         a = int(input("first number"))
#         b = int(input("Enter second number"))
#         c = a/b
#         break
#     except:
#         print(sys.exc_info())


# while True:
#     try:
#         a = int(input("first number"))
#         b = int(input("Enter second number"))
#         c = a/b
#         break
#     except:
#         a,b,c = sys.exc_info()
#         print("Exception class",a)
#         print("Exception message",b)
#         print("Traceback object ",c)
#         print("Line number",c.tb_lineno)

import traceback
# while True:
#     try:
#         a = int(input("first number"))
#         b = int(input("Enter second number"))
#         c = a/b
#         break
#     except:
#         print(traceback.format_exc())


#Custom Exception
# while True:
#     try:
#         a = int(input("first number:"))
#         b = int(input("second number"))
#         if a<0 or b<0:
#             raise Exception("negative number not allowed")
#         c = a/b
#         print("div is",c)
#         break
#     except ValueError:
#         print("please enter integer only")
#     except ZeroDivisionError:
#         print("please enter non zero denominator")
#     except Exception as e:
#         print(e)  


# class NegativeNumberException(Exception):
#     pass

# while True:
#     try:
#         a = int(input("first number:"))
#         b = int(input("second number"))
#         if a<0 or b<0:
#             raise NegativeNumberException("negative number not allowed")
#         c = a/b
#         print("div is",c)
#         break
#     except ValueError:
#         print("please enter integer only")
#     except ZeroDivisionError:
#         print("please enter non zero denominator")
#     except NegativeNumberException as e:
#         print(e) 

#else keyword
# try:
#     a = int(input("first number:"))
#     b = int(input("second number"))
# except:
#     print("don't use zero in denominator")
# else:
#     print("python rocks!!")

#finally keyword
try:
    a = int(input("first number:"))
    b = int(input("second number"))
    c= a/b
except:
    print("don't use zero in denominator")
finally:
    print("python rocks!!")