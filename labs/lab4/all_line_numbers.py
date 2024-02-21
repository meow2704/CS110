#Omyaasree Balaji
#Lab-4 Files And Functions
#CS110    



def line_processor(file):

    line_number = 1 #the number are always assigned from 0 hence we are prior assigning it to 1

    for line in file:

        print(f"{line_number}: ", line)

        line_number += 1 #moving to the next number for the next line



def main():
    
    file_name = input("Enter the name of the file: ")
    
    file = open(file_name, 'r') #opening the file only for reading and not write or append as no changes are made the file
    
    line_processor(file)
    

main()