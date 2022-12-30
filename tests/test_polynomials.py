from polynomials import Polynomial 

p = Polynomial([0])
q = Polynomial([0,1,0,4])
r = Polynomial([1,1,0,0])
m = Polynomial([1,1,0,0])

def test_print():
   
    assert str(p) == "0"
    assert str(q) == "4x^3 + x"
    assert str(r) == "x + 1"

def test_equality():
    
    assert m.coefficients == r.coefficients
