def is_triangle(a,b,c):
    
    if a+b > c: 
        if a+c > b: 
            if b+c > a:
                return True 
    else: 
        return False  

    
print(is_triangle(1,2,3))
