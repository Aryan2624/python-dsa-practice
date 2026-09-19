def subsets(nums):
    result = []
    current = []

    def backtrack(start):
        result.append(current.copy())

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1)
            current.pop()

    backtrack(0)
    return result


print(subsets([1, 2, 3]))


#Expected output:
#[[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
