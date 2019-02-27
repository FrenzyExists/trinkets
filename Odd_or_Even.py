# Odd or Even?

#variables
num_int = int(input ("Insert a number, any number "))
#NOTE: divisor is by default 2.
divisor = 2

#Calculate
if divisor == 0:
    print("ERROR: Cannot divide by 0")

if num_int <0:
    num_int *= -1

if divisor <0:
    divisor *= -1
    
# We are simply making a substraction loop until
# our number is larger or equal to our divisor

while num_int >=divisor:
    num_int -=divisor

#Print it!
if num_int != 0 and divisor == 2:
    print("Odd")
elif num_int == 0 and divisor == 2:
    print("Even")
else:
    print("Not Even nor Odd")
    
#Some option thingy
option = input("Do you want to know the remainder amount?" + " ")
if option == "yes":
    print(num_int)
    
elif option == "no":
    print("GO TO HELL!")