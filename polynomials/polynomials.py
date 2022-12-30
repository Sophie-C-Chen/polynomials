""" Defines polynomial class. """

class Polynomial:

    def __init__(self, coefs):

        self.coefficients = coefs

    def degree(self):
        coefs = self.coefficients
        for i in range(len(coefs)):
            if coefs[i]:
                return len(coefs)-1
                break
        return 0

    def __str__(self):

        """ Converts polynomial object into its familiar mathematical representation. """
        
        coefs = self.coefficients # list of coefs from lowest order term to highest order term.
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



        
        

