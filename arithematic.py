# Program: Simple Calculator with Error Handling

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Floor Division (//)")
print("6. Modulus (%)")
print("7. Exponentiation (**)")

choice = input("Enter your choice (1-7): ")

if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        print("Result:", result)
    else:
        print("Error: Division by zero")

elif choice == "5":
    if num2 != 0:
        result = num1 // num2
        print("Result:", result)
    else:
        print("Error: Division by zero")

elif choice == "6":
    if num2 != 0:
        result = num1 % num2
        print("Result:", result)
    else:
        print("Error: Division by zero")

elif choice == "7":
    result = num1 ** num2
    print("Result:", result)

else:
    print("Invalid choice")
