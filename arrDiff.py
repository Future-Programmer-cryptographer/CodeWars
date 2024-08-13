# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


# subtract one list from another 

def array_diff(a,b):
    result = [] 
    for i in a: 
        if i not in b: 
            result.append(i)
    return result 

print(array_diff([1,2,2,2,3],[2]))