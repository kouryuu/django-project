import re
from collections import deque


def derivative(func):
    """ It makes the assumption that func is a polynomial with x as a free variable.
        this function returns the derivative of such polynomial
    """
    terms = re.split('[+-]+',func)
    signs_stack = deque(getSigns(func)) #I use a queue to store the sign symbols
    derivative_terms = []
    for term in terms:
        derivative_terms.append(deriveTerm(term))
    derivative = ""
    for term in derivative_terms:
        if len(signs_stack) > 0:
            derivative += term + signs_stack.popleft()
        else:
            derivative += term
    # Clean bothersome zero terms
    if derivative[0] == '0':
        derivative = derivative[1:]
    return derivative

def getSigns(func):
    """ Strips the sign symbols from a string function
        returns a list with such symbols
    """
    signs_stack = []
    for char in func:
        if char == '+' or char == '-':
            signs_stack.append(char)
    return signs_stack

def deriveTerm(term):
    """ Derives the term of a polynomial
        returns a term associated with the derivative of term
    """
    x_terms = 0
    coefficients = []
    for char in term:
        if char == 'x':
            x_terms += 1
        elif char == '0':
            return '0'
    number_string = ""
    number = 1
    digits_continue = False
    for char in term:
        if char.isdigit():
            digits_continue = True
            number_string += char
        elif char == '*' and digits_continue:
            print number
            number = int(number_string)*number
            number_string = ""
            digits_continue = False
    if x_terms == 0:
        return "0" # Derivative of a constant is always zero
    elif x_terms == 1:
        return str(number) # When the term has a variable raised to power one the derivative is its coefficient.
    else:
        coeff = x_terms* number # Multiply the power of the variable by the coefficient
        return str(coeff) + '*' + generateXs(x_terms - 1) # Returns the coefficient previously calculated concatenated with the x term with one less term
def generateXs(xs):
    """ Auxiliary function to generate as much x terms as xs values
        returns a string with concatenated x's
    """
    string = ""
    for i in range(0,xs):
        if i > 0:
            string += '*x'
        else:
            string += 'x'
    return string
def calculatePoint(func, point):
    """" Calculates a point in a function func
    """
    func_replaced = func.replace('x',str(point))
    print func_replaced
    return eval(func_replaced) #quite dangerous but simple solution use with validations
def genPoints(func):
    """ Generates points of values 1 ,10 ,20,30,40,50,60
    """
    points = [1 ,10 ,20,30,40,50,60]
    func_points = []
    for point in points:
        func_points.append(calculatePoint(func,point))
    return func_points
