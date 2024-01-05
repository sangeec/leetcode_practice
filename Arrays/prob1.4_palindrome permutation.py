def is_alphanumeric(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9')

def is_palindrome_permutation(str1):
    char_count = [0] * 128  

    for char in str1:
        if is_alphanumeric(char): 
            char_count[ord(char.lower())] += 1

    count = 0
    for key in range(len(char_count)):
        count += char_count[key] % 2

    return count <= 1

str1 = input("Enter a string ")
if is_palindrome_permutation(str1):
    print(f"{str1} is a permutation of a palindrome.")
else:
    print(f"{str1} is not a permutation of a palindrome.")
