# https://www.codewars.com/kata/56efc695740d30f963000557/train/python
def to_alternating_case(string):
    result = ''
    for i in string: 
        if i.islower():
            result += i.upper()
        else: 
            result += i.lower()
    return result 

print(to_alternating_case('hello world'))
