class School:
    def __init__(self, name, address, students, teachers, courses):
        self.name = name
        self.address = address
        self.students = students  # a list of dictionaries, each dictionary contains name, age, and grade of a student
        self.teachers = teachers  # a list of dictionaries, each dictionary contains name, subject, and salary of a teacher
        self.courses = courses  # a list of dictionaries, each dictionary contains name, code, and credits of a course

    def add_student(self, name, age, grade):
        student = {"name": name, "age": age, "grade": grade}
        self.students.append(student)
        print(f"Added a new student: {name}, {age} years old, grade {grade}.")

    def remove_student(self, name):
        for student in self.students:
            if student["name"] == name:
                self.students.remove(student)
                print(f"Removed a student: {name}.")
                break
        else:
            print(f"No student with the name {name} found.")

    def update_grade(self, name, grade):
        for student in self.students:
            if student["name"] == name:
                student["grade"] = grade
                print(f"Updated the grade of {name} to {grade}.")
                break
        else:
            print(f"No student with the name {name} found.")

    def add_teacher(self, name, subject, salary):
        teacher = {"name": name, "subject": subject, "salary": salary}
        self.teachers.append(teacher)
        print(f"Added a new teacher: {name}, teaching {subject}, earning {salary}.")

    def remove_teacher(self, name):
        for teacher in self.teachers:
            if teacher["name"] == name:
                self.teachers.remove(teacher)
                print(f"Removed a teacher: {name}.")
                break
        else:
            print(f"No teacher with the name {name} found.")

    def update_salary(self, name, salary):
        for teacher in self.teachers:
            if teacher["name"] == name:
                teacher["salary"] = salary
                print(f"Updated the salary of {name} to {salary}.")
                break
        else:
            print(f"No teacher with the name {name} found.")

    def add_course(self, name, code, credits):
        course = {"name": name, "code": code, "credits": credits}
        self.courses.append(course)
        print(f"Added a new course: {name}, code {code}, worth {credits} credits.")

    def remove_course(self, code):
        for course in self.courses:
            if course["code"] == code:
                self.courses.remove(course)
                print(f"Removed a course: {course['name']}, code {code}.")
                break
        else:
            print(f"No course with the code {code} found.")

    def update_credits(self, code, credits):
        for course in self.courses:
            if course["code"] == code:
                course["credits"] = credits
                print(f"Updated the credits of {course['name']} to {credits}.")
                break
        else:
            print(f"No course with the code {code} found.")

    def print_info(self):
        print(f"School name: {self.name}")
        print(f"School address: {self.address}")
        print(f"Number of students: {len(self.students)}")
        print(f"Number of teachers: {len(self.teachers)}")
        print(f"Number of courses: {len(self.courses)}\n")

        print("Students:")
        for student in self.students:
            print(f"{student['name']}, {student['age']} years old, grade {student['grade']}")

        print("\nTeachers:")
        for teacher in self.teachers:
            print(f"{teacher['name']}, teaching {teacher['subject']}, earning {teacher['salary']}.")

        print("\nCourses:")
        for course in self.courses:
            print(f"{course['name']}, code {course['code']}, worth {course['credits']} credits.\n")


# Create an instance of the School class with some initial data
my_school = School(
    name="Mweiga High School",
    address="Mweiga, Nyeri, Kenya",
    students=[
        {"name": "Alice", "age": 16, "grade": 10},
        {"name": "Bob", "age": 17, "grade": 11},
        {"name": "Charlie", "age": 15, "grade": 9}
    ],
    teachers=[
        {"name": "David", "subject": "Math", "salary": 50000},
        {"name": "Eve", "subject": "English", "salary": 45000},
        {"name": "Frank", "subject": "Science", "salary": 55000}
    ],
    courses=[
        {"name": "Algebra", "code": "MATH101", "credits": 3},
        {"name": "Literature", "code": "ENGL201", "credits": 4},
        {"name": "Biology", "code": "SCIE301", "credits": 5}
    ]
)

# Print the information of the school
my_school.print_info()

# Add a new student
my_school.add_student(name="Grace", age=16, grade=10)

# Remove a student
my_school.remove_student(name="Bob")

# Update the grade of a student
my_school.update_grade(name="Alice", grade=11)

# Add a new teacher
my_school.add_teacher(name="Gina", subject="History", salary=40000)

# Remove a teacher
my_school.remove_teacher(name="Frank")

# Update the salary of a teacher
my_school.update_salary(name="David", salary=60000)

# Add a new course
my_school.add_course(name="Geography", code="HIST401", credits=4)

# Remove a course
my_school.remove_course(code="SCIE301")

# Update the credits of a course
my_school.update_credits(code="ENGL201", credits=5)

# Print the information of the school again
my_school.print_info()
