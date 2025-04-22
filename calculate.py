def add(a: float, b: float) -> float:
    return a + b


def divide(a: float, b: float):
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Cannot divide by zero")
