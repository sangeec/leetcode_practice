def are_permutations(str1, str2):
    if len(str2) != len(str1):
        return False
    
    ascii_str1 = [0] * 128
    ascii_str2 = [0] * 128

    for ele in str1:
        ascii_str1[ord(ele)] += 1

    for ele in str2:
        ascii_str2[ord(ele)] += 1

    return ascii_str1 == ascii_str2

str1 = input("enter string 1 ")
str2 = input("enter string 2 ")

print(are_permutations(str1, str2))
    