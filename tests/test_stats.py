from src.stats import mean, fib

def test_mean_basico():
    assert mean([1, 2, 3]) == 2.0

def test_fib():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(5) == 5
    assert fib(10) == 55
