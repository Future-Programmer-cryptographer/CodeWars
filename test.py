import math 

def find_next_square(sq):
    check = math.sqrt(sq)
    if check - int(check) == 0: 
        return (check + 1 )**2
    else: 
        return -1

print(find_next_square(114))