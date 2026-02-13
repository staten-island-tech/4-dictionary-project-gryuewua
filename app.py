bakery_items = [
    {
    "name": "cookies",
    "price": int("11"),
    "description": "Hard as concrete, tastes like concrete as well: do NOT use 'I can't believe it's not butter!'."
    },
    {
        "name":  "cake",
    "price": int("50"),
    "description": "Hopefully not as bad as those cookies, but that's wishful thinking."
    },
    {
    "name":  "pboy",
    "price": int("1"),
    "description": "placeholder"
    }
]

for index, item in enumerate(bakery_items):
    print(index, ":", item["name"])

purchase = int(input("What would you like to buy?"))  

receipt = []

total = []

checkout = ""

while checkout != "yes":
    print(bakery_items[purchase]["name"])
    receipt.append(bakery_items[purchase]["name"])
    total.append(bakery_items[purchase]["price"])
    checkout = (input("Would you like to checkout?"))  
    if checkout == "no":
            for index, item in enumerate(bakery_items):
                print(index, ":", item["name"])
            purchase = int(input("What would you like to buy?"))  
    
if checkout == "yes":
    end = input("Thank you for shopping with us! Would you like a reciept?")
    if end == "yes":
        print (receipt)
        print (f"Your total is ${sum(total)}")
    elif end == "no":
        print (f"Your total is ${sum(total)}")