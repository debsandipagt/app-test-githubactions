from src.math_operations import add, sub

def test_add():
    assert add(3,2)==5
    assert add(4, 5)==9

def test_sub():
    assert sub(5,3)==2
    assert sub(9,5)==4