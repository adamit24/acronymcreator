# Name: Taylor Adami
# Date: Feb 20, 2022
# Project: Acronym Creator
# File: acronym Creator --> main.py
#--------------------------------------------
# Python program to create acronyms
word = input('') # word to create acronym
text = (word.replace('of', '')).split()
string = '' # Creates a blank string variable to store the acronym

# Start for loop to iterate through text, which will split the word
for i in text:
    string = string + str(i[0]).upper() # Takes the strings first index and places it in the string variable

print('The Word Acronym: ', string) # Final Print satement
