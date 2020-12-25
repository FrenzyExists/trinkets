# Some simple eucladean function I did while practicing for a Discrete Math quiz

def eucladean(a:int, b:int):
    counter = 1
    while True:
        if a < b:
            a, b = b, a
        r = a%b
        q = a//b
        print(str(r) + " " + " " + str(counter) + " division")
        print(str(q) + " " + " " + str(counter) + " division\n")
        a = b
        b = r
        if r == 0:
            print(q)
            print(r)
            break
        counter +=1
