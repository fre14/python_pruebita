from app import Calculator

def test_sum():
    calc = Calculator()
    assert calc.sum(2, 3) == 5
    assert calc.sum(-1, 1) == 0
