# ============================================================
# Problem 7: Find the Smallest K Elements
# ============================================================

def smallest_k(nums, k):

    if k <= 0:
        return []

    heap = []

    for num in nums:

        heapq.heappush(heap, -num)

        # Keep only k smallest elements
        if len(heap) > k:
            heapq.heappop(heap)

    result = [-num for num in heap]

    result.sort()

    return result


nums7 = [10, 4, 7, 2, 8, 1, 9]
k7 = 3

print("\nProblem 7: Smallest K Elements")
print("Array:", nums7)
print(f"Smallest {k7} elements:", smallest_k(nums7, k7))


# ============================================================
# Problem 8: Find Maximum Element Using Heap
# ============================================================

def maximum_using_heap(nums):

    if not nums:
        return None

    max_heap = [-num for num in nums]

    heapq.heapify(max_heap)

    return -heapq.heappop(max_heap)


nums8 = [12, 5, 19, 3, 25, 8]

print("\nProblem 8: Maximum Using Heap")
print("Array:", nums8)
print("Maximum:", maximum_using_heap(nums8))
