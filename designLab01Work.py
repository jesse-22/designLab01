#
# File:   designLab01Work.py
# Author: 6.01 Staff
# Date:   02-Sep-11
#
# Below are templates for your answers to three parts of Design Lab 1

# -----------------------------------------------------------------------------

def fib(n):
    count = 1
    num1 = 0
    num2 = 2
    next_number = num1 + num2

    while count <= n:
        print(next_number, end="")
        count += 1
        num1, num2 = num2, next_number
        next_number = num1 + num2


# -----------------------------------------------------------------------------

class V2:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def get_x(self):
        return self.v1

    def get_y(self):
        return self.v2

    def __add__(self, other):
        return V2(self.v1 + other.v1, self.v2 + other.v2)

    def __sub__(self, other):
        return V2(self.v1 - other.v1, self.v2 - other.v2)

    def __mul__(self, other):
        return V2(self.v1 * other.v1, self.v2 * other.v2)


# -----------------------------------------------------------------------------
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = list(coefficients)

    def __repr__(self):
        """
        method to return the canonical string representation
        of a polynomial.
        """
        return "Polynomial" + str(tuple(self.coefficients))

    def __str__(self):

        def x_expr(degree):
            if degree == 0:
                res = ""
            elif degree == 1:
                res = "x"
            else:
                res = "x^" + str(degree)
            return res

        degree = len(self.coefficients) - 1
        res = ""

        for i in range(0, degree + 1):
            coeff = self.coefficients[i]
            # nothing has to be done if coeff is 0:
            if abs(coeff) == 1 and i < degree:
                # 1 in front of x shouldn't occur, e.g. x instead of 1x
                # but we need the plus or minus sign:
                res += f"{'+' if coeff > 0 else '-'}{x_expr(degree - i)}"
            elif coeff != 0:
                res += f"{coeff:+g}{x_expr(degree - i)}"

        return res.lstrip('+')  # removing leading '+'
