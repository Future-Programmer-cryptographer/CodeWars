# import math 

# def count(digits):
#     total = [] 
#     for i in range(0,digits):
#         enter = int(input('Enter digit: '))
#         total.append(enter)
#     total.sort()
#     print(total)
#     output = [] 
#     for i in set(total):
#         output.append((total.count(i)))
#     print(f'Highest frequency: {max(output)}')
    
#     # counter = 0 
#     # for i in range(0,len(total)+1):
#     #     if total[i] == total[i+1] and total[i+1] != len(total)+1:
#     #         counter += 1 
#     #     elif total[i] == total[i-1]:
#     #         counter += 1 
#     #     else: 
#     #         pass 
#     # print(counter)
# digits = int(input('How many digits would you like to enter?: '))
# count(digits)


# # have the user enter these many digits, save them to a 


def count_digits():
    num_digits = int(input('How many digits would you like to enter?: '))
    digits = []
    for i in range(num_digits):
        digit = int(input('Enter digit: '))
        digits.append(digit)

    digit_counts = {}
    for digit in digits:
        if digit in digit_counts:
            digit_counts[digit] += 1
        else:
            digit_counts[digit] = 1

    print(digit_counts)

    max_count = max(digit_counts.values())
    max_digits = []
    for digit, count in digit_counts.items():
        if count == max_count:
            max_digits.append(digit)

    if len(max_digits) == 1:
        print(f'The most frequently entered digit was {max_digits[0]} with a frequency of {max_count}')
    else:
        print('Data was multimodal')

count_digits()
