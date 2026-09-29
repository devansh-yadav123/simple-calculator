from addition import add
from subtraction import subtract
from multiplication import multiply
from division import divide


print("================================")
print("       MY SIMPLE CALCULATOR")
print("================================")


while True:

    try:
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nChoose operation")
        print("+ : Addition")
        print("- : Subtraction")
        print("* : Multiplication")
        print("/ : Division")

        choice = input("Enter your choice: ")

        if choice == "+":
            answer = add(num1, num2)

        elif choice == "-":
            answer = subtract(num1, num2)

        elif choice == "*":
            answer = multiply(num1, num2)

        elif choice == "/":
            answer = divide(num1, num2)

        else:
            print("Invalid choice")
            continue

        print("Answer =", answer)

    except ValueError:
        print("Please enter numbers only.")
        continue

    again = input("\nDo you want to calculate again? (y/n): ")

    if again.lower() != "y":
        print("\nThank you for using my calculator!")
        break