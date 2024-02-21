#given the cover price of the textbook is 80.25$
#the bookstore gets 40% discount
#5$ is charged as shipping for the first book 
# 2.25$ for every other book
print()
print()
copies=60
price=80.25
#let price1 be the cost of 60 copies with 40% discount
price1=(copies*price)*(1-0.4)
print("the number of purchase copies is", copies)
print("QUESTION 1")
print("What is the purchase price of 60 copies of the book for the bookstore by taking into account the discount (before shipping)?")
print("the discount price of the copies is", price1)
print()
print()
price2=price1+(5+(copies-1)*2.25)
print("QUESTION 2")
print("What is the total wholesale cost of the 60 copies that the bookstore purchases from the bookstore? ")
print("the total cost of the purchase with shipping would be", price2)
print()
print()
print("QUESTION 3")
print("What is the profit that the bookstore makes by selling the 60 books at full price ($80.25 per book)?")
print("the profit made by the bookstoreis", (copies*price)-price2)
print()
print()
print("QUESTION 4")
print("Allow the user to enter the number of books and display the profit made by the bookstore if all those books are sold.")
print()
n=int(input("enter the number of books(with discount, without shipping)"))
print()
print("the price of the books when sold without shipping and without discount is",n*price)
print()
p=0.6*n*price
#print("the price of the copies is(with discount)", 0.6*n*price)
p1=p+(5+(n-1)*2.25 )
print("the price of the copies with shipping and 40% discount is",p1)
print()
print("the profit made by the bookstore if all the books are sold at original price is",)
print((n*price)-p1)