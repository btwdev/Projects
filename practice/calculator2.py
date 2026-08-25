import math

def get_numbers():
    nums = input("Enter numbers separated by space: ").split()
    return [float(n) for n in nums]

def get_single_number():
    return float(input("Enter number: "))

while True:
    print("\n------ Calculator ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Clear / New Input")
    print("8. Quit")
    print("------------------------")

    choice = input("Choose an option: ").strip().lower()

    if choice == "8" or choice == "quit":
        print("Calculator closed.")
        break

    # Multiple number operations
    if choice in ["1", "2", "3", "4"]:
        nums = get_numbers()

        if len(nums) < 2:
            print("Please enter at least two numbers.")
            continue

        if choice == "1":
            result = sum(nums)
            print("Result:", result)

        elif choice == "2":
            result = nums[0]
            for n in nums[1:]:
                result -= n
            print("Result:", result)

        elif choice == "3":
            result = 1
            for n in nums:
                result *= n
            print("Result:", result)

        elif choice == "4":
            try:
                result = nums[0]
                for n in nums[1:]:
                    result /= n
                print("Result:", result)
            except ZeroDivisionError:
                print("Cannot divide by zero.")

    # Single number operations
    elif choice in ["5", "6"]:
        if choice == "5":
            n = get_single_number()
            if n < 0:
                print("Square root of negative number is not possible.")
            else:
                print("Square Root:", math.sqrt(n))

        elif choice == "6":
            base = float(input("Enter base: "))
            power = float(input("Enter exponent: "))
            print("Result:", base ** power)

    elif choice == "7":
        print("Input cleared.")

    else:
        print("Invalid option. Please choose from the menu.")
