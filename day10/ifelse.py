'''username =input("username: ")
password =input("password: ")
if username=="admin" and password=="admin123":
    print("Login Successful")
else:
    print("invalid credentials")'''



units=int(input("Enter the number of units consumed: "))
senior_citizen=input("Are you a senior citizen? (yes/no): ")

if 0 < units <= 100:
    total_bill = units * 1.5
elif 101 < units <= 200:
    total_bill = units * 2.5
elif 201 < units <= 500:
    total_bill = units * 4
else:
    total_bill = units * 6 

if senior_citizen == "yes":
    total_bill = total_bill - (total_bill * 0.10)
if units > 800:
    total_bill = total_bill + (total_bill * 0.05)

print("Final Bill Amount: ₹", total_bill)   



     