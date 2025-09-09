# calculator/core.py

def add(a, b):
    """Adds two positive integers."""
    if not (isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0):
        raise ValueError("Inputs must be positive integers.")
    return a + b

def subtract(a, b):
    """Subtracts the second positive integer from the first."""
    if not (isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0):
        raise ValueError("Inputs must be positive integers.")
    result = a - b
    if result < 0:
        raise ValueError("Subtraction result cannot be negative.")
    return result

def multiply(a, b):
    """Multiplies two positive integers."""
    if not (isinstance(a, int) and isinstance(b, int) and a >= 0 and b >= 0):
        raise ValueError("Inputs must be positive integers.")
    return a * b
