# Some answer to some guy from a Udemy course while learning C++
# I made in Python instead, shut up

def triple_convert(A:list, B:list) -> int:
    length: int = len(A) if len(A) < len(B) else len(B) # Yeah I know I should save these lengths before shut up
    counter: int = 0
    for i in range(length):
        if A[i] != B[i]:
            temp_calc:int = A[i] - B[i]
            B[i] += temp_calc
            counter += 1
    return counter
