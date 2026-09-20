def find_first(text, pattern):
    if pattern == "":
        return 0

    for start in range(len(text) - len(pattern) + 1):
        match = True

        for offset in range(len(pattern)):
            if text[start + offset] != pattern[offset]:
                match = False
                break

        if match:
            return start

    return -1


print(find_first("abracadabra", "cad"))  # 4
print(find_first("abracadabra", "xyz"))  # -1
