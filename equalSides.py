# 9th Sept 224 
# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/python

def find_even_index(arr):
    for i in range(len(arr)):
      leftSum = sum(arr[:i])
      rightSum = sum(arr[i+1:]) 
      if leftSum == rightSum:
         return i 
    return -1
      

print(find_even_index([1,100,50,-51,1,1]))
