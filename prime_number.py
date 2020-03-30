def is_prime(n):
    if n <= 0 or n == 1:
        return False

    i = 2

    while (i <= n ** 0.5): # if number is not dividable by all numbers up to the square of original number it is a prime number
        if n % i == 0:
            return False
        i += 1
    return True

print((is_prime(5)))