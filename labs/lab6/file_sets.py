#Omyaasree
#cs110
#lab6- Dictionaries, Sets, and APIs
#part 1 


import sys

def read_file(file_name):
    word_list = []
    with open(file_name, 'r') as file:
        text = file.readline()
        words = text.lower().split()    
        for word in words:
            word_list.append(word.strip('.,?!'))
            print(word)    
    return set(words)

def main():

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if len(sys.argv) != 3:
        print("please enter only 2 files : file1, file2")
        sys.exit(1)


    set1 = read_file(file1)
    set2 = read_file(file2)

    union = set1.union(set2)
    intersection = set1.intersection(set2)
    unique = (set1 - set2).union(set2 - set1)

    print(f"The list of all the unique words contained in both files is  {list(union)}")
    print(f"The list of the words that appear in both the files is  {list(intersection)}")
    print(f"The list of words that appear in one of the files but not both is  {list(unique)}")

main()