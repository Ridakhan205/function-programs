def book_name():
    book=[]
    book.append (input("enter book1 name : "))
    book.append (input("enter book2 name : "))
    book.append (input("enter book3 name : "))
    return book

def book_price():
     price=[]
     price.append (int(input("enter book1 price : ")))
     price.append (int(input("enter book2 price : ")))
     price.append (int(input("enter book3 price : ")))
     return price

def discount(price):
    total_price=sum(price)
    discount=total_price*(1-10/100)
    total_cost=discount
    return total_cost
book=book_name()
prices=book_price()
total_cost=discount(prices)

print("the books names are  these:" , book)
print("the books price are  these:" , prices)
print("the books total cost are  these:" ,total_cost )

if total_cost > 1000:
    shipping_charges=0
    print("shipping charges waved")
else:
    shipping_charges=200
    print("you have to pay 200rupees as shipping charges : ")

final_price= total_cost+shipping_charges
print("final_price is" ,final_price)











