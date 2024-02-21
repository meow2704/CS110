# Project 1  - Analyzing Text Files
# CS 110
# Alark Joshi 

# Imports
# To use Regular Expressions
import re 
# To access the input provided at the command line (command line parameters)
import sys 

# Print the number of parameters / arguments provided by the user at the command line
print ("Number of arguments:", len(sys.argv), "arguments")

# Print the parameters printed at the command line
print ("Argument List:", str(sys.argv))

# The name of the text file is provided as the 2nd parameter and is accessed using index 1
# Index 0 contains the first element (name of the program)
# Index 1 contains the second element (name of the text file)
filename = sys.argv[1]

# Print the name of the text file to make sure that we're reading the correct text file
print(filename)

# Open the text file
file_handler = open(filename, "r", encoding="utf8") # The file is opened in READ mode using the "r" parameter

# Create empty lists
all_words = [] 
# This list will contain all the words in the text file
all_characters = [] 
# This list will contain all the characters in the text file

# Read the text file into the program one line at a time using a for loop
for one_line in file_handler:
    
    # Add all the characters in the file to the allcharacters list, one line at a time 
    all_characters.extend(one_line)

    # split the line with a regular expression on spaces
    # For example, "Hello, How are you?" is split into six strings: "Hello", ",", "How", "are", "you", "?"
    chunks = re.findall( r'\w+|[^\s\w]+', one_line)

    # If a line is empty, then do not add any words to the allwords list 
    if len(chunks) > 0:
        all_words.extend(chunks)

# This is to check that the contents of the file have been read into the all_characters and all_words lists
# For tiny_file.txt, len(all_characters) prints 20, len(all_words) prints 6
print(len(all_characters))
print(len(all_words))

# PART 1

# Initialize 3 variables to zero - one to count commas, one to count vowels, one to count consonants,

#Helper code: The following snippet of code prints each character in the file on a separate line
#for character in all_characters:
#  print(character)
for words in all_words:
    print(words)

# Iterate over the all_characters list to count the number of commas, the number of vowels, and the number of consonants
count_commas = 0
for comma_character in all_characters:

    if comma_character == "," :
        count_commas = count_commas + 1


print (f"\nthe file contains {count_commas} commas \n")


# Print the number of commas, vowels, and consonants

lowercase_vowels = 0
lowercase_consonants = 0
uppercase_vowels = 0
uppercase_consonants = 0
special_charecters = 0

for character in all_characters:

    if character.isalpha():

        if character.islower():

            if character == "a" or character == "e" or character == "i" or character== "o" or character == "u":
                lowercase_vowels += 1

            else:
                lowercase_consonants += 1

        else:   

            if character == "A" or character == "E" or character == "I" or character == "O" or character =="U":
                uppercase_vowels += 1

            else:
                uppercase_consonants += 1
    else:
        special_charecters+=1



print("for lowercase alphabets")

#for lowercase vowels 
print (f"the file contains {lowercase_vowels} lowercase vowels\n")
#for lowercase consonants
#print (f"the file contains {lowercase_consonants} lowercase consonants\n")

print("for both lowercase and uppercase alphabets")

#for uppercase and lower case vowels
print(f"the file contains {uppercase_vowels + lowercase_vowels} total vowels" )
# for uppercase and lower case consonants
print (f"the file contains {uppercase_consonants + lowercase_consonants} total consonants\n")

#for special characters
print(f"the file contains {special_charecters} special characters")


# Part 2
# (a) Count the number of times a user-specified word (the search key) is found in the file and display the count
# (b) Extend this using a loop to allow the user to keep entering words until the enter "exit" as the search key to exit the program
while (True):
    search_word = str(input("enter the word you would like to find the count for:  "))

    if search_word == "exit" :
        print ("exiting the program")
        break
    else:
        wordcount = 0
        for words in all_words:
            if words.lower() == search_word.lower():
                wordcount += 1
            
    print (f"the word you searched for has appeared {wordcount} time in the text file {filename}")

