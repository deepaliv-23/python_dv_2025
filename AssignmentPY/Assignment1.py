def remove_duplicates(lst):
    """
    Task 1: Return a new list with duplicates removed,
    preserving the original order.
    """
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


if __name__ == "__main__":
    # Example for Task 1
    sample = [1, 2, 2, 3, 1, 4, 3]
    print(remove_duplicates(sample))  # ➞ [1, 2, 3, 4]
