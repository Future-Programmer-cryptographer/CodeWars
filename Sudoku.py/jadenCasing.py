def to_jaden_case(string):
    # start of each word char, want to take the first and .upper() that 
    return ' '.join(i.capitalize() for i in string.split(" "))
    # for i in string.split(" "):
    #     return ''.join(i.capitalize())

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))