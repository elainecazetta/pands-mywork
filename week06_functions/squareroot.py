# This program takes a positive floating-point number as input 
# and outputs an approximation of its square root, 
# through newton method at estimating square roots

def sqrt(number):
    guess = number / 2.0
    tolerance = 0.0001

    while abs(guess * guess - number) > tolerance:
        guess = (guess + number / guess) / 2

    return guess

num = float(input("Please enter a positive number: "))
result = sqrt(num)

print(f"The square root of {num} is approx. {result:.1f}")