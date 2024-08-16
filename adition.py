''''
Write a Python program that takes two integer inputs from the user and calculates their sum. The program should perform the following tasks:

Prompt the user to enter the first number.
Read the input and convert it to an integer.
Prompt the user to enter the second number.
Read the input and convert it to an integer.
Calculate the sum of the two numbers.
Print the total sum with an appropriat message
'''
first_num = int(input("enter the first number"))
second_num = int(input("enter the second number"))
total= first_num + second_num
print(f"the sum of {first_num} and {second_num} is {total}")
