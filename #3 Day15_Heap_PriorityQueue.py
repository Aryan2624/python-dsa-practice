# ============================================================
# Problem 9: Kth Smallest Element
# ============================================================

def kth_smallest(nums, k):

    heap = nums.copy()

    heapq.heapify(heap)

    for _ in range(k - 1):
        heapq.heappop(heap)

    return heap[0]


nums9 = [7, 10, 4, 3, 20, 15]
k9 = 3

print("\nProblem 9: Kth Smallest Element")
print("Array:", nums9)
print(f"{k9}rd smallest:", kth_smallest(nums9, k9))


# ============================================================
# Problem 10: Running Median
# ============================================================

def running_median(nums):

    # Max heap for left half
    left = []

    # Min heap for right half
    right = []

    medians = []

    for num in nums:

        # Add to left max heap
        heapq.heappush(left, -num)

        # Move largest from left to right
        heapq.heappush(
            right,
            -heapq.heappop(left)
        )

        # Balance heaps
        if len(right) > len(left):
            heapq.heappush(
                left,
                -heapq.heappop(right)
            )

        # Calculate median
        if len(left) > len(right):
            median = -left[0]

        else:
            median = (-left[0] + right[0]) / 2

        medians.append(median)

    return medians


nums10 = [5, 15, 1, 3]

print("\nProblem 10: Running Median")
print("Array:", nums10)
print("Running medians:", running_median(nums10))
