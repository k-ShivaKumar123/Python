import random
numbers=['0','1','2','3','4','5','6','7','8','9']
print("****Welcome to OTP Generator****")
n_numbers=int(input("How many numbers OTP you want to generate:"))
OTP=" "
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    OTP += char
print(OTP)
print(f"Your One Time Password is {OTP}")
print("Thank You...")
