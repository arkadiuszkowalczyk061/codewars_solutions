"""This method checks if the given number is a perfect square"""

def is_square(n):
    if n >= 0:
        if int(n**0.5)** 2 == n:
            return True
    return False

print(is_square(9))