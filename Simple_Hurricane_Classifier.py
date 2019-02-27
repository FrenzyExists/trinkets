#Basic Hurricane Classifier 

Windspeed = input("Input windspeeds: ")
wspd = int(Windspeed)

if wspd >= 74 and wspd <= 95:
	print("Huricane is category 1")
elif wspd >=96 and wspd <=110:
    print("Hurricane is category 2")
elif wspd >=111 and wspd <=129:
    print("Hurricane is category 3")
elif wspd >=130 and wspd <=156:
    print("Hurricane is category 4")    
elif wspd >=157:
    print("Hurricane is category 5")
else:
    print("Relax, no hurricane")