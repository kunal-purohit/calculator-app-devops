from calculator.core import add, multiply, subtract

def main():
    """A simple CLI for the calculator."""
    print("--- Simple Calculator ---")
    try:
        num1 = int(input("Enter the first positive integer: "))
        num2 = int(input("Enter the second positive integer: "))
        
        print(f"\nAddition: {num1} + {num2} = {add(num1, num2)}")
        print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")
        
        try:
            print(f"Subtraction: {num1} - {num2} = {subtract(num1, num2)}")
        except ValueError as e:
            print(f"Subtraction: {e}")

    except ValueError:
        print("\nError: Please enter valid positive integers only.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()