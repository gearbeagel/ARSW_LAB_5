def double_factorial(n):
    """
    Обчислює подвійний факторіал n!! для невід'ємного цілого числа n.

    :param n: Невід'ємне ціле число
    :return: Подвійний факторіал n!!
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result