def compress(str1):
    compressed_str = ""
    count = 1

    for i in range(1, len(str1)):
        if str1[i] == str1[i-1]:
            count += 1
        else:
            compressed_str += str1[i-1] + str(count)
            count = 1
    compressed_str += str1[i-1] + str(count)
    return compressed_str

    # return compressed_str if len(compressed_str) < len(str1) else str1

original_string = "abcd"
compressed_result = compress(original_string)
print(f"Original String: {original_string}")
print(f"Compressed Result: {compressed_result}")