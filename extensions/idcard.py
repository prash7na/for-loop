#Methods
#upper(), lower(), title(), capitalize(), swapcase()
#1. A hospital system stores patient names in random case for example rahUl DahaL. Write a program to display the name in proper title format on the prescription.
name = "rahUl Dahal"
print(name.title())



#2. A cybersecurity system requires all passwords to be checked in lowercase for consistency. Take a password input like ‘Pass@123’ and convert it for comparison.
password = input("enter your password")
password = "Pass123"
print(password.islower())
print(password.lower())


# 3. A movie ticket booking system receives the movie name in lowercase ‘spider-man no way home’. Display it in title case on the ticket.
movie_name = "spider-man no way home"
print(movie_name.upper())


#4. A school notice board program takes a heading input and displays it in ALL CAPS for attention. Take input ‘annual sports day’ and display it.
program = input("enter your event")
program = "annual sports day"
print(program.upper())


#5. A fun CAPS-LOCK reversal tool takes the sentence ‘hELLO wORLD’ and swaps every letter's case. Write a program for this.
sentance = "hELLO wORLD"
print(sentance.swapcase())


#Methods

#find(), index(), count(), startswith(), endswith().
#6. A document editor wants to find the first position where the word ‘error’appears in a log message: ‘System error detected, error code 404’.
log_message = "System error detected"
print(log_message.find("error"))


#7. An email validation system checks whether an entered email ends with ‘@gmail.com’. Write a program to validate it.
email = "bhukhaju217@gmail.com"
print(email.endswith("@gmail.com"))


#8. A spam filter counts how many times the word ‘free’ appears in a message: ‘Get free stuff, free gifts and free coupons now!’.
message = "Get free stuff, free gifts and free coupons now"
print(message.count("free"))

#9. A URL checker verifies whether a website link starts with "https" for security. Write a program for this.
URL = "https.ifh"
print(URL.startswith("https"))

#10. A resume scanner checks whether the keyword ‘Python’ is present in a resume text. Use the in operator.
resume_text = "skills in python,java"
keyword = "Python"
print(keyword in resume_text)

#11. A bank transaction log uses index() to find the exact position of the word ‘FAILED’ in the message ‘Transaction FAILED due to low balance’.
message = "Transaction FAILED due to low balance"
print(message.find("FAILED"))

#12. A government office receives a file named ‘budget_report.pdf’. Write a Python program that checks whether the file is a PDF document or not using endswith() and directly print the result.
file_name="budget_report.pdf"
print(file_name.endswith(".pdf"))

#13. A telecom registration system receives a phone number ‘+977-9841123111’. Write a Python program that checks whether the phone number starts with the Nepal country code ‘+977’. Print the result directly.
phone_number="+977-9841123111"
print(phone_number.startswith("+977"))

#14. A cybersecurity system receives a url ‘https://www.moha.gov.np/’.
#Write a Python program that checks whether the URL belongs to a government website, print the result directly.
url ="https://www.moha.gov.np/"
print(url.endswith(".gov.np/"))

#Methods
#replace(), strip(), lstrip(), rstrip()

#15. A customer feedback form receives input with extra spaces: ‘ Great service! ‘. Clean it before saving to the database.
input = "Great service!"
print(input.strip())

#16. A chat application replaces all occurrences of a banned word ‘hate’ with ‘****’ in the message "I hate this, hate it completely".
message="I hate this, hate it completely"
print(message.replace("hate","****"))

#17. A file system receives filenames with leading slashes like ‘///student_records.pdf ‘. Remove the leading slashes.
filesname = "///students_records.pdf" 
print(filesname.lstrip("/"))

#A web scraper fetches product prices as ‘Price: $120.33 ‘ with trailing spaces. Clean the right side using rstrip() and remove symbols too.
Price= "$120.33"
print(Price.lstrip("$"))

#19. A phone number formatter takes ‘+977 984-123-4567’ and removes all dashes - using replace() to store only digits format. 
number = "+977 984-123-4567"
print(number.replace("-",""))

#Methods
#split(), join()

#20. A CSV file contains student data as ‘Aarav,22,Kathmandu,Computer Science’. Split it into individual fields and display each on a new line.
data= ["Aarav","22","Kathmandu","Computer Science"]
print(data.split(","))

#21. A social media app stores hashtags as a ‘Python, Coding, Nepal, Tech’.Join them with # prefix to display as #Python #Coding #Nepal #Tech.
hashtags =["Python", "Coding", "Nepal", "Tech"]
display_hashtags = '#'+'#'.join(hashtags)
print(display_hashtags)

#22. A train ticket system receives passenger names separated by commas:‘Ram, Shyam, Hari, Sita’. Split and count the total number of passengers.
name = ['Ram', 'Shyam',' Hari',' Sita']
print(name.split(","))

#23. A sentence builder takes individual words [‘The’, ‘flight’, ‘departs’, ‘at’,‘6AM’] and joins them with a space to form a proper sentence.
words= ['The', 'flight', 'departs', 'at','6AM']
sentence = "".join(words) 
print(sentance)

#Methods
#isdigit(), isalpha(), isalnum(), isspace(), isupper(), islower()

#24. A government form validation checks whether the entered age contains only digits. Take input ‘25’ or ‘25abc’ and validate it.
age = "24"
print(age.digit())

#25. A username registration system checks that the username contains only letters and numbers, no special characters.
username = "prashna7"
print(username.isalnum())

#26. A name field validator in a school admission form checks that the student's name contains only alphabets (no digits).
name = "Prashna"
print(name.isalpha())

#27. A PIN verification system checks whether the user's PIN is all uppercase letters for a code like ‘ASDF’.
pin = "ABC"
print(pin.isupper())

#28. A blank field detector in a form checks whether the user entered only spaces.
form = ""
print(form.isspace())