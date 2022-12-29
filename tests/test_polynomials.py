from polynomials import Polynomial 


def test_print():
    p = Polynomial([0])
    q = Polynomial([0,1,0,4])
    r = Polynomial([1,1,0,0])

    assert str(p) == "0"
    assert str(q) == "4x^3 + x"
    assert str(r) == "x + 1"
