'''1. Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.
Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."
Output
Number 1 is odd.
Number 2 is even.
Number 3 is odd.
Number 4 is even.
Number 5 is odd.'''

for i in range(1,6):
    if i%2==0:
        print(f"Number{i} is even.")
    else:
        print(f"Number{i} is odd.")


#2
page_no=[10,20,30,40]
running_total=0
for i in page_no:
   running_total+=i
   print(f"Added total{i}.Running total is{running_total} ")

print(f"final total={running_total}")

#3
student_name=['Ram','Hari','Sita']
print("---Email Greetings Generated---")
for name in student_name:
    print(f'Hi {name},your course approval is ready!.')

#4
page_counts= [45, 30, 50, 40] 
print("---Book Chapter Summary---")
for index,pages in enumerate(page_counts,start=1):
    print(f"Chapter {index} has {pages} pages.")

#5
data=[4,5,3,2]
product=1
for i in data:
    product*=i
print(f"Thr product is :{product}")

#6
num = 11
for i in range(1,11):
    print(f"{i}*{num}={i* num}")

#7
given_list = [3,2,1,4,5]
reverse=given_list[-1: :-1]
print(reverse)

#8
list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
common_elements=(set(list1)) & (set(list2))
print(list(common_elements))

#9
lst=[1,2,3,4]
new_lst =lst [::3]
print(new_lst)

#10
string = "my name is Ram."
vowels = "aeiouAEIOU"
result =""
for i in string:
  if i  not in vowels:
      result+=i

print(f"Without vowels:{result}")

#11
given_output='Loops are fun'
vowels_list="aeiouAEIOU"
vowel_num=0
consonant_num=0
for i in given_output:
    if i in vowels_list:
        vowel_num+=1
    else:
        consonant_num+=1
print(f"vowels= {vowel_num}")
print(f"consonant={consonant_num}")

#12
number=[1,2,3,4,5]
odd=[]
even=[]
for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(f"odd: {odd}")
print(f"even:{even}")


#13
given_num=int(input("Enter a num:"))
is_prime = True

if given_num<=1:
    is_prime=False
else:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            break
    else:
        print(f"{given_num} is a prime number.")

#14
mixed_list=[1,2,3,4,"a","b"]
integer = []
string=[]
for i in mixed_list:
    if type(i) == str:
        string.append(i)
    else:
        integer.append(i)
print(f"integer:{integer}")
print(f"string:{string}")

#15
given_string=str(input("Enter a string:"))
digits=0
letters=0
for i in given_string:
    if i.isdigit():
        digits+=1
    elif i.isalpha():
        letters+=1

print(f"no of digits:{digits}")
print(f'no of letters: {letters}')

#16
user_name=input("Enter username: ")
password=input("Enter Password: ")
if len(user_name)>=5 and len(password)>=8:
    print("Valid")
else:
    print("Invalid")

#17
given_number=int(input("Enter number: "))
if given_number%2==0:
    print(f"{given_number} is even.")
else:
    print(f'{given_number} is odd.')

#18
num = int(input("Enter a num: "))
fact=1
if num<0:
    print("There is no factorial.")
elif num==0:
    print("the factorial is 1.")
else:
    for i in range(1,num+1):
        fact=fact*i
    print(f"The factorial is {fact}")

#19
for i in range(1,9):
    for j in range(1,11):
        print(f"{i}*{j}={i*j}")


#21
odd=0
for i in range(1,6):
    if i%2!=0:
        odd+=i
print(odd)

#22
even=0
for i in range(1,6):
    if i%2==0:
        even+=i
print(even)

#23
text = "He is a good boy."
count = text.count("")
print(count)


#24
lst1=[1,2,3,4]
cube=[]
for i in lst1:
    cube.append(i**3)
print(cube)


#25
a ="programming"
rev=a[::-1]
print(rev)

#26
for i in range(50):
    if i <7:
        break
print(i)


#27
A="python"
for i in A:
    print(i)

#28
name =['ram''shyam']
for i in name:
    print(f"hello!{i}")

#29
names=['ram','shyam']
new=[]
for i in name:
    new.append(f"Dr,{i}")
print(new)

#30
N=[1,2,3,4]
square=[]
for i in N:
    square.append(N**2)
print(square)


#31
positive=[]
l=[111,32,-9,-45,-17,9,85,-10]
for i in l:
    if i>0:
        positive.append(i)
print(positive)

#32
giv_list=[0,1,2,3,4,5,6]
for i in giv_list:
    if i==3 and i==6:
        continue
print(i)


#33
first_list=['apple','mango',1,2,100,1.1]
sec_list=[]
for i in first_list:
    sec_list.append(type(i))
print(sec_list)

#34
for i in range(2):
    print(i)
else:
    print("Done")

#35
for i in range(105,0,-7):
   print(i)

#36
bad_chars = [';', ':', '!', "*"]
string = "py;th* o:n ! ;py * t*h:o !n"
for i in bad_chars:
    string=string.replace(i,"")
print(string)

#37
odd_no=0
even_no=0
for i in range(11):
    if i%2==0:
        odd_no+=1
    else:
        even_no+=1
print(f"odd:{odd_no}")
print(f"even:{even_no}")


#38
sum=0
for i in range(3,100):
    if i%3==0 or i%5==0:
       sum+=i
print(sum)


#39
sum_odd=0
sum_even=0
for i in range(1,101):
    if i%2==0:
        sum_even+=i
    else:
        sum_odd+=i
print(f"odd:{sum_odd}")
print(f"even:{sum_even}")


#40
list40=[10,20,10,30,10,40,50]
target=10
count=0
for i in list40:
    if i==target:
        count+=1
print(count)