def is_triangle(a,b,c):
    
    if a+b > c: 
        if a+c > b: 
            if b+c > a:
                return True 
            else: 
                return False 
        else: 
            return False 
    else: 
        return False  


"""
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
"""

print(is_triangle(1,2,3))
