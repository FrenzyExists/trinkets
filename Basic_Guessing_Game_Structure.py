#Basic Guessing Game Structure
"""
This code is intended to be expanded, but I don't have any idea of what I
can do to make the game fun. Also I got tired, I guess.
"""

question = float(input("In what year WWI occured? "))
answer = 1914
error =  ((answer - question)/answer)

if error < 0:
    error = -1 * error;

if question == answer and error == 0.0:
    print("Correct!")
elif question != answer and error <= 0.10:
    print("Wrong!")
    print("You are close")
elif question != answer and error <= 0.30:
    print("Wrong!")
    print("Lukewarm")
elif question != answer:
    print("YOU SUCK!!!")
