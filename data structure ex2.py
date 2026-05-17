#1
#Create a dictionary mapping student names to email addresses. Write a
#program that prompts the user for a name. If the name exists, display the
#email, otherwise display contact not found.
dict = {
    "prashna":"bhukhaju217@gmail.com",
    "arisha":"arishna@gmail.com",
    "aman":"amanp00@gmail.com"}
name = input("Enter your name: ")

if name in dict:
    print(dict[name])
else:
    print("contact not found")

#2
shopping_list = {"milk","bread","eggs"}
bought = {"bread","eggs"}
unbought = shopping_list.difference(bought)
if unbought:
    print(unbought)
else:
    print("shopping completed")


#3
class_list = ["ram","sita","laxman"]
new_stutend = input("Enter the name: ").lower()
if new_stutend in class_list:
    print(f"{new_stutend} is already present")
else:
    class_list.append(new_stutend)
    print(f"conformation : {new_stutend} is added in class")


#4
votes = ["blue","red","blue","green","blue"]
blue_count =votes.count("blue")
if blue_count>=3:
    print("Blue wins")
else:
    print("Blue didnot win")

#5
grades = {"ram":92,"sita":88}
name = input("Enter your name: ")
if name in grades:
    print(f"grades:{grades[name]}")
else:
    print("Grade is not available")

#6
applicant = {
    "name":"priya",
    "skills":["java","SQL"],
    "expericence":1}
required_skills={"python","java"}
has_skill = required_skills.intersection(set(applicant["skills"]))
has_experience = applicant["expericence"]>=2
if has_skill and has_experience>=2:
    print("qualified")
else:
    print("not qualified")

#7
banned_items={"scissors","knife","lighter"}
weight = int(input("Enter your baggage weight: "))
items =input("Enter the items carried: ").lower()
if items in banned_items and weight>7:
    print("baggage not allowed")
else:
    print("baggage allowed")

#8
emp_dict={
    "emp1":{'name':'jhon','salary':7500},
    "emp2":{'name':'emma','salary':8000},
    "emp3":{'name':'shyam','salary':500}
}
emp_dict['emp3']['salary']=8500
print(emp_dict)

#9
ram = {"apple","banana","orange"}
laxman = {"orange","kiwi","mango"}
common = ram.intersection(laxman)
if common:
    print(common)
else:
    print("they picked completely different items")

#10
list = [10,10,30]
tuple=10,20,30
set ={40,55}
dict = {"b":"true"}
val = 20

if val in list and val in tuple:
    print("Entered step 2")
    if "b" in dict and val not in set:
        print("verified token route")
        print("Path A")
    else:
        print("access denied/route diverted")
        print("path B")
      
else:
    print("token rejected")
    print("path C")

#16.Create a dictionary menu where Pizza is 15, Burger is 10, and Salad is 8. Set
#order = ‘Pizza’. Write a program that checks if the order exists as a key in
#the menu. If it does, print the price of that item; if not, print item not found

menu = {"pizza":15,"burger":10,"salad":8}
order = input("enter your order: ").lower()
if order in menu:
    print(menu[order])
else:
    print("item not found")

#17
student_data = {
    "name":"sam",
    "score":85
}
if student_data["score"]>=80:
    student_data["status"]="Pass"
    print(student_data)
else:
    student_data["status"]="review"
    print(student_data)
    
##18
database = {"admin":"1234","user":"abcd"}
user_input = 'admin'
user_pass = '1234'
if user_input in database and database[user_input]==user_pass:
    print("Login successful")
else:
    print("login failed") 

#19
emails = ['ram123@gmail.com','hari77@gmail.com']
blacklisted_email = {'hari77@gmail.com'}
current_email = 'hari77@test.com'
if current_email in emails and current_email not in blacklisted_email:
    print("Email sent")
else:
    print("Blocked")

#20
inventory = {"A1":50,"B2":0,"C3":10}
restricted_zones = {'B2','Z9'}
target = 'B2'
if target in inventory:
    if target not in restricted_zones:
        if inventory[target]>0:
            print("dispatch item")
        else:
            print("stock error")
    else:
        print("invalid zone")
else:
    print("invalid zone")        

#21
valid_courses = {'python', 'robotics', 'java'} 
hs_grades = [9,10,11,12]

name = input("Enter your name: ")
course = input("Enter your course")
grade = int(input("Enter your grades: "))
student_record = {
"name":name,
"course":course,
"grade":grade
}
if course in valid_courses:
    print("valid course")
    if grade in hs_grades:
        print("valid grades")
        if student_record["grade"]==9 and student_record['course']=="robotics":
            print(f"{name} is not eligible for {course}")
        else:
            print(f"{name} is approved for {course}")
    elif student_record["grade"]<9:
        print("grade too low")
    else:
        print("grades are too high")

else:
    print(f"{name} selected invalid course.")
