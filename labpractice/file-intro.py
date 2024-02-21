print("the contents of the text file\n")

text_handler = open("filetext.txt", "r")
reading = text_handler.read()
print(reading)

# Close the file after reading
text_handler.close()

# Reopen the file for searching
text_handler = open("filetext.txt", "r")

search_key = input("enter the word you want to search for: ")
find_count = 0

for line in text_handler:
    finder = line.lower().find(search_key.lower())
    if finder != -1:
        find_count += 1

print(f"the word {search_key} is found {find_count} times in the text file\n")

# Close the file after searching
text_handler.close()



output_text=str(f"\nthe word {search_key} is found {find_count} times in the text file.")

text_handler = open("filetext.txt", "a")
writing = text_handler.write(output_text)
