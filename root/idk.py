import pytest

# triple a number
def triple_number(a: int) -> int:
    """Multiplies a number by 3.

    :param a: The first factor.
    :return: The product.
    """
    return a * 3

def test_triple_integer_five():
    assert triple_number(5) == 15

def test_triple_integer_two():
    assert triple_number(2) == 6

# divide number by 2
def divide_by_two(a: float) -> float:
    """Divides a number by 2.

    :param a: The dividend.
    :return: The quotient.
    """
    return a / 2

def test_divide_even():
    assert pytest.approx(5) == divide_by_two(10)

def test_divide_decimal_result():
    assert pytest.approx(3.5) == divide_by_two(7)


# multiplies by 10
def multiply_by_ten(a: float | int) -> float | int:
    """Multiplies a number by 10.

    :param a: The first factor.
    :return: The product.
    """
    return a * 10

def test_multiply_positive():
    assert multiply_by_ten(4) == 40

def test_multiply_decimal():
    assert multiply_by_ten(1.2) == 12.0
