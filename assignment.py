# Define the ages based on the given conditions Age Assignments Based on the Riddle

'''Age Assignments Based on the Riddle

Problem Statement: Write a program to solve this age-related riddle! Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:
Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.
'''
anton_age = 21
beth_age = anton_age+6
chen_age = beth_age+ 20
drew_age = chen_age + anton_age
ethan_age = chen_age

# Print the ages
print(f"Anton age is {anton_age} years oldd ")
print(f"beth age is{anton_age+6} years old")
print(f"Chen is {chen_age} years old.")
print(f"Drew is {drew_age} years old.")
print(f"Ethan is {ethan_age} years old.")

