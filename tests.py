from main import double_factorial


def test_double_factorial_zero():
    assert double_factorial(0) == 1, "Тест не пройдено: 0!! повинно дорівнювати 1"


def test_double_factorial_one():
    assert double_factorial(1) == 1, "Тест не пройдено: 1!! повинно дорівнювати 1"


def test_double_factorial_three():
    assert double_factorial(3) == 3, "Тест не пройдено: 3!! повинно дорівнювати 3"


def test_double_factorial_large_number():
    expected_value = 1
    for i in range(1000, 0, -2):
        expected_value *= i

    result = double_factorial(1000)
    assert result == expected_value, "Тест не пройдено: 1000!! повинно дорівнювати обчисленому значенню"

def test_double_factorial_expression():
    assert double_factorial(3 + 1) == 8, "Тест не пройдено: 3+1!! повинно дорівнювати 8"


def test_double_factorial_e10():
    try:
        double_factorial(1e10)
    except TypeError as e:
        assert str(e) == "n must be an integer", \
            "Тест не пройдено: повинно бути виключення для некоректного типу даних"
    else:
        assert False, "Тест не пройдено: повинно бути виключення для некоректного типу даних"


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


def test_double_factorial_float():
    try:
        double_factorial(5.5)
    except TypeError as e:
        assert str(e) == "n must be an integer", \
            "Тест не пройдено: повинно бути виключення для некоректного типу даних"
    else:
        assert False, "Тест не пройдено: повинно бути виключення для некоректного типу даних"


def test_double_factorial_none():
    try:
        double_factorial(None)
    except TypeError as e:
        assert str(e) == "n must be an integer", \
            "Тест не пройдено: повинно бути виключення для None"
    else:
        assert False, "Тест не пройдено: повинно бути виключення для None"
