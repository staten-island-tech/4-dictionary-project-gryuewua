bakery_items = [
    {
    "name": "cookies",
    "price": int("11"),
    "description": "Hard as concrete, tastes like concrete as well: do NOT use 'I can't believe it's not butter!'."
    },
    {"name":  "cake",
    "price": int("50"),
    "description": "Hopefully not as bad as those cookies, but that's wishful thinking."
    },
    {"name":  "pboy",
    "price": int("1"),
    "description": "placeholder"
    }
]

for index, item in enumerate(bakery_items):
    print(index, ":", item["name"])

purchase = int(input("What would you like to buy?"))  

receipt = []

total = []

print(bakery_items[purchase]["name"])
confirm = input("Are you sure?")
if confirm == "yes":
    receipt.append(bakery_items[purchase]["name"])
    total.append(bakery_items[purchase]["price"])
    purchase = int(input("What would you like to buy?"))
else:
    checkout = (input("Would you like to checkout"))  
    if checkout == "no":
        purchase = int(input("What would you like to buy?"))  
    elif checkout == "yes":
        end = input("Thank you for shopping with us! Would you like a reciept?")
        if end == "yes":
            print (receipt)
            print (f"Your total is ${sum(total)}")


'''if purchase == 0:
    print(bakery_items[0]["name"])
    confirm = input("Are you sure?")
    if confirm == "yes":
        receipt.append(bakery_items[0]["name"])
        total.append(bakery_items[0]["price"])
    else:
        checkout = (input("Would you like to checkout"))  
        if checkout == "no":
            purchase = int(input("What would you like to buy?"))  
        elif checkout == "yes":
            end = input("Thank you for shopping with us! Would you like a reciept?")
            if end == "yes":
                print (receipt)
                print (f"Your total is ${sum(total)}")
elif purchase == 1:
    print(bakery_items[1]["name"])
    confirm = input("Are you sure?")
    if confirm == "yes":
        receipt.append(bakery_items[1]["name"])
        total.append(bakery_items[1]["price"])
    else:
        checkout = (input("Would you like to checkout"))  
        if checkout == "no":
            purchase = int(input("What would you like to buy?"))  
        elif checkout == "yes":
            end = input("Thank you for shopping with us! Would you like a reciept?")
            if end == "yes":
                print (receipt)
                print (f"Your total is ${sum(total)}")
elif purchase == 2:
    print(bakery_items[2]["name"])
    confirm = input("Are you sure?")
    if confirm == "yes":
        receipt.append(bakery_items[2]["name"])
        total.append(bakery_items[2]["price"])
    else:
        checkout = (input("Would you like to checkout"))  
        if checkout == "no":
            purchase = int(input("What would you like to buy?"))  
        elif checkout == "yes":
            end = input("Thank you for shopping with us! Would you like a reciept?")
            if end == "yes":
                print (receipt)
                print (f"Your total is ${sum(total)}") '''