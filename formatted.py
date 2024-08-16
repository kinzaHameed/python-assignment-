'''Formatted String Interpolation

Task: Given the variables name, age, and city, use f-strings to construct a sentence that describes a person using these variables.'''

name:str = "kinza"
age:int = 24
city:str ="Lahore"

sentence=(f"{name} is {age} and she lives in {city}")

print(sentence)