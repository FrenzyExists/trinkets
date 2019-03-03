# Simple grade classifier

insert = input("Insert your grade: ")

score = int(insert)
 
if score <=100 and score >= 90:
        print("Your score is A")
        
elif score <=89 and score >= 80:
        print("Your score is B")

elif score <=79 and score >= 70:
        print("Your score is C")
        
elif score <=89 and score >= 60:
        print("Your score is D")

elif score <=59 and not score <=0:
        print("Your score is F")

elif score <=0:
    print("That score seems mysterious")
