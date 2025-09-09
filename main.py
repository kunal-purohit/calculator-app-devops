from calculator.core import add, multiply, subtract

def main():
    """A non-interactive script for automated runs."""
    print("--- Running Automated Calculator Sanity Check ---")
    
    num1 = 10
    num2 = 5
    
    print(f"Using numbers: {num1} and {num2}")
    
    try:
        # Perform and print all operations
        add_result = add(num1, num2)
        print(f"Addition Result: {add_result}")

        sub_result = subtract(num1, num2)
        print(f"Subtraction Result: {sub_result}")

        multi_result = multiply(num1, num2)
        print(f"Multiplication Result: {multi_result}")
        
        print("\nSanity check PASSED.")

    except Exception as e:
        print(f"\nSanity check FAILED: {e}")

if __name__ == "__main__":
    main()