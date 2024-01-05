def isRotation(str1, str2):
    if len(str1) != len(str2):
        return False
    str_joined = str1 + str2
    return isSubString(str_joined, str2)

def isSubString(s1, s2):
    return s2 in s1

s1 = "waterbottle"
s2 = "erbottlewat"

if isRotation(s1, s2):
    print(f"{s2} is a rotation of {s1}.")
else:
    print(f"{s2} is not a rotation of {s1}.")