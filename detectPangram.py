# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
# 25th August 2024 

# import string 
# alphabet = 'abcdefghikjlmnopqrstuvwxyz'
# alphabet = alphabet.translate((str.maketrans('', '', string.punctuation)))
# alphabet = sorted(alphabet)
# alphabet = set(alphabet) 

# def is_pangram(st):
#     st = st.lower()
#     st = "".join(c for c in st if c.isalpha())
#     st = st.replace(' ', '')
#     st = sorted(st)
#     st = set(st)
#     # print (st) 
#     # print (alphabet)
#     return True if st ==alphabet else False 


# So I went down the route of 'let's strip down the input into bare alphabets, convert both into a set, and then compare the sets... lovely... 

# This is a much more efficient approach: 

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

print(is_pangram('abcdefghijklm opqrstuvwxyz'))

def test_pangrams():        
        pangrams = [ "The quick brown fox jumps over the lazy dog.",
                     "Cwm fjord bank glyphs vext quiz",
                     "Pack my box with five dozen liquor jugs.",
                     "abcdefghijklm opqrstuvwxyz.",
                     "ABCD45EFGH,IJK,LMNOPQR56STUVW3XYZ"]