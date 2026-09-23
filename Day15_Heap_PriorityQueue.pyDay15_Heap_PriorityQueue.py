# Day 15 - Heaps & Priority Queues
# Python DSA Practice
# Author: Aryan Dubey

import heapq
from collections import Counter


# ============================================================
# Problem 1: Min Heap
# ============================================================

def min_heap_sort(nums):
    heap = []

    # Insert all elements into the heap
    for num in nums:
        heapq.heappush(heap, num)

    result = []

    # Remove elements in ascending order
    while heap:
        result.append(heapq.heappop(heap))

    return result


nums1 = [7, 2, 9, 1, 5, 3]

print("Problem 1: Min Heap")
print("Original:", nums1)
print("Sorted using Min Heap:", min_heap_sort(nums1))


# ============================================================
# Problem 2: Kth Largest Element
# ============================================================

def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        # Keep only k largest elements
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


nums2 = [3, 2, 1, 5, 6, 4]
k2 = 2

print("\nProblem 2: Kth Largest Element")
print("Array:", nums2)
print(f"{k2}nd largest:", kth_largest(nums2, k2))


# ============================================================
# Problem 3: Top K Frequent Elements
# ============================================================

def top_k_frequent(nums, k):
    frequency = Counter(nums)

    heap = []

    for num, count in frequency.items():

        heapq.heappush(heap, (count, num))

        # Keep only k most frequent elements
        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    while heap:
        count, num = heapq.heappop(heap)
        result.append(num)

    result.reverse()

    return result


nums3 = [1, 1, 1, 2, 2, 3]
k3 = 2

print("\nProblem 3: Top K Frequent Elements")
print("Array:", nums3)
print(f"Top {k3} frequent elements:", top_k_frequent(nums3, k3))


# ============================================================
# Problem 4: Merge K Sorted Lists
# ============================================================

def merge_k_sorted_lists(lists):
    heap = []

    # Put first element of every list into heap
    for list_index, current_list in enumerate(lists):

        if current_list:
            heapq.heappush(
                heap,
                (current_list[0], list_index, 0)
            )

    result = []

    while heap:

        value, list_index, element_index = heapq.heappop(heap)

        result.append(value)

        next_index = element_index + 1

        # Add next element from the same list
        if next_index < len(lists[list_index]):

            next_value = lists[list_index][next_index]

            heapq.heappush(
                heap,
                (next_value, list_index, next_index)
            )

    return result


lists4 = [
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]

print("\nProblem 4: Merge K Sorted Lists")
print("Lists:", lists4)
print("Merged:", merge_k_sorted_lists(lists4))


# ============================================================
# Problem 5: K Closest Numbers
# ============================================================

def k_closest_numbers(nums, target, k):

    # Max heap using negative distance
    heap = []

    for num in nums:

        distance = abs(num - target)

        heapq.heappush(
            heap,
            (-distance, num)
        )

        # Keep only k closest numbers
        if len(heap) > k:
            heapq.heappop(heap)

    result = []

    while heap:
        distance, num = heapq.heappop(heap)
        result.append(num)

    return result


nums5 = [1, 3, 5, 7, 9, 11]
target5 = 6
k5 = 3

print("\nProblem 5: K Closest Numbers")
print("Array:", nums5)
print("Target:", target5)
print(f"{k5} closest numbers:", k_closest_numbers(
    nums5,
    target5,
    k5
))


# ============================================================
# Problem 6: Task Scheduler
# ============================================================

def least_interval(tasks, n):

    frequency = Counter(tasks)

    # Max heap using negative frequencies
    max_heap = [
        -count for count in frequency.values()
    ]

    heapq.heapify(max_heap)

    time = 0

    while max_heap:

        temporary = []
        tasks_executed = 0

        # One scheduling cycle
        for _ in range(n + 1):

            if max_heap:

                count = -heapq.heappop(max_heap)

                count -= 1

                tasks_executed += 1

                if count > 0:
                    temporary.append(-count)

            time += 1

            # No remaining tasks
            if not max_heap and not temporary:
                break

        # Put unfinished tasks back
        for count in temporary:
            heapq.heappush(max_heap, count)

    return time


tasks6 = ["A", "A", "A", "B", "B", "C"]
n6 = 2

print("\nProblem 6: Task Scheduler")
print("Tasks:", tasks6)
print("Cooldown:", n6)
print("Minimum intervals:", least_interval(tasks6, n6))


