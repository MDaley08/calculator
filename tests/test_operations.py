import pytest 
from app.operations import addition, subtraction, multiplication, division


def test_addition_invalid_input():
    "test invalid values for additon"
    assert addition('a', 1)
    assert addition(1, 'a')
    assert addition('a', 'b')


def test_addition_positive():
    """test positive cases for additon"""
    assert addition(1.0,1.0) == pytest.approx(2.0)
    assert addition(-1.0,2.0) == pytest.approx(1.0)
    assert addition(3.0,0.0) == pytest.approx(3.0)

def test_addition_negative():
    """test negative cases for additon"""
    assert addition(-3.0,-1.0) == pytest.approx(-4.0)
    assert addition(-3.0,1.0) == pytest.approx(-2.0)
    assert addition(-3.0,0.0) == pytest.approx(-3.0)


def test_subtraction_invalid_input():
    "test invalid values for multiplication"
    assert subtraction('a', 1)
    assert subtraction(1, 'a')
    assert subtraction('a', 'b')

def test_subtraction_postitive():
    """test positive cases for subtraction"""
    assert subtraction(3.0,1.0) == pytest.approx(2.0)
    assert subtraction(4.0,-3.0) == pytest.approx(7.0)
    assert subtraction(2.0,0.0) == pytest.approx(2.0)

def test_subtraction_negative():
    """test negative cases for subtraction"""
    assert subtraction(1.0,3.0) == pytest.approx(-2.0)
    assert subtraction(-4.0,-3.0) == pytest.approx(-1.0)
    assert subtraction(-1.0,0.0) == pytest.approx(-1.0)

def test_multiplication_invalid_input():
    "test invalid values for multiplicaiton"
    assert multiplication('a', 1)
    assert multiplication(1, 'a')
    assert multiplication('a', 'b')

def test_multiplication_positive():
    """test positive cases for multiplication""" 
    assert multiplication(1.0, 3.0) == pytest.approx(3.0)
    assert multiplication(-2.0, -3.0) == pytest.approx(6.0)
    assert multiplication(3.0, 0.0) == pytest.approx(0.0)

def test_multiplication_negative():
    """test negative cases for multiplication"""
    assert multiplication(-1.0,3.0) == pytest.approx(-3.0)
    assert multiplication(3.0,-8.0) == pytest.approx(-24.0)

def test_division_invalid_input():
    "test invalid values for additon"
    assert division('a', 1)
    assert division(1, 'a')
    assert division('a', 'b')

def test_division_positive():
    """test positive cases for division"""
    assert division(3.0, 1.0) == pytest.approx(3.0)
    assert division(-6.0, -3.0) == pytest.approx(2.0)

def test_division_negative():
    """test negative cases for division"""
    assert division(-3.0, 1.0) == pytest.approx(-3.0)
    assert division(6.0, -3.0) == pytest.approx(-2.0)

def test_division_zero():
    """test ValueError for division by zero"""
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        division(1.0,0)