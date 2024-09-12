from collections import Counter 
def stray(arr):
    count = Counter(arr)
    return min(count, key=count.get)
    
print(stray([1,1,3,1,1]))

# alternative method 

def stray(arr):
    for x in set(arr): 
        if arr.count(x) == 1: 
            return x 