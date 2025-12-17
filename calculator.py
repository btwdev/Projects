while True:
    user_choice = input("1 :- Addition\n2:- Substraction\n3:- Multiplication\n4:- Divition\n5:- finding Roots\n'Quit' to stop the program\nEnter the Choice : ").strip().lower()
    
    if user_choice == 'quit':
        break

    if user_choice not in ['1', '2', '3', '4' , '5']:
        print("please Enter from the given option")
        continue
    
    user_choice = int(user_choice)
    num1 = int(input("Enter the first no. : "))
    num2 = int(input("Enter the second no. : "))

    def add():
        print(f"The Addition of {num1} and {num2} is {num1+num2}")

    def sub():
        print(f"The Substraction of {num1} and {num2} is {num1-num2}")

    def mul():
        print(f"The Multiplication of {num1} and {num2} is {num1*num2}")

    def div():
        print(f"The Divition of {num1} and {num2} is {num1/num2}")

    def root():
        print(f"the square root of {num1} is {num1**0.5}")
        print(f"the square root of {num2} is {num2**0.5}")


    if user_choice==1:
        add()

    elif user_choice==2:
        sub()

    elif user_choice==3:
        mul()

    elif user_choice==4:
        if num2 == 0:
            print(ZeroDivisionError)
            print(f"{num1} is Not Divisible by {num2} please enter another number")
            continue
        else:
            div()

    elif user_choice==5:
        root()