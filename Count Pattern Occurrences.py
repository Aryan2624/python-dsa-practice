def count_occurrences(text, pattern):
    if pattern == "" or len(pattern) > len(text):
        return 0

    count = 0

    for start in range(len(text) - len(pattern) + 1):
        if text[start:start + len(pattern)] == pattern:
            count += 1

    return count


print(count_occurrences("aaaa", "aa"))  # 3

#Time: O((n - m + 1) × m)
