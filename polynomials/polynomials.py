""" Defines polynomial class. """

from numbers import Number

class Polynomial:

    def __init__(self, coefs): # coefs is a tuple, i.e., immutable!

        self.coefficients = coefs

    def degree(self):
        coefs = self.coefficients
        for i in range(len(coefs)):
            if coefs[i]:
                return len(coefs)-1
                break
        return 0

    def __str__(self):

        """ Converts polynomial object into its familiar algebraic representation. """
        
        coefs = self.coefficients # tuple of coefficients from lowest order term to highest order term.
        terms = []

        # convert each term of polynomial object into algebraic representation a_nx^n
        # where n is a natural number and a_n is real.
        if coefs[0]:
            terms.append(str(coefs[0])) # if constant term non-zero, include in algebraic rep of polynomial.
        if self.degree() and coefs[1]: # polynomial is at least of degree one and linear term non-zero
            terms.append(f"{'' if coefs[1]==1 else coefs[1]}x")
        
        # add remaining terms as algebraic strings to terms
        terms+=[f"{'' if c==1 else c}x^{d}" for d,c in enumerate(coefs[2:],start=2) if c]

        return " + ".join(reversed(terms)) or '0'

    def __eq__(self,other):

        return self.coefficients == other.coefficients

    def __add__(self, other):

        if isinstance(other, Polynomial):    
            common = min(self.degree(), other.degree()) + 1 # no. of common terms to be added together
            coefs = tuple(a + b for a, b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]

            return Polynomial(coefs)

        elif isinstance(other, Number):
            return Polynomial(((self.coefficients[0] + other,) + self.coefficients[1:]))

        else:
            return NotImplemented

    def __radd__(self, other):
        return self + other
       



        




        
        

