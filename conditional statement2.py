#3
num = int(input("enter a number: "))
match num:
    case 1:print("spring")
    case 2:print("winter")
    case 3:print("summer")
    case 4:print("autum")
    case _:print("Invalid number")
    #case 1|2|3:print("Spring") ##prints spring when input is 1,2and3


#2
light = input("enter color: ")
match light:
    case "red":print("Stop")
    case"green":print("GO")
    case "Yellow":print("Ready")

#1
age = int(input("Enter your age"))
height = int (input("Enter your height"))
if age>=12 and height>=140:
    print("Valid")
else:
    print("Invalid")

#4
username =input("Enter Username")
password = input("Enter password")
if username =="admin":
    print("valid login")
    if password =="pass123":
        print("Valid password")
    else:
        print("Invalid login")
else:
    print("Invalid username")


#5
age =int(input("Enter your age"))
monthly_income = int(input("Enter your manthly income"))
credit_score = int(input("Enter your credit score"))
if (21<=age<=60) and(monthly_income>=30000) and ( credit_score>=700):
    print("Loan Approved")
else:
    if age>60 and age<21:
        print("Invalid age")
    elif monthly_income<30000:
        print("Monthly income must be greater that RS30000")
    elif credit_score<700:
        print("Credit score must be greater than 700")

#6
age = int(input("Enter your age: "))

if age <12:
    print("Free tickets")
else:
    if 12<=age<=60:
        has_membership = input("Do you have membership(yes/no): ").lower()
        if has_membership=="yes":
            print("Price=Rs150")
        else:
            print("price=Rs200")
    else:
      print("Price=Rs100")


#7
salary = int(input("Enter your sa;ary"))
year_of_service = int(input("Enter your year of servic"))
percent = 0.05

if year_of_service>5:
    netbonus = (salary*percent)
    print(f"net bonus={netbonus}")
else:
    print("You are not eligible for bonus")


#8
import math
radius=int(input("Enter raduis"))
Area = math.pi*(radius**2)
         

#9
age = int(input("Enter your age"))
gender = input("Enter your gaender").lower()
if age>=18 and age<30:
    if gender == "male":
       print("wage=700")
    else:
       print("wage=750")
elif age>=30 and age<=40:
    if gender =="male":
        print("wage=800")
    else:
        print("wage=850")
else:
    print("age must be greater than 18 and less than 40.")


#10
num =int(input("Enter number"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%3==0 and num%5!=5:
    print("Fizz")
elif num%3!=0 and num%5==0:
    print("Buzz")
else:
    print(f"{num}")
