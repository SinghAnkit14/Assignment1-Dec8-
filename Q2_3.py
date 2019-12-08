'''
Q2_3)Write a Python program to reverse a word after accepting the input from the user.
'''
rev = input('Enter Word')
s = ""
for i in rev:
    s = i+s
print(s)
