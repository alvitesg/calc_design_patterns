# pylint: disable=invalid-name
def add(a, b):
    """Add two numbers.

    Args:
        a (float or int): The first addend.
        b (float or int): The second addend.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """Subtract two numbers.

    Args:
        a (float or int): The minuend.
        b (float or int): The subtrahend.

    Returns:
        float: The difference of a and b.
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers.

    Args:
        a (float or int): The multiplicand.
        b (float or int): The multiplier.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """Divide two numbers.

    Args:
        a (float or int): The dividend.
        b (float or int): The divisor.

    Raises:
        ValueError: If the divisor is zero.

    Returns:
        float: The quotient of a and b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
