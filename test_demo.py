import demo

def test_calc_sum():
    total = demo.calc_sum(4, 5)
    assert total == 9


def test_calc_multiply():
    total = demo.calc_multiply(10, 5)
    assert total == 50


