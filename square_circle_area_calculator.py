# SQUARE / CIRCLE AREA CALCULATOR
# This was made from some code a friend of mine called Edgar did. I basically organize his code and fixed nad add some minor stuff
# Initiate variables required to calculate

    # Variables to calculate circle
pi = 3.14
rad = float(input("Enter radius of circle: "))
a_circle = pi*rad**2

    # Variables to calculate square
side = rad*2
a_square = side**2
    # Calculate area
a_final = round(a_square-a_circle, 4)

# Print Result
print(f'\nThe area of square is {a_square}')
print(f'\nThe area of circle is {a_circle}')
print(f'\nThe remaining area between circle and square is {a_final}')
