def Solution(a):
    if a % 2 == 0:
        print(f"{a} is an Even Number")
    else:
        print(f"{a} is an Odd Number")

while True:
    user_input = input("Enter a number (or type 'quit' to stop): ").strip().lower()
    
    if user_input == "quit":
        print("Program ended. Goodbye!")
        break
    
    try:
        a = int(user_input)
        Solution(a)
    except ValueError:
        print("Please enter a valid integer or 'quit' to exit.")
