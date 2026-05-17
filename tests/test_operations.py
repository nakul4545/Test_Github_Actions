from src.math_operations import add, sub 

def test_add():
    assert add(2,3) == 5 # these are test cases whether it is equal or not if yes then it will return true else false 
    assert add(-1,1) == 0 
    
def test_sub():
    assert sub(5,3) == 2
    assert sub(10,7) == 3 
    assert sub(1,2) == -1 
