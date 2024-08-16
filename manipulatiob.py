'''String Manipulation

Task: Given the string s, use string methods to:
Capitalize the first letter: make the first character uppercase and the rest of the string lowercase.
Convert to uppercase: change all characters in the string to uppercase.
Convert to lowercase: change all characters in the string to lowercase.
'''

#Capitalize the first letter: make the first character uppercase and the rest of the string lowercase
# Define the string
s = "hello, World!"

# Capitalize the first letter
capitalized = s.capitalize()

# Convert to uppercase
uppercase = s.upper()

# Convert to lowercase
lowercase = s.lower()

# Print the results
print(f"Original string: {s}")
print(f"Capitalized: {capitalized}")
print(f"Uppercase: {uppercase}")
print(f"Lowercase: {lowercase}")
