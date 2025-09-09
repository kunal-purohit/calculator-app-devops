# import sys
# import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from calculator.core import add, subtract, multiply

def test_add():
    """Test the add function."""
    assert add(5, 3) == 8
    assert add(10, 0) == 10

def test_subtract():
    """Test the subtract function."""
    assert subtract(10, 4) == 6
    assert subtract(5, 5) == 0

def test_multiply():
    """Test the multiply function."""
    assert multiply(3, 4) == 12
    assert multiply(7, 0) == 0

def test_input_validation():
    """Test that functions raise errors for invalid inputs."""
    with pytest.raises(ValueError):
        add(-1, 5)  # Negative input
    with pytest.raises(ValueError):
        subtract(10, 3.5)  # Float input
    with pytest.raises(ValueError):
        multiply("a", 2)  # String input
        
def test_negative_subtraction_result():
    """Test that subtraction resulting in a negative number raises an error."""
    with pytest.raises(ValueError):
        subtract(3, 10)
