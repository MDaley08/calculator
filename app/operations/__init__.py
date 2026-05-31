def validate_num(a):
    """
    Check if input is a valid Number

    Args:
        a: The input value of any type to check.
    Returns:
        True if input is an int or float, False otherwise
    """
    return isinstance(a,(int,float,complex)) and  not isinstance(a,bool)

def addition(a,b):
    """
    adds two numbers

    Args:
        a: first number to add
        b: second number to add
    Returns:
        the sum of a and b
    """
    if(validate_num(a) and validate_num(b)):
        return a + b
    else:   
        return "invalid input" #place holder, implement proper error later

def subtraction(a,b):
    """
    subtracts b from a

    Args:
        a: the minuend(number being subtracted from)
        b: subtrahend(number being subtracted)
    Returns:
        the difference of b from a
    """
    if(validate_num(a) and validate_num(b)):
        return a - b
    else:   
        return "invalid input" #place holder, implement proper error later

def multiplication(a,b):
    """
    multiplies a and b

    Args:
        a: first factor to be multiplied
        b: second factor to be multiplied
    Returns:
        the product of a and b
    """
    if(validate_num(a) and validate_num(b)):
        return a * b
    else:   
        return "invalid input" #place holder, implement proper error later

def division(a,b):
    """
    divided a by b

    Args:
        a: the dividend
        b: the divisor
    Returns:
        returns the quotient of a and b
    """
    
    if(validate_num(a) and validate_num(b)):
        return a / b
    else:   
        return "invalid input" #place holder, implement proper error later
