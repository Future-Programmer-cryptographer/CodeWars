# https://www.codewars.com/kata/523f5d21c841566fde000009/train/python


# subtract one list from another 

def array_diff(a,b):
    result = [] 
    for i in a: 
        if i not in b: 
            result.append(i)
    return result 

print(array_diff([1,2,2,2,3],[2]))

""""
We create an empty list result that will store the elements of a that are not present in b.
We iterate over each element i in list a.
For each element i, we check if it is not present in list b using the not in operator.
If i is not present in b, we append it to the result list.
Finally, we return the result list.
"""