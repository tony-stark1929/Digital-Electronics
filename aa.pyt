import matplotlib.pyplot as plt

# Global list of courses
common_courses = ["Java", "Python", "Full Stack", "Maths", "Physics", "Digital Electronics", "Cyber Security"]

class User:
    def __init__(self, user_id, name, role, password):
        self.user_id = user_id
        self.name = name
        self.role = role
        self.password = password

    def authenticate(self, password):
        return self.password == password

class Student(User):
    def __init__(self, student_id, name, password, courses=None, grades=None, attendance=None):
        super().__init__(student_id, name, "student", password)
        self.courses = courses if courses else [course.lower() for course in common_courses]
        self.grades = grades if grades else {course.lower(): None for course in common_courses}
        self.attendance = attendance if attendance else {course.lower(): 0 for course in common_courses}

    def enroll(self, course):
        course = course.lower()
        if course not in [c.lower() for c in self.courses]:
            self.courses.append(course)
            self.grades[course] = None
            self.attendance[course] = 0
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def assign_grade(self, course, grade):
        course = course.lower()
        if course in [c.lower() for c in self.courses]:
            self.grades[course] = grade
        else:
            print(f"{self.name} is not enrolled in {course}.")

    def mark_attendance(self, course):
        course = course.lower()
        if course in [c.lower() for c in self.courses]:
            self.attendance[course] += 1
        else:
            print(f"{self.name} is not enrolled in {course}.")

    def display_profile(self):
        print(f"\nStudent ID: {self.user_id}\nName: {self.name}\nCourses: {', '.join(self.courses)}")

    def view_marksheet(self):
        print("\nMarksheet:")
        for course, grade in self.grades.items():
            print(f"{course}: {grade if grade is not None else 'No Grade'}")

    def view_progress_report(self):
        if not self.grades:
            print("No grades available for progress report.")
            return

        courses = list(self.grades.keys())
        scores = [self.grades[course] if self.grades[course] is not None else 0 for course in courses]

        plt.figure(figsize=(8, 6))
        plt.bar(courses, scores, color='blue')
        plt.xlabel("Courses")
        plt.ylabel("Scores")
        plt.title("Progress Report")
        plt.show()

class Faculty(User):
    def __init__(self, faculty_id, name, password, courses=None):
        super().__init__(faculty_id, name, "faculty", password)
        self.courses = courses if courses else []

    def assign_course(self, course):
        course = course.lower()
        if course not in [c.lower() for c in self.courses]:
            self.courses.append(course)
            # Add the course to all students' course list
            for student in students:
                student.enroll(course)
        else:
            print(f"{self.name} already teaches {course}.")

    def display_profile(self):
        print(f"\nFaculty ID: {self.user_id}\nName: {self.name}\nCourses: {', '.join(self.courses)}")

    def assign_grades_to_student(self):
        student_id = input("Enter student ID: ")
        student = next((s for s in students if s.user_id == student_id), None)
        if student:
            print(f"Assigning grades for {student.name}")
            for course in student.courses:
                grade = input(f"Enter grade for {course}: ")
                student.assign_grade(course, grade)
        else:
            print("Student not found.")

    def mark_attendance(self):
        student_id = input("Enter student ID: ")
        student = next((s for s in students if s.user_id == student_id), None)
        if student:
            course = input("Enter course: ").lower()
            student.mark_attendance(course)
        else:
            print("Student not found.")

    def view_student_performance(self):
        student_id = input("Enter student ID: ")
        student = next((s for s in students if s.user_id == student_id), None)
        if student:
            student.view_marksheet()
            student.view_progress_report()
        else:
            print("Student not found.")

    def manage_courses(self):
        while True:
            print("\n1. Add Course\n2. Remove Course\n3. Display Courses\n4. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                course = input("Enter new course name: ").lower()
                self.assign_course(course)
            elif choice == '2':
                course = input("Enter course to remove: ").lower()
                if course in [c.lower() for c in self.courses]:
                    self.courses.remove(course)
                    # Remove the course from all students' course list
                    for student in students:
                        if course in [c.lower() for c in student.courses]:
                            student.courses.remove(course)
                            del student.grades[course]
                            del student.attendance[course]
                else:
                    print(f"{course} not found in your courses.")
            elif choice == '3':
                self.display_courses()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please try again.")

    def display_courses(self):
        if not common_courses:
            print("No courses available.")
        else:
            print("Common Courses for All Students:")
            for course in common_courses:
                print(course)

class Admin(User):
    def __init__(self, admin_id, name, password):
        super().__init__(admin_id, name, "admin", password)

    def manage_students(self):
        while True:
            print("\n1. Add Student\n2. Remove Student\n3. Display Students\n4. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.remove_student()
            elif choice == '3':
                display_students()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please try again.")

    def manage_faculty(self):
        while True:
            print("\n1. Add Faculty\n2. Remove Faculty\n3. Display Faculty\n4. Back")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.add_faculty()
            elif choice == '2':
                self.remove_faculty()
            elif choice == '3':
                display_faculty()
            elif choice == '4':
                break
            else:
                print("Invalid choice! Please try again.")

    def add_student(self):
        user_id = input("Enter Student ID: ")
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        student = Student(user_id, name, password)
        students.append(student)
        users.append(student)
        print("Student added successfully!")

    def remove_student(self):
        user_id = input("Enter Student ID to remove: ")
        student = next((s for s in students if s.user_id == user_id), None)
        if student:
            students.remove(student)
            users.remove(student)
            print("Student removed successfully!")
        else:
            print("Student not found.")

    def add_faculty(self):
        user_id = input("Enter Faculty ID: ")
        name = input("Enter Name: ")
        password = input("Enter Password: ")
        faculty = Faculty(user_id, name, password)
        faculties.append(faculty)
        users.append(faculty)
        print("Faculty added successfully!")

    def remove_faculty(self):
        user_id = input("Enter Faculty ID to remove: ")
        faculty = next((f for f in faculties if f.user_id == user_id), None)
        if faculty:
            faculties.remove(faculty)
            users.remove(faculty)
            print("Faculty removed successfully!")
        else:
            print("Faculty not found.")

def display_students():
    if not students:
        print("No students registered yet.")
    else:
        for student in students:
            student.display_profile()

def display_faculty():
    if not faculties:
        print("No faculty members registered yet.")
    else:
        for faculty in faculties:
            faculty.display_profile()

def login():
    user_id = input("Enter ID: ")
    password = input("Enter Password: ")
    
    for user in users:
        if user.user_id == user_id and user.authenticate(password):
            return user
    print("Invalid credentials!")
    return None

def student_menu(student):
    while True:
        print("\n1. Display Profile\n2. View Marks\n3. View Marks Chart\n4. Logout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student.display_profile()
        elif choice == '2':
            student.view_marksheet()
        elif choice == '3':
            student.view_progress_report()
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please try again.")

def faculty_menu(faculty):
    while True:
        print("\nFaculty Menu:\n1. View Profile\n2. Assign Grades to Students\n3. Mark Attendance\n4. View Student Performance Reports\n5. Manage Courses\n6. Logout")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            faculty.display_profile()
        elif choice == '2':
            faculty.assign_grades_to_student()
        elif choice == '3':
            faculty.mark_attendance()
        elif choice == '4':
            faculty.view_student_performance()
        elif choice == '5':
            faculty.manage_courses()
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

def register():
    print("\nRegistration Form")
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    role = input("Enter Role (student/faculty/admin): ").lower()
    
    if role == "student":
        user = Student(user_id, name, password)
        students.append(user)
    elif role == "faculty":
        user = Faculty(user_id, name, password)
        faculties.append(user)
    elif role == "admin":
        user = Admin(user_id, name, password)
        admins.append(user)
    else:
        print("Invalid role! Registration failed.")
        return
    
    users.append(user)
    print("Registration successful!")

students = []
faculties = []
admins = [Admin("admin1", "Admin", "admin")]
users = students + faculties + admins

# Predefined student and faculty for testing
students.append(Student("s1", "John Doe", "student123", courses=["Python", "FSD","DE","Java"], grades={"Python": 85, "FSD": 90, "DE":76, "Java":87}))
faculties.append(Faculty("f1", "Smith", "faculty123"))
users = students + faculties + admins  # Update user list

def main():
    while True:
        print("\n1. Login\n2. Register\n3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user = login()
            if user:
                if user.role == "student":
                    print(f"Welcome {user.name}, you are logged in as a student.")
                    student_menu(user)
                elif user.role == "faculty":
                    print(f"Welcome {user.name}, you are logged in as faculty.")
                    faculty_menu(user)
                elif user.role == "admin":
                    print(f"Welcome {user.name}, you are logged in as an admin.")
                    while True:
                        print("\nAdmin Panel:\n1. Manage Students\n2. Manage Faculty\n3. Logout")
                        admin_choice = input("Enter your choice: ")
                        if admin_choice == '1':
                            user.manage_students()
                        elif admin_choice == '2':
                            user.manage_faculty()
                        elif admin_choice == '3':
                            break
                        else:
                            print("Invalid choice! Please try again.")
        elif choice == '2':
            register()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()