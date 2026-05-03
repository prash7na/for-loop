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
    