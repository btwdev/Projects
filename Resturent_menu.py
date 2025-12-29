print("--- MENU ---\n1. pizza   ₹100\n2. Burger    ₹50\n3. Maggie   ₹100\n4. Chai   ₹10\n5. Ice Creane    ₹70\n6.Break Samosa    ₹30\n~Please Comform your Order\n")
user = input("Place Your First Order:").strip().lower()
Pricing = {"pizza" : 100,
        "Burger" : 50,
        "Maggie" : 100,
        "Chai" : 10,
        "IceCreame" : 70,
        "BreakSamosa": 30}
order = []
if user=="1":
    order.append(Pricing["pizza"])
    print("You Order Pizza")
elif user=="2":
    order.append(Pricing["Burger"])
    print("You Order Burger")
elif user=="3":
    order.append(Pricing["Maggie"])
    print("You Order Maggie")
elif user=="4":
    order.append(Pricing["Chai"])
    print("You Order Chai")
elif user=="5":
    order.append(Pricing["IceCreame"])
    print("You Order Ice Creame")
elif user=="6":
    order.append(Pricing["BreakSamosa"])
    print("You Order BreakSamosa")

while True:
    user = input("Place Your Next Order & 'no' For View Bill:").strip().lower()
    if user=="no":
        print(f"Your Total Bill : {sum(order)}")
        print("Thank You For Visiting")
        print("You Have a Good Day")
        break
    elif user=="1":
        order.append(Pricing["pizza"])
        print("You Order Pizza")
    elif user=="2":
        order.append(Pricing["Burger"])
        print("You Order Burger")
    elif user=="3":
        order.append(Pricing["Maggie"])
        print("You Order Maggie")
    elif user=="4":
        order.append(Pricing["Chai"])
        print("You Order Chai")
    elif user=="5":
        order.append(Pricing["IceCreame"])
        print("You Order Ice Creame")
    elif user=="6":
        order.append(Pricing["BreakSamosa"])
        print("You Order BreakSamosa")
    else:
        print("Please Pick The correct Option")