# a = int(input("Enter your AGE: "))

# if(a > 18):
#     print("You are above the age of consent.")
#     print("Good to go!")

# elif(a < 0):
#     print("You are entering an invalid age.")

# else: 
#     print("You are below the age of consent.")

# print("End of progress")

# Practice sets
# Question 1
b = int(input("Enter your number 1: "))
c = int(input("Enter your number 2: "))
d = int(input("Enter your number 3: "))
e = int(input("Enter your number 4: "))
if (b>c) and (b>d) and (b>e):
    print("Number 1 is the greatest")
elif (c>b) and (c>d) and (c>e):
    print("Number 2 is the greatest")
elif (d>b) and (d>c) and (d>e):
    print("Number 3 is the greatest")
else:
    print("Number 4 is the greatest")

# Question 2
a = int(input("Enter your marks of subject 1: "))
b = int(input("Enter your marks of subject 2: "))
c = int(input("Enter your marks of subject 3: "))

total_marks = a + b + c
percentage = (total_marks / 300) * 100
if percentage >= 40 and a >= 33 and b >= 33 and c >= 33:
    print("You are passed.")
else:
    print("You are failed.")

# Question 3
p1 = "Make a alot of money"
p2 = "Buy now"
p3 = "Subscribe this"
p4 = "Click this"
message = input("Enter your message: ")
if (p1 in message) or (p2 in message) or (p3 in message) or (p4 in message):
    print("This is a spam message.")

# Question 4
username = input("Enter your username: ")
if len(username) < 10:
    print("Username must be at least 10 characters long.")
else:
    print("Username is valid.")

# Question 5
l = ["Areeb", "Ali", "Hassan", "Hussain"]
name = input("Enter your name: ")
if name in l:
    print("Your name is present in the list.") 
else:
    print("Your name is not present in the list.")

# Question 6
marks = int(input("Enter your marks: "))
if marks <= 100 and marks >= 90:
    print("Your grade is A+")
elif marks < 90 and marks >= 80:
    print("Your grade is A") 
elif marks < 80 and marks >= 70:
    print("Your grade is B")
elif marks < 70 and marks >= 60:
    print("Your grade is C")
elif marks < 60 and marks >= 50:
    print("Your grade is D")
elif marks < 50 and marks >= 40:
    print("Your grade is E")

# Question 7
post = input("Enter your post: ")
if "Hey" in post:
    print("Greeting detected.")
else:
    print("No greeting detected.")
