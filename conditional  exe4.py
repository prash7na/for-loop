#5.
total_purchase_amount = int(input("Enter your purchase amount"))
user_input = 6000
if total_purchase_amount>5000:
   has_membership = input("Do you have membership?").lower()
   if has_membership == "yes":
     persent_membership = input("do you have membership card now?").lower()
     if persent_membership =="yes": 
      discount=total_purchase_amount*0.30
      final_amount=total_purchase_amount - discount
      print(f"final amount = {discount}")
      print(f"Total saved = {final_amount}" )
     else:
        print(f"Final bill = {total_purchase_amount}")
   else:
     print(f"Final bill = {total_purchase_amount}") 
else:
    print(f"Final bill = {total_purchase_amount}")



#6
print("Welcome to the Magic Forest")
direction = input("Go north or south").lower()
if direction =="north":
   print("stage 2")
   path = input("cross the river or follow the path").lower()
   if path == ("cross the river"):
      print("Stage 3")
      angel = input("Chose fairy,ogre and elf").lower()
      if angel==("elf"):
         print("Stage 4")
      else:
         print("Game over")
   else:
      print("Game over")
else:
   print("Game Over")


#10.
body_weight = float(input("Enter your body weight"))
height = float(input("Enter your height"))
BMI = body_weight/(height**2)

if BMI<18.5:
   print("Underweight")
elif 18.5<= BMI<=25:
   print("Normal weight")
elif 25<BMI<=30:
   print("Overweight")
else:
    print("Obese")



#16
units = float(input("Enter your electricity units"))
if units<=100:
   cost = units*5
   print(f"total_cost={cost}")
elif 100<units<=300:
   cost = (100*5)+((units-100)*8)
   print(f"total cost = {cost}")
else:
   cost=(100*5)+(200*8)+((units-200)*10)
   print(f"total cost = {cost}")

#19. A store gives a 20% discount if the total purchase is above RS
#1000 AND the customer is a member, or a 10% discount if the
#purchase is above RS 1000 but the customer is not a member. Write a
#program that takes total_amount and is_member (True/False) as
#input and prints the final amount after applying the correct discount
#or no discount
total_amount=int(input("Enter your amount"))
if total_purchase_amount>1000:
   is_member = input("Are you member(yes/no?").lower()
   if is_member == "yes":
      discount=total_amount*0.20
      final_amount=total_amount-discount
      print(f"final amount={final_amount}")
   else:
      discount=total_amount*0.10
      final_amount=total_amount-discount
      print(f"Final amount={final_amount}")
else:
   print(f"Final amount={total_amount}")

#20
weight=float(input("Enter your earth weight: "))
planet={
   1:0.38,
   2:0.91,
   3:0.38,
   4:2.53,
   5:1.07,
   6:0.89,
   7:1.14
}
planet_number=int(input("Enter your planet number(1-7): "))
if planet_number in planet:
   gravity=planet[planet_number]
   print(f"weight={weight}*{planet}")
else:
   print("Invalid planet number")


#21
math =float(input("Enter maths mark"))
science =float(input("Enter science mark"))
social =float(input("Enter social mark"))
nepali =float(input("Enter nepali mark"))

total_marks=math+science+social+nepali
print(f"total marks = {total_marks}")
percentage = (total_marks/400)*100
print(f"percentage={percentage}")
if percentage > 70:
   print("grade:distinction")
elif percentage>60:
   print("First")
elif percentage>40:
   print("pass")
else:
   print("fail")

#22
is_card_valid="true"
initial_balance = 5000
correct_pin=123

pin=int(input("Enter your pin"))
if pin == correct_pin:
   while True:
      print("\n---ATM MENU---")
      print("1=Withdraw")
      print("2=check Balance")
      print("3=Exit")
      choice = input("Select an option(1-3: ")
      if choice == "1":
         amount=float(input("Enter amount to withdraw"))
         if amount<=initial_balance:
            balance = initial_balance-amount
            print(f"Rs{amount} is detucted.you current balance is Rs{balance}")
         else:
            print("indufficient balance")
      elif choice =="2":
         print(f'Balance ={initial_balance}')
      elif choice =="3":
          print("Thank you for visiting.")
      else:
         print("Invalid option.")
else:
   print("Incorrect pin")


#23
target_floor=int(input("Enter your floor number(0-10): "))
weight=float(input("Enter your weight(In KG): "))
door_status=input("Is door open or closed?: ").lower()

if 0>target_floor or target_floor>10:
   print("Invalid Floor")
elif weight>500:
   print("over weight:lift cannot move")
elif door_status =="open":
   print("WARNING:CLOSE THE DOOR")
else:
   print("ACTIVATE ELEVATOR MOTION")
