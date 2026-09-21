#1️⃣ Valid Palindrome — Two Pointer Approach

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))

#OUTPUT
#True
#False

#Complexity: O(n) time, O(1) space

##2️⃣ Two Sum II — Sorted Array

def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]

        if current_sum < target:
            left += 1
        else:
            right -= 1

    return []


numbers = [2, 7, 11, 15]
target = 9

print(two_sum_sorted(numbers, target))

#OUTPUT :- [1, 2]
#Complexity: O(n) time, O(1) space

##3️⃣ Move Zeroes

def move_zeroes(nums):
    insert_position = 0

    for num in nums:
        if num != 0:
            nums[insert_position] = num
            insert_position += 1

    while insert_position < len(nums):
        nums[insert_position] = 0
        insert_position += 1


nums = [0, 1, 0, 3, 12]

move_zeroes(nums)

print(nums)

#Output: [1, 3, 12, 0, 0]
#Complexity: O(n) time, O(1) space
