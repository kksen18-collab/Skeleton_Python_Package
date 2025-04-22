from datacraft import remove_nulls

def test_remove_nulls():
    data = {"a": 1, "b": None, "c": 3}
    assert remove_nulls(data) == {"a": 1, "c": 3}