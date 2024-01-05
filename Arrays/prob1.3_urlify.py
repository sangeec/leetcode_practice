def replaceSpaces(str1):

    str1 = str1.strip()
    print(str1)

    str1 = str1.replace(" ", "%20")
    print(str1)
    # for i in range(len(str1)):
    #     if str1[i] == ' ':
    #         str1 = str1.replace(str1[i], "%20")
    # print(str1)

str1 = input("enter a string ")

replaceSpaces(str1)