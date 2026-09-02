def linear_search(numbers, target):
    """Return the first matching index, or -1 if not found.

    Time: O(n). Extra space: O(1).
    """
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1


if __name__ == "__main__":
    assert linear_search([4, 7, 2, 9], 2) == 2
    assert linear_search([4, 7, 2, 9], 5) == -1
    assert linear_search([], 2) == -1
    assert linear_search([7, 7, 2], 7) == 0

    print("All 4 tests passed!")
  
