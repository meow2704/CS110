# omyaasree
# cs110
# sorting a list of classes


from book import Book

def insertionSort_name(books):
    n = len(books)
      
    if n <= 1:
        return
    
    for i in range(1, n):
        key = books[i]
        j = i - 1
        while j >= 0 and key.get_name() < books[j].get_name():
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key

def insertionSort_num_pages(books):
    n = len(books)
      
    if n <= 1:
        return
    
    for i in range(1, n):
        key = books[i]
        j = i - 1
        while j >= 0 and key.get_num_pages() < books[j].get_num_pages():
            books[j + 1] = books[j]
            j -= 1
        books[j + 1] = key

def main():
    books = [
        Book("Harry Potter and the Sorcerer's Stone", 300),
        Book("Percy Jackson and the Sea of Monsters", 150),
        Book("Mark of Athena", 500),
        Book("Matilda", 200),
        Book("Charlie and the Chocolate Factory", 400)
    ]

    print("\nList of Book Objects:")
    for book in books:
        print(book)

    insertionSort_name(books)

    print("\nSorted List of Books by Name:")
    for book in books:
        print(book)
        insertionSort_num_pages(books)
    print("\nSorted List of Books by Name:")
    for book in books:  
        print(book)

if __name__ == '__main__':
    main()
