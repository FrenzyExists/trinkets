# Function that outputs longest string from a string

def longest(string) -> str:
    k = ""
    g = ""
    for i in string.lower().split(","):
        if len(i) > len(g):
            k = i
            g = i
        elif len(i) == len(g):
            k += "," + i 
    return k
