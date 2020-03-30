# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy (divided_by in Ruby and Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Divison should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(function=None):
    if function is None:
        return 0
    else:
        return function(0)

def one(function=None):
    if function is None:
        return 1
    else:
        return function(1)

def two(function=None):
    if function is None:
        return 2
    else:
        return function(2)

def three(function=None):
    if function is None:
        return 3
    else:
        return function(3)

def four(function=None):
    if function is None:
        return 4
    else:
        return function(4)

def five(function=None):
    if function is None:
        return 5
    else:
        return function(5)

def six(function=None):
    if function is None:
        return 6
    else:
        return function(6)

def seven(function=None):
    if function is None:
        return 7
    else:
        return function(7)

def eight(function=None):
    if function is None:
        return 8
    else:
        return function(8)

def nine(function=None):
    if function is None:
        return 9
    else:
        return function(9)

def plus(number):
    return lambda x: x + number

def minus(number):
    return lambda x: x - number

def times(number):
    return lambda x: x * number

def divided_by(number):
    return lambda x: x // number

print(five(times((seven()))))
print(seven(divided_by(five())))