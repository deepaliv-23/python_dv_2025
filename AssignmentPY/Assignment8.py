# Assignment 6: Dictionary Program

def main():
    grades = {"John": 85, "Alice": 92, "Bob": 78}

    name = input("Add student name: ")
    score = float(input(f"Grade for {name}: "))
    grades[name] = score

    avg = sum(grades.values()) / len(grades)
    top_student = max(grades, key=grades.get)

    print("Average grade:", avg)
    print("Top performer:", top_student, "with", grades[top_student])

if __name__ == "__main__":
    main()
