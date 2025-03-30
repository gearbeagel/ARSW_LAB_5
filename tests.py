from main import double_factorial


def test_double_factorial_zero():
    assert double_factorial(0) == 1, "Тест не пройдено: 0!! повинно дорівнювати 1"


def test_double_factorial_one():
    assert double_factorial(1) == 1, "Тест не пройдено: 1!! повинно дорівнювати 1"


def test_double_factorial_three():
    assert double_factorial(3) == 3, "Тест не пройдено: 3!! повинно дорівнювати 3"


def test_double_factorial_four():
    assert double_factorial(4) == 8, "Тест не пройдено: 4!! повинно дорівнювати 8"


def test_double_factorial_large_number():
    assert double_factorial(10) == 3840, "Тест не пройдено: 10!! повинно дорівнювати 3840"


def test_double_factorial_negative():
    try:
        double_factorial(-5)
    except ValueError as e:
        assert str(e) == "n must be a non-negative integer", \
            "Тест не пройдено: повинно бути виключення для від'ємного n"
    else:
        assert False, "Тест не пройдено: повинно бути виключення для від'ємного n"


def test_double_factorial_invalid_data():
    try:
        double_factorial("string")
    except TypeError as e:
        assert str(e) == "n must be an integer", \
            "Тест не пройдено: повинно бути виключення для некоректного типу даних"
    else:
        assert False, "Тест не пройдено: повинно бути виключення для некоректного типу даних"
