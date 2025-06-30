def add(x: int, y: int) -> int:
    return x + y

def divide(x: int, y: int) -> float:
    if y == 0:
        raise ValueError
    return x / y

