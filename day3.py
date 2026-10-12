# # #marks=int(input("Enter Your Marks"))
# # if marks  >=90:
# #     print("first Class")
# # elif marks >=75:
# #     print("Second class")
# # elif marks >=50:
# #     print("Third Class")
# # else:
# #     print("Poor performance")
# #--------------------------------------------------------------------------------------------------------
# # age=int(input("Enter Your Age:"))
# # has_id=bool(input("Enter your id type Yes/no:"))
# # if age>=18 and has_id == Yes:
# #     print("Entry Allowed")
# # if age<13 or age >60:
# #     print("Discount")
# # if not has_id:
# #     print("ID Required")
# #--------------------------------------------------------------------------------------------------------------
# # username=input("Enter Username")
# # password=input("Enter Password")

# # if username == 'admin':
# #     if password == 'ajay':
# #         print("Login successful")
# # else:
# #     print("Invalid User")
# #----------------------------------------------------------------------------------------------------------------
# age=int(input("enter Your Age:"))
# status="Adult" if age>18 else "Minor"
# print(status)
#--------------------------------------------------------------------------------------------------------------------
# name=""
# if name:
#     print("name is given")
# else:
#     print("name is empty")
#----------------------------------------------------------------------------------------------------
# for i in range(10,0,-2):
#     print(i)
#----------------------------------------------------------------------------------------------------
# for ch in "AI":
#     print(ch)
#------------------------------------------------------------------------------------------------------
# total = 0
# for n in range(0, -101, -1):
#     total +=n
# print("sum=",total)
#-----------------------------------------------------------------------------------------------------------
# num=5
# for i in range(1, 11):
#     print(f"{num}*{i}={num*i} sq={(num*i)**2}")
#------------------------------------------------------------------------------------------------------------
# count=1

# while count<=3:
#     print("count:",count)
#     count +=1
#--------------------------------------------------------------------------------------------------------
# for i in range(1,5):
#     print("*" * i)
#---------------------------------------------------------------------------------------------------------
# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i*j,end='')
#     print()
#---------------------------------------------------------------------------------------------------------
#Functions
# def greet():
#     print("Hello,World!")
# greet()
#--------------------------------------------------------------------------------------------------------
# def greet(name):
#     print("Hello", name)
# greet("ajay")
# greet("sumeet")
#----------------------------------------------------------------------------------------------
# def add(a, b):
#     return a+b
# result = add (10,5)
# print (result)
#----------------------------------------------------------------------------------------------
# def power(base,exp=2):
#     return base**exp
# print(power(5))
# print(power(2,3))
#---------------------------------------------------------------------------------------------
# def intro(name, city):
#     print(f"Hello {name} from {city}")

# intro(input("Name: "), input("City name: "))
#---------------------------------------------------------------------------------------------
#Variable scope
# x=10
# def show():
#     y=5
#     print(x,y)
# show()
#--------------------------------------------------------------------------------------------
#functions with conditions and loops

# def is_even(n):
#     return n%2 == 0
# def factorial(n):
#     result = 1
#     for i in range (1,n+1):
#         result *=1
#     return result
# print(is_even (8))
# print(factorial (5))
#--------------------------------------------------------------------------------------------
#lambda 
# sqr=int(input("enter a no"))
# square = lambda x: x*x 
# print(square(sqr))
#---------------------------------------------------------------------------------------------
# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "Error! Division by zero."
#     else:
#         return x / y


# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))

# while True:
#     print("\nChoose an operation:")
#     print("1. Add")
#     print("2. Subtract")
#     print("3. Multiply")
#     print("4. Divide")
#     print("5. Exit")

#     choice = input("Enter your choice (1-5): ")

#     if choice == '1':
#         print("Result:", add(x, y))

#     elif choice == '2':
#         print("Result:", subtract(x, y))

#     elif choice == '3':
#         print("Result:", multiply(x, y))

#     elif choice == '4':
#         print("Result:", divide(x, y))

#     elif choice == '5':
#         print("Exiting the program.")
#         break

#     else:
#         print("Invalid choice! Please choose 1-5.")
