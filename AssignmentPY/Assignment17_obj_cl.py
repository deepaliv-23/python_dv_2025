class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # Each course maps to a dict with 'grade' and 'credits'
        self.courses = {}

    def enroll(self, course_name):
        if course_name not in self.courses:
            self.courses[course_name] = {'grade': None, 'credits': 0}
        else:
            print(f"[Warning] Already enrolled in {course_name}")

    def update_grade(self, course_name, grade):
        if course_name in self.courses:
            self.courses[course_name]['grade'] = grade
        else:
            raise ValueError(f"Course '{course_name}' not found. Enroll first.")

    def add_credits(self, course_name, credits):
        if course_name in self.courses:
            self.courses[course_name]['credits'] = credits
        else:
            raise ValueError(f"Course '{course_name}' not found. Enroll first.")

    def calculate_gpa(self):
        total, count = 0.0, 0
        for info in self.courses.values():
            if info['grade'] is not None:
                total += info['grade']
                count += 1
        return total / count if count else 0.0

    def calculate_weighted_gpa(self):
        weighted_sum, total_credits = 0.0, 0
        for info in self.courses.values():
            if info['grade'] is not None and info['credits'] > 0:
                weighted_sum += info['grade'] * info['credits']
                total_credits += info['credits']
        return weighted_sum / total_credits if total_credits else 0.0

    def get_highest_grade(self):
        best = (None, float('-inf'))
        for course, info in self.courses.items():
            g = info['grade']
            if g is not None and g > best[1]:
                best = (course, g)
        return best if best[0] is not None else (None, None)

    def display_info(self):
        print(self.__str__())

    def __str__(self):
        lines = [f"Student: {self.name} (ID: {self.student_id})"]
        for course, info in self.courses.items():
            lines.append(f"  {course}: grade={info['grade']}, credits={info['credits']}")
        lines.append(f"Unweighted GPA: {self.calculate_gpa():.2f}")
        lines.append(f"Weighted GPA: {self.calculate_weighted_gpa():.2f}")
        return "\n".join(lines)


if __name__ == "__main__":
    # ---- Demonstration ----

    # Student 1
    s1 = Student("Alice", "A001")
    s1.enroll("Math")
    s1.add_credits("Math", 4)
    s1.update_grade("Math", 3.7)

    s1.enroll("History")
    s1.add_credits("History", 3)
    s1.update_grade("History", 3.3)

    print(s1)
    best_course, best_grade = s1.get_highest_grade()
    print(f"Alice's highest grade: {best_grade} in {best_course}\n")

    # Student 2
    s2 = Student("Bob", "B123")
    s2.enroll("Chemistry")
    s2.add_credits("Chemistry", 3)
    s2.update_grade("Chemistry", 3.0)

    s2.enroll("Art")
    s2.add_credits("Art", 2)
    s2.update_grade("Art", 4.0)

    s2.enroll("Physics")
    s2.add_credits("Physics", 4)
    # No grade yet for Physics

    s2.display_info()
    best_course2, best_grade2 = s2.get_highest_grade()
    print(f"\nBob's highest grade: {best_grade2} in {best_course2}")
