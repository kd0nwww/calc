import functions

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("What we gonna do with these numbers?")
print("1 - Addition")
print("2 - Subtraction")
print("3 - Division")
print("4 - Multiplication")
choice = int(input())

if choice == 1:
    print(functions.add(a, b))
elif choice == 2:
    print(functions.subtract(a, b))
elif choice == 3:
    print(functions.divide(a, b))
elif choice == 4:
    print(functions.multiply(a, b))