from polynomials import Polynomial 
import pytest

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

@pytest.mark.parametrize(
    "a, b, sum",
    (
       ((1,),(0,1),(1,1)),
       ((2,0,3),(1,2),(3,2,3)),
       ((4,2),(10,2,4),(14,4,4)) 
    )
)

def test_add(a, b, sum):
    assert Polynomial(a)+Polynomial(b) == Polynomial(sum)

def test_add_scalar():
    assert Polynomial((2,1)) + 3 == Polynomial((5,1))

def test_reverse_add_scalar():
    assert 3 + Polynomial((2,1)) == Polynomial((5,1))

def test_add_unknown():
    with pytest.raises(TypeError):
        Polynomial((1,)) + "cat"    
