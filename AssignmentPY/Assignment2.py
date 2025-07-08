def merge_and_sort(list1, list2):
    """
    Task 2: Merge two lists, remove duplicates,
    and return a sorted ascending list.
    """
    merged = list1 + list2
    unique_sorted = sorted(set(merged))
    return unique_sorted


if __name__ == "__main__":
    # Example for Task 2
    a = [3, 1, 4, 1]
    b = [5, 3, 9, 4]
    print(merge_and_sort(a, b))  # ➞ [1, 3, 4, 5, 9]
