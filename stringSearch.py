'''Task: Given the string s, use string methods to:
Find the index of "fox": get the starting index of the substring "fox". If "fox" is not found, it should return -1.
Count occurrences of "the": Use the string's built-in method to count how many times the substring "the" appears in the string.
s:str ="the quick brown fox jumps over the lazy dog"
'''
s:str= "the quick brown fox jumps over the lazy dog"
index_fox = s.find("fox")
count_the = s.count("the")

print(f"the index of 'fox' is {index_fox} ")
print(f"the occurrence of 'the' : {count_the}")