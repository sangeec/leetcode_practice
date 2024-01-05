def is_character_unique(input_string):
    if len(input_string) > 128:
        return False

    char_set = [False] * 128
    # print(char_set)

    for ele in input_string:
        ascii_val_ele = ord(ele)
        # ord function in Python is used to get the Unicode code point of a given character.
        print(ascii_val_ele)
        if char_set[ascii_val_ele]:
            return False
        char_set[ascii_val_ele] = True
    return True

user_input = input("Enter an input string ")


if is_character_unique(user_input):
    print("Characters are unique")
else:
    print("Characters are not unique")
