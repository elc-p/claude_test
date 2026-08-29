from src.stats import mean, top_n

def test_mean():
    assert mean([1, 2, 3]) == 2

def test_top_n():
    assert top_n([3, 1, 4, 1, 5], 2) == [5, 4]