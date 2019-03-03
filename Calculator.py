# -*- coding: utf-8 -*-

# Created on Wed Feb  6 17:07:45 2019
# Basic Calculator 1.0v (and I am not going to do another version!!!)
# By wolF
"""
<<<<<<<<<<<<ITS FINALLY DONE!!!>>>>>>>>>>>>

This code is a tiny compilation of experiments I did during Algorithms class.
There might be bugs around, even tho I tried to eliminate most of them.
Compromises are also made, on purpose. 
It was made to play around with the code to see what will happen.
Don't ask how I made this, I have no idea how I did it.
Some stuff where made with the help of my professor and other classmates.
I know the code is kinda WET and it will remain like that.
I'm too lazy to DRY it.
I made it modular-like so you (the user who download this toy) can add stuff, I dunno, whatever you want.
Send me a coffee, I'm sleepy.
"""
killme = True # Mood...
while killme == True:    
    list = ["Options:","sum","subtract","multiply","divide","average", "factorial", "exponent","square_root", "decimal_to_binary", "binary_to_decimal", "art"]
    
    print("\n\n",list[0])
    print("Enter", "'"+list[1]+"'", "to add numbers")
    print("Enter", "'"+list[2]+"'", "to subtract numbers")
    print("Enter", "'"+list[3]+"'", "to multiply numbers")
    print("Enter", "'"+list[4]+"'", "to divide numbers")
    print("Enter", "'"+list[5]+"'", "to get average")
    print("Enter", "'"+list[6]+"'", "to obtain the factorial of a number")
    print("Enter", "'"+list[7]+"'", "to get exponentials")
    print("Enter", "'"+list[8]+"'", "to get square root")
    print("Enter", "'"+list[9]+"'", "to convert base ten to binary")
    print("Enter", "'"+list[10]+"'", "to convert binary to base ten")
    print("Enter", "'"+list[11]+"'", "to write a message to get ASCII art")   
    print("Enter 'exit' to end the program")
    
    
    operation = input("input desired operation: ")
    
    def operation_one(): #Sum operation
        try:
            r = int(input("how many numbers of inputs will you need?: "))
            all_t = []
            b = 0
            for k in range(0, r):
                t = float(input("write input:"))
                all_t.append(t)
                b = b + all_t[k]       
            print(f'The result is: {b}')
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return
        
    def operation_two(): #Subtract operation
        try:            
         # Defines the list of numbers to be calculated
            r = int(input('how many numbers of inputs will you need?: '))
            print(f'Number of inputs entered: {r}')
            all_t = []
            a = 1
            b = 0
            for k in range(0, r):
                t = float(input('write input:'))
                print(f't is {t}')
                all_t.append(t)
                print(f'all_t is {all_t}')
        # Performs the calculations required, in here it's subtraction        
            z = all_t[0]    
            while a < len(all_t):
                b = all_t[a]
                z = z - b
                a = a+1            
            print(f'The result is: {z}')  
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return
        
    def operation_three(): #Multiplication operation
        try:
            r = int(input("how many numbers of inputs will you need?: "))
            all_t = []
            b = 1
            for k in range(0, r):
                t = float(input("write input:"))
                all_t.append(t)
                b = b * all_t[k]
            print("The result is:", b)
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
        return
    
    def operation_four(): #Division operation
        try:            
         # Defines the list of numbers to be calculated
            r = int(input('how many numbers of inputs will you need?: '))
            print(f'Number of inputs entered: {r}')
            all_t = []
            a = 1
            b = 0
            for k in range(0, r):
                t = float(input('write input:'))
                print(f't is {t}')
                all_t.append(t)
                print(f'all_t is {all_t}')
        # Performs the calculations required, in here it's subtraction        
            z = all_t[0]    
            while a < len(all_t):
                b = all_t[a]
                z = z / b
                a = a+1            
            print(f'The result is: {round(z,4)}')  
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
        except ZeroDivisionError:
            print("ERROR: Cannot Divide over Zero")
            print("Please try again")
            return   
    
    def operation_five(): #Average Calculation
        try:
           r = int(input("how many numbers of inputs will you need?: "))
           all_t = []
           b = 0
           for k in range(0, r):
              t = float(input("write input:"))
              all_t.append(t)
              b = b + all_t[k]
           m = len(all_t)
           print("The result is:", b/m)
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return 
        
    def operation_six(): #Factorial Calculation NOTE: Remember add the feature of calculating more than one number at a time.
        try:
            f = int(input("Input factorial number: "))
            for u in range(1, f):
                f *= u
            print ("The result is:", f)
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return 
                 
    def operation_seven(): #Exponential Calculation
        try:
            num_1 = int(input("input base: "))
            num_2 = int(input("input exponent: "))
            print ("The result is:", num_1**num_2)
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
        except TypeError:
            print("ERROR: Only integers are valid")
            print("Please try again")
            return 

    def operation_eight(): #Square Root Calculation
        try:    
            radicand = float(input("Enter radicant number: "))
            index = float(input("Enter index number: "))
            calc =  radicand**(1/index)
            print(round(calc, 6))
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
        except ValueError:
            print("ERROR: Cannot calculate square root of a negative integer")
            print("Please try again")
            return
            
    def operation_nine(): #Decimal to binary
        try:
            num = int(input("Please enter a number: "))
            store = []
            while num > 0:
                res = num % 2
                store.append(res)
                num = int(num/2)           
            re_order = []
            k = len(store) - 1
            while k >= 0:
                re_order.append(store[k])
                k = k - 1
            print(store)
        except TypeError:
            print("ERROR: Only integers are valid")
            print("Please try again")
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return
        
    def operation_ten(): #Binary to decimal
        try:
            # BINARY TO DECIMAL
            # NOTE: PLEASE DON'T BLAME ME SEMPAI! :3
            
            # Split binary number into a list
            binary = input("Enter binary number: ")
            
            # r is True if it contains only 0 or 1; False otherwise the except will activate.
            r = all(e in ["0", "1"] for e in binary)
             
            string = []
            c_string = str(binary)
            for i in c_string:
                string.append(i)
            #print(string)   #Debug
            
            convert = [int(k) for k in string]
            #print(convert)  #Debug    
            
            # Re-order the list backwards
            store = []
            n = 0
            b = 0
            re_order = []
            k = len(convert) - 1
            while k >= 0:
                re_order.append(convert[k])
                k = k - 1
            #print(re_order) #Debug
            
            # Convert Binary List into Decimal
            for l in range(0, len(re_order)):
                temp = re_order[l] * 2**n
                n = n+1
                store.append(temp)
                b = b + store[l]
            print(b)    #Output
            if r == False:
                raise ValueError("ERROR: that's not a binary number")
        except ValueError:
            print("ERROR: Cannot calculate letters nor symbols")
            print("Please try again")
            return    
        
        
    def operation_eleven():  #ASCII ART MY FRIEND
        word = input("Write a mesage! \n\n")
        lngth = len(word)
    
        for x in range(0, lngth):
            c = word[x]
            c = c.upper()
            if (c == "A"):
                print("  AAAAAA  \n  A    A  \n  AAAAAA  \n  A    A  \n  A    A \n\n")
            elif (c == "B"):
                print("  BBBBBB  \n  B    B  \n  BBBBB   \n  B    B  \n  BBBBBB  \n\n")
            elif (c == "C"):
                print("  CCCCCC   \n  C  \n  C       \n  C       \n  CCCCCC  \n\n")
            elif (c == "D"):
                print("  DDDDD   \n  D    D  \n  D    D  \n  D    D  \n  DDDDD   \n\n")
            elif (c == "E"):
                print("  EEEEEE  \n  E       \n  EEEEE   \n  E       \n  EEEEEE  \n\n")
            elif (c == "F"):
                print("  FFFFFF  \n  F       \n  FFFFF   \n  F       \n  F       \n\n")
            elif (c == "G"):
                print("  GGGGGGG  \n  G       \n  G   GGG   \n  G     G  \n  GGGGGGG  \n\n")
            elif (c == "H"):
                print("  H    H  \n  H    H  \n  HHHHHH  \n  H    H  \n  H    H \n\n")
            elif (c == "I"):
                print("    II    \n    II    \n    II    \n    II    \n    II        \n\n")
            elif (c == "J"):
                print("  JJJJJJ  \n    JJ    \n    JJ    \n  J JJ  \n  JJJJ    \n\n")
            elif (c == "K"):
                print("  K   K   \n  K  K    \n  KK      \n  K  K    \n  K   K   \n\n")
            elif (c == "L"):
                print("  L      \n  L      \n  L      \n  L       \n  LLLLLL  \n\n")
            elif (c == "M"):
                print("  M    M   \n  MM  MM  \n  M MM M  \n  M    M   \n  M    M  \n\n")
            elif (c == "N"):
                print("  N    N  \n  NN   N  \n  N N  N  \n  N  N N  \n  N   NN  \n\n")
            elif (c == "O"):
                print("  OOOOOO   \n  O    O  \n  O    O  \n  O    O  \n  OOOOOO  \n\n")
            elif (c == "P"):
                print("  PPPPPP  \n  P    P  \n  PPPPPP  \n  P       \n  P       \n\n")
            elif (c == "Q"):
                print("  QQQQQQ  \n  Q    Q  \n  Q Q  Q  \n  Q  Q Q  \n  QQQQQQ   \n       Q \n\n")
            elif (c == "R"):
                print("  RRRRRR  \n  R    R \n  R RR   \n  R   R   \n  R    R  \n\n")
            elif (c == "S"):
                print("  SSSSSS    \n  S      \n  SSSSSS  \n       S  \n  SSSSSS   \n\n")
            elif (c == "T"):
                print("  TTTTTT  \n    TT     \n    TT    \n    TT    \n    TT     \n\n")
            elif (c == "U"):
                print("  U    U  \n  U    U   \n  U    U    \n  U    U    \n  UUUUUU   \n\n")
            elif (c == "V"):
                print("  V    V  \n  V    V  \n  V    V  \n   V  V   \n    VV    \n\n")
            elif (c == "W"):
                print("  W    W  \n  W    W  \n  W WW W  \n  WW  WW \n  W    W  \n\n")
            elif (c == "X"):
                print("  X    X  \n   X  X   \n    XX    \n   X  X   \n  X    X  \n\n")
            elif (c == "Y"):
                print("  Y    Y  \n   Y  Y   \n    YY    \n    YY    \n    YY    \n\n")
            elif (c == "Z"):
                print("   ZZZZZZ    \n       Z  \n     Z    \n   Z     \n  ZZZZZZ""  \n\n")
            elif (c == " "):
                print("..........\n..........\n..........\n..........\n\n")
            elif (c == "."):
                print("----..----\n\n")
            elif(c == "0"):
                print("  0000000  \n 00    000 \n 00  00 00 \n 00 00  00 \n 000    00 \n  0000000  \n\n")
            elif (c == "1"):
                print("    11    \n  1111    \n    11    \n    11    \n    11    \n 11111111 \n\n")
            elif(c == "2"):
                print("   222222  \n 22     22 \n 22    222 \n     222   \n   2222    \n 222222222 \n\n")
            elif(c == "3"):
                print("  3333333  \n 33     33 \n     3333  \n 33     33 \n 33     33 \n  3333333  \n\n")
            elif(c == "4"):
                print("       44  \n     4444  \n  444  44  \n 444444444 \n       44  \n       44  \n\n")
            elif(c == "5"):
                print(" 55555555  \n 55        \n 55555555  \n       555 \n 55    555 \n  5555555  \n\n")
            elif(c == "6"):
                print("  6666666  \n 66        \n 66666666  \n 666   666 \n 666   666 \n  6666666  \n\n")                
            elif(c == "7"): 
                print("  77777777 \n 77     77 \n       77  \n      77   \n     77    \n    77     \n\n")
            elif(c == "8"):
                print("  8888888  \n 888   888 \n  8888888  \n 888   888 \n 888   888 \n  8888888  \n\n")
            elif(c== "9"):
                print("  9999999  \n 999   999 \n 999   999 \n  99999999 \n        99 \n  9999999  \n\n")

    def operation_end():
        print("You exit the program")
        
    def operation_null():
        print("Unknown operation. Please try again.")
        return(operation)
    {
    list[1]: operation_one,
    list[2]: operation_two,
    list[3]: operation_three,
    list[4]: operation_four,
    list[5]: operation_five,
    list[6]: operation_six,
    list[7]: operation_seven,
    list[8]: operation_eight,
    list[9]: operation_nine,
    list[10]: operation_ten,
    list[11]: operation_eleven,
    "exit": operation_end
    }.get(operation, operation_null)()

    if operation == "exit":
        break
