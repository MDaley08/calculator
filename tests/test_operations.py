import pytest 
from app.operations import addition, subtraction, multiplication, division

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

def test_subtraction_postitive():
    """test positive cases for subtraction"""
    assert subtraction(3.0,1.0) == pytest.approx(2.0)
    assert subtraction(4.0,-3.0) == pytest.approx(7.0)
    assert subtraction(2.0,0.0) == pytest.approx(2.0)

def test_subtraction_negative():
    """test negative cases for multiplication"""
    assert subtraction(1.0,3.0) == pytest.approx(-2.0)
    assert subtraction(-4.0,-3.0) == pytest.approx(-1.0)
    assert subtraction(-1.0,0.0) == pytest.approx(-1.0)

def test_multiplication_negative():
    """test negative cases for multiplication"""
    pass

def test_division_positive():
    """test positive cases for division"""
    pass

def test_division_negative():
    """test negative cases for division"""
    pass

def test_division_zero():
    """test """
    pass