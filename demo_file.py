### format method ###
#item = "moon"
#animal = "cow"
#print("The {} jumped over the {}".format(animal,item))
#positional argument
#print("The {0} jumprd over the {1}".format(animal,item))
#keyword argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))
#text
#text = "The {} jumped over the {}."
#print (text.format(animal,item))
# for numbers 
#number = 3.1459
#print("The number pi is {}".format(number))
 

 #### f-string method ### 
      #How to use ??
#name = "Ram"
#print (f"Hello! \n My name is {name}")
#name = "Hari"
#age = 23
#print(f"Hello \n My name is {name} \n I am {age} years old.")
        #formatting codes 
#import datetime


#today = datetime.datetime.today()
#print(f"{today:%B %d,%Y}")

#name = "Ram"
#age = 24
#print(f"My name is {name} \n I am {age} years old.")

###   replace
#name = "ram"
#print (name.replace('r','R'))

#price= "$12.33"
#print(price.replace("$",""))

#slicing
#num = "+977+1111"
#print(num[0:4]+ num[5:])


#replacing multiple letters using replace method
#name = "pyhton"
#print(name.replace("p","P").replace("n","N"))


###maketrans only returns S/key value.so we have to use translate the value to get the result.
#print(name.maketrans("pn","PN"))
#print(name.translate)


###    centre method

#name = "Ram"
#print(name.center(9,"*"))

###   operators:opertors are used to perform various operations
#  1.arithematic operators
#  2.assignment  operators;used to assign values
#  3.comparison operators;to compare between variables
#  4.Logical operators;AND,OR and NOT
#  5.Identity operatos(is);compare the object, not if they are equal but if they are the same object with same memory location
#x = ["apple","banana"]
#y = ["apple","banana"]
#z = x
#print(x is z)#true
#print(x is y)#false
#print(x==y)#true
 
#6.membership operators;it tests if a sequence is present in an object.
#fruits = {"apple","banana","mango"}
#print("banana" in fruits)#true
#print("guava" not in fruits)#true

#bitwise operators;compare binary numbers
#print(2 & 3)
#num1 = 18
#num2 = 17
#print(num1&num2)
#print(num1^num2)
#print(num1|num2)

#number1 = 21
#number2 = 23
#print(number1&number2)
#print(number1^number2)
#print(number1|number2)
#a = -19
#b = 117
#print(~a)
#print(~b)
#only for positive value
#step1;convert in binary
#step1;apply XOR (changes the sign bit)
#step2;apply1 1"complement and then 2's complment(doesn"t changes the sign bit)
#for negative :B,1's com,2's compl,TT


###   split method
#timestamp = "2026,12,13"
#print(timestamp[0:5])
#print(timestamp.split(","))#will split in place of (,)


###    ljust;shifts apace in the right

#name = "Ram"
#rint(name.ljust)

###    cleaning;shifting spacaces from left to right
#name = "eam"
#print(name.lstrip())#to shift into left


### startswith ;checks the prefix ot the starting of the data
#gives boolean value ahd is used in decision making.
#name ="tommy" 
#print(name.startswith("ram"))  

#endswith:
#url = "employee_record.pdf"
#print(url.endswith("pdf"))

#how it is used
#url = "employee_record.pdf"
#if url.endswith('.xllx'):
#    print("file not supported")
#else:


### find,rfind,index,rindex
#find returns-1 for not found but index gives value error for not found
#find work only on string but index work on strings,lists and tuples
#find=left,used to find if the datatype is present or not fron left to right
#r=right to left

#dataset = "ram is a boy"
#print(dataset.find("r"))
#print(dataset.rfind("r"))
#print(dataset.index("r"))
#print(dataset.rindex("r"))#allgive positive 

#to get negative index number
#index_number=dataset.rfind('r'
#print(-lens(dataset))

###isdecimal,isalpha,isdigit,isalnum
#num= "123"
#print(num.isdecimal()) #decimal
#print(num.isalpha())    #alphabet
#print(num.isdigit()) #digit
#pprint(num.isalnum())  #alphabet and number
#print(num.isnumeric()) #num,fractions and roman
#print(num.isspace()) #complete space all should be space
#print(num.isprintable()) #escape characters=False 



#name = input("enter your name")
#name = "Laxman Devkota"
#print(f"Your user name is :{name} ")
#step1=name.replace("","_")
#print(step1)
#print("_".join(step1))

#first_name="ram"
#middle_name="bahadur"
#last_name="kc"
#print(first_name,middle_name,last_name,sep="_")
#print("_".join((first_name,middle_name,last_name)))

#to capitalize the all the first word.
#text = "see you soon!"
#print(text.title())

#to capitalize the the first letter of the sentences.
#text = "see you soon.how are you?"
#print()



#text = "python is good"
#print(text.upper())
#print(text.lower())
#print(text.title())
#print(text.swapcase())
#print(text.capitalize())
#print(text.casefold())
#print(text.center(40))
#print(text.count(""))
#print(text.encode())
#print(text.find("is"))
#print("_".join(text))

#print(2**2**3)
#print(10/2//3)

#### Input function
#asks user for thr information from the keyboard.
#converts the given info in string only
#typecasting;changing the datatype
#implicit conversion:doesn't need user involvement
#explicit conversion:needs users involvement to convert
#eval function is used to convert the datatype in all type
#sep parameter ;print(year,month,sep="")
#end perameter :print("Hello", end=" ")
#print("World")
# Output: Hello World (on a single line)

####conditional statement
#age =  18
#if age>= 18 :
#    print("You are an adult")

###else
#temperature = 35
#if temperature >30: 
#    print("It is hot outside.")
#    print("Too hot")
#else:
#    print("The weather is good.")


#elif
#score = 75
#if score >= 90:
#    grade = "A"
#elif score>= 80:
#    grade = "B"

#marks = 45
#if marks>=90:
#    print("Grade = A")
#elif marks>80:
#    print("Grade = B")
#elif marks>70:
#    print("Grade = C")
#else:
#    print("Failed")

#name = "Ram"
#age =14

#if age >=18:
#    print(f"{name} is regestered to vote.")
#else:
#    print(f"{name} is an invalid user.")
#    print("You must 18+.")


#1
#num = int(input("Enter a number"))
#if num<=100:
#   print("Valid")
#else:
#    print("invalid") 

#2)
#num = int(input("Enter a number."))
#if num %2 == 0:
#    print("Even")
#else:
#    print("odd") 


#3
#num = int(input("Enter number between 1-12"))
#if num==1:
#    print("January")
#elif num==2:
#     print("feb")
#elif num==3:
#     print("march")
#elif num==4:
#     print("april")
#elif num==5:
#print("may")
#elif num==6:
#     print("june")
#elif num==7:
#     print("july")
#elif num== 8:
#     print("aug")
#elif num==9 :
#     print("sep")
#lif num==10:
#     print("oct")
#elif num== 11:
#     print("nov")
#elif num ==12:
#     print("dec")
#else:
#     print("Invalid")

###in dictionary method
#user_input= int(input("Enter a number"))
 # month={1:"jan,"}

#6
#num1 =int(input("enter num1"))
#num2 = int(input("enter num2"))
#op = input("enter op")
#ops = {"+": num1+num2,"-":num1-num2}
#if op in ops:
#     print(ops[op])
#else:
 #    print('invalid symbol')

 
#8
#integer = int(input("enter an integer"))
#if integer%3==0 and integer%5==0:
#    print("FizzBuzz")
#elif integer%3==0:
#    print("Fizz")
#elif integer%5==0:
#    print("Buzz")
#else:"nothing"

#7
#salary = int(input("Enter your salary"))
#Creditscore = int(input("Enter your credit score"))
#if salary >=50000 and Creditscore >=700:
#    print("Eligiable")
#else:
#    print("Not Eligible")



### first name
#first_name = input("Enter your name: ")
#if first_name =="":
#    print("First name cannot be empty.")
#elif not first_name.isalpha():
#    print("Must be letters only")
#else:
#    print("Valid")

###Last name
#last_name = input("Enter your last name: ")
#if last_name=="":
    #print("Last name cannot be empty")
#elif last_name.isalpha:
#    print("Valid")
#else:
#    print("Must be lettrs only.")


###email
#email = input("Enter your E-mail")
#if "@"in email and "." in email:
#    print("Valid")
#else:
#    print("Invalid")


###Re-email
#re_email = input("Enter your email again")
#if re_email == email:
#    print("Valid")
#else:
#    print("E-mail and re-email doesnot match")


####Password
#password = int(input("Enter your password"))
#if len(password) >=6:
#    print("Valid")
#else:
#    print("minimum 6 characters needed")




##if not (First_name and Last_name and email and re_email):
##  print("all fields are mandatory")
#elif not(first_name.isaplha() and last_name,isalpha()):
     #print("must enter letters only")
#elif not("@" in email and "." in email and "@" in re_email and "." in re_email):
    #print("Invalid")
#elif not(email == re-email):
    #print("email not matched")
#else:
#print("Registered Sucessfully")


####   Nested 
#command1 = input("Scissor/Paper/rock")
#command2 = input("Scissor/Paper/rock")
#if command1 ==  command2:
#    print("It's a tie!!")

#elif command1 == "rock":
#  if command2 =="scissor":
#    print("Player 1 won")
#  else:
#    print("Player 2 won")
#
#elif command1=="scissor":
#  if command2=="rock":
#    print("player2 won")
#  else:
#     print("Player 1 won")
#
#elif command1 == "paper":
#    if command2 == "rock":
#        print("player1 won")
#    else:
#        print("Player 2 won")


#else:
#    print("Invalid input")


##### nested way
#balance = 20000
#is_card_valid = True

#correct_pin = 1234

#print("Weolcome to 123Back")

#user_pin = int(input("Enter your pin: "))

#if user_pin == correct_pin:
#    print ("1.check balance")
#    print(".Withdraw amount")
#    print("3.Exit")
#    choice= int(input("Select an option(1-3): "))
#    if choice ==1:
#        print(f"Your balance is {balance}")
#    elif choice ==2:
#        amount = int(input("Enter the amount"))
#          
#        if amount<= balance:
#           print(f"Please collect your cash:Rs{amount}")
#            print(f"your updated balance is Rs:{balance-amount}")
#        elif amount<=0:
#            print("Invalid amount")
#        else:
#            print("Insufficient Balance")
#    elif choice ==3:
#       print("Thank you for visiting.")
#    else:
#        print("Invalid selection")
#else:
#    print("Invalid Pin")
    

####    Elevator

#user_input = int(input("Enter your floor number (1-10):"))


#if 1<= user_input <=10:
#    print("Valid floor")
#    weight = int(input("Enter the total weight:"))
#    if weight<=500:
#        print("valid Weight")
#        door = input("Is the door closed?").lower()
#        if door =="yes":
#            print("Lift moving up")
#        else:
#            print("The door isnot closed.")
#    elif weight<0:
#        print("Invalid weight")
#    else:
#        print("weight cannot be more than 500kg")
#else:
#   print("Invalid floor")



####   Data structure
#1) List []
#list can store all kind of data types.



###how to add elements in list
######append=adds append(), it adds that entire list as a single nested element.
#nums = [1, 2, 3]
#nums.append([4, 5]) 
# Result: [1, 2, 3, [4, 5]]

######
#nsert(index, object)=Use this when you need to put an item in a specific spot rather than at the end
#nums = [1, 2, 3]
#nums.insert(1, "new") # Inserts at index 1
# Result: [1, "new", 2, 3]
#can only add iterable objects ie the object that can be used in indexing or loop

#####. extend(object);adds at the last individually.

#cart = ['apple','orange']
#cart.extend('orange')
#cart.extend('orange')
#cart.insert(0,"coke")
#print(cart)



###### how to remove in list
#remove=Use this when you know exactly what item you want to get rid of, but don't necessarily know where it is in the lis
#fruits = ['apple', 'banana', 'cherry', 'banana']
#fruits.remove('banana') 
# Result: ['apple', 'cherry', 'banana'] (Only the first 'banana' is gone)


#pop=Use this when you know the position of the item or when you need to use the deleted item after it’s removed
#fruits = ['apple', 'banana', 'cherry']

# Remove by index
#second_item = fruits.pop(1) 
# second_item is 'banana'; fruits is now ['apple', 'cherry']

# Remove the last item (default)
#last_item = fruits.pop() 
# last_item is 'cherry'; fruits is now ['apple']



###modify
#cart =['apple','orange']
#cart[0]="cake"
#print(cart)

####tuple:
#A tuple is an immutable ordered collection of elements.

#Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
#Can hold elements of different data types.
#These are ordered, heterogeneous and immutable.

#cart = 1,2,3,4,5
#print(cart[1:])
### chamge in list
#cart1=list(cart)
#cart1.pop(0)
#print(cart)


####set
#empty_set 
#1)items=set()
#i
#tems={*()}
# set doesnot have ordern.so we cannot do slicing and indexing
# set is unchangable
#hASTABLE Data structure create hashvalue for all the element and checks for same hasvalue for the same number and rejects them
#set cannot be modified-

###how to add items in set
#items ={1,2,3,4}
#items.add(6) to add one element
#items.update({7,8}) to add multiple element

####how to delete
#remove needs  to mention the element and  removes the element if present and if not present shows error
#discaed removes the element if present or gives the same output
#pop delets the first elemrnt as we cannot do indexing
## clear removes all and gives thr output empty set like set()

#difference = doesnA-b in set
#symmetric_difference=remoces all the common elemrnts and add the two set 
##union(|)=combines all the set
#intersection=writes only common
#is_disjoint=gives true if any elements of set1 is not present in set2
#is_subset=gives true if all the items are same from left to right
#items3=items.issuperset(items4)
#is_superset=gives true if all the items are same from rightto left

####   dictionary
#key value pair
#key is immutable and unique and value can be mutable or immutable


#how to get the value
#fruits = {"apple":"red","orange":"orange"}
#print(fruit['apple'])
#result.get("mango","fruit not found")
#print(result)


##how to add in dict
#fruits = {"apple":"red","orange":"orange"}
#fruit["mango"]="yellow"

#add many key value pairs
#del
#fruits = {"apple":"red","orange":"orange"}
#fruits.update({"mango":"yellow","kiwi":"green"})


###how to remove
#fruits = {"apple":"red","orange":"orange"}
#del fruits["apple"]


#pop
#fruits.pop()    #must pass the key
#fruits.popitem() #removes the last key and value

#clear
#fruits.clear()

##key,values and items
#fruits = {"apple":"red","orange":"orange"}

#nested dictionary
#students ={
#    "Ram":{"Math":34,"science":65},
#    "sita":{"Math":45,"science":56},
#}
#print(students["Ram"]["Math"])



data = {"a":10,"b":20,"a":30}
print(data)