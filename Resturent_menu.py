print("--- MENU ---\n1. pizza   ₹100\n2. Burger    ₹50\n3. Maggie   ₹100\n4. Chai   ₹10\n~Please Comform your Order\n")
user = input("Place Your First Order:").strip().lower()
Pricing = {"pizza" : 100,
        "Burger" : 50,
        "Maggie" : 100,
        "Chai" : 10}
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

while True:
    user = input("Place Your Next Order & 'no' For View Bill:").strip().lower()
    if user=="no":
        print(f"Your Total Bill : {sum(order)}")
        print("Thank You For Visiting")
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
    else:
        print("Please Pick The correct Option")