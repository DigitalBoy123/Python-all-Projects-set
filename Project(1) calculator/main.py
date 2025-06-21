# In this file we addrees the inputs of a user and import all the operations for execution in this project.
from calculator_functions import add_num, sub_num, mul_num,  div_num,  mod_num,sqrt_num, cube_root_num, factorial_num, square_num, pow_num, cube_num,table_of_num
def main():
    print("Welcome to the calculator!")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Power")
    print("7. Square Root")
    print("8. Cube Root")
    print("9. Factorial")
    print("10. Square")
    print("11. Cube")
    print("12. Table")
    try:
        choice = int(input("Enter your choice (1-12): "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 12.")
        return
    if choice in [1, 2, 3, 4, 5, 6]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if choice == 1:
                result = add_num(a, b)
            elif choice == 2:
                result = sub_num(a, b)
            elif choice == 3:
                result = mul_num(a, b)
            elif choice == 4:
                result = div_num(a, b)
            elif choice == 5:
                result = mod_num(a, b)
            elif choice == 6:
                result = pow_num(a, b)
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            return
    elif choice in [7, 8, 10, 11, 12]:
        try:
            a = int(input("Enter your number: "))
            
            if choice == 7:
                result = sqrt_num(a)
            elif choice == 8:
                result = cube_root_num(a)
            elif choice == 10:
                result = square_num(a)
            elif choice == 11:
                result = cube_num(a)
            elif choice == 12:
                result = table_of_num(a)
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            return
    elif choice == 9:
        try:
            if choice == 9:
                a = int(input("Enter a whole number for factorial: "))
                if a < 0:
                    print("Factorial is not defined for negative numbers.")
                    return
            result = factorial_num(a)
        except ValueError:
                    print("Invalid input. Please enter a whole number.")
                    return
    else:
        print("Invalid choice. Please try again.")
        return
    print(f"The result is/are: \n{result}")
    while True:
        try:
            content = input("Do you want to perform another operation? (yes/no): ").strip().lower()
            if content == 'yes':
                main()
                break
            elif content == 'no':
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        except:
            print("An error occurred. Please try again.")
if __name__ == "__main__":
    main()


 

