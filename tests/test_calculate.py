import pytest

from calculate import divide


def test_divide_positive_by_negative():
    # Test dividing a positive number by a negative number
    result = divide(10.0, -2.0)
    assert result == -5.0

    # Additional test case with different values
    result = divide(15.0, -3.0)
    assert result == -5.0

    # Test with decimal values
    result = divide(7.5, -1.5)
    assert result == -5.0


def test_divide_negative_by_negative():
    # Test dividing a negative number by a negative number
    result = divide(-10.0, -2.0)
    assert result == 5.0

    # Additional test case with different values
    result = divide(-15.0, -3.0)
    assert result == 5.0

    # Test with decimal values
    result = divide(-7.5, -1.5)
    assert result == 5.0


def test_divide_zero_by_non_zero():
    # Test dividing zero by a positive number
    result = divide(0.0, 5.0)
    assert result == 0.0

    # Test dividing zero by a negative number
    result = divide(0.0, -3.0)
    assert result == 0.0

    # Test dividing zero by a decimal
    result = divide(0.0, 2.5)
    assert result == 0.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10.0, 0.0)
