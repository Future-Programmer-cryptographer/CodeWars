# def words(word1, word2):
#     possible = ""
#     word1 = ''.join(sorted(word1))
#     word2 = ''.join(sorted(word2))
#     for i in word2:
#         for j in word1: 
#             if i in j:
#                 possible += i
#         # print(i)
#     possible = ''.join(sorted(possible))
#     for i in range(len(word1)): 
#         if possible[i] == word1[i]:
#             # print(word1)
#             # print(possible)
#             return True 
#         else: 
#             return False 
    

# word1 = input("Enter first word: ")
# word2 = input("Enter second word: ")


# print(words(word1, word2))

# def can_form_word(word1, word2):
#     word1 = ''.join(sorted(word1))
#     word2 = ''.join(sorted(word2))
#     i = j = 0 # use two pointers to keep track of words 
#     while i < len(word1) and j < len(word2): 
#         if word1[i] == word2[j]:
#             i += 1
#         j += 1 
#     return i == len(word1)

# word1 = 'TO'
# word2= 'POSITION'

# print(can_form_word(word1, word2))


from collections import Counter

def can_form_word(word1, word2):
    char_count = Counter(word2)
    print(char_count)
    for char in word1:
        print(char)
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    return True

word1 = "TO"
word2 = "POSITION"

print(can_form_word(word1, word2))