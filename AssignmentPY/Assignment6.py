# Assignment : Basic Tuple Operations

def main():
    students = ("John", "Alice", "Bob", "Carol", "Dave")
    print("Second student:", students[1])
    print("Is 'Alice' in tuple?", "Alice" in students)

    new_students = ("Eve", "Frank", "Grace")
    combined = students + new_students
    print("All students:", combined)
    print("Total students:", len(combined))

if __name__ == "__main__":
    main()
