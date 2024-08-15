def is_palindrome(s):
    s=s.lower()
    reverse = s[::-1]
    if s == reverse: 
        return True 
    else: 
        return False 
    
print(is_palindrome('Abba'))


# def is_palindrome(s):
#     s = s.lower()
#     return s == s[::-1]