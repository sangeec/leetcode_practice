def one_edit_away(first, second):
    if abs(len(first) - len(second)) > 1:
        return False

    sl, s2 = (first, second) if len(first) < len(second) else (second, first)

    indexl = 0
    index2 = 0
    found_difference = False

    while index2 < len(s2) and indexl < len(sl):
        if sl[indexl] != s2[index2]:
            if found_difference:
                return False
            found_difference = True

            if len(sl) == len(s2):
                indexl += 1
        else:
            indexl += 1
        index2 += 1

    return True


str1 = input("enter string 1 ")
str2 = input("enter string 2 ")
print(one_edit_away(str1, str2))
