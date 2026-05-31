def _validate_num(a) -> float:
    """
    Check if input is a valid Number

    Args:
        a: The input value of any type to check.
    Returns:
        None if value is not a valid number, returns the number itself if it is
    """
    if not isinstance(a,(float,int)) or isinstance(a,bool):
        return None
    
    return float(a)

def addition(a: float ,b: float) -> float:
    """
    adds two numbers

    Args:
        a: first number to add
        b: second number to add
    Returns:
        the sum of a and b
    """
    val_a = _validate_num(a)
    val_b = _validate_num(b)

    if val_a and val_b:
        return val_a + val_b
    else:   
        return "invalid input" #place holder, implement proper error later

def subtraction(a: float,b: float) -> float:
    """
    subtracts b from a

    Args:
        a: the minuend(number being subtracted from)
        b: subtrahend(number being subtracted)
    Returns:
        the difference of b from a
    """
    val_a = _validate_num(a)
    val_b = _validate_num(b)

    if val_a and val_b:
        return val_a - val_b
    else:   
        return "invalid input" #place holder, implement proper error later

def multiplication(a: float,b: float) -> float:
    """
    multiplies a and b

    Args:
        a: first factor to be multiplied
        b: second factor to be multiplied
    Returns:
        the product of a and b
    """
    val_a = _validate_num(a)
    val_b = _validate_num(b)

    if val_a and val_b:
        return val_a * val_b
    else:   
        return "invalid input" #place holder, implement proper error later

def division(a: float,b: float) -> float:
    """
    divided a by b

    Args:
        a: the dividend
        b: the divisor
    Returns:
        returns the quotient of a and b
    """
    val_a = _validate_num(a)
    val_b = _validate_num(b)

    if val_a and val_b:
        return val_a / val_b
    else:   
        return "invalid input" #place holder, implement proper error later
