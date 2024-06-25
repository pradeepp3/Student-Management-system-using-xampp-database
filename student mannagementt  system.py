class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name, age, grade):
        if student_id in self.students:
            print("Student ID already exists.")
            return
        student = Student(student_id, name, age, grade)
        self.students[student_id] = student
        print(f"Student {name} added successfully.")

    def delete_student(self, student_id):
        if student_id not in self.students:
            print("Student ID not found.")
            return
        del self.students[student_id]
        print(f"Student ID {student_id} deleted successfully.")

    def update_student(self, student_id, name=None, age=None, grade=None):
        if student_id not in self.students:
            print("Student ID not found.")
            return
        student = self.students[student_id]
        if name:
            student.name = name
        if age:
            student.age = age
        if grade:
            student.grade = grade
        print(f"Student ID {student_id} updated successfully.")

    def view_student(self, student_id):
        if student_id not in self.students:
            print("Student ID not found.")
            return
        print(self.students[student_id])

    def view_all_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students.values():
            print(student)

def main():
    sms = StudentManagementSystem()
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. View Student")
        print("5. View All Students")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            grade = input("Enter Grade: ")
            sms.add_student(student_id, name, age, grade)
        
        elif choice == '2':
            student_id = input("Enter Student ID to delete: ")
            sms.delete_student(student_id)
        
        elif choice == '3':
            student_id = input("Enter Student ID to update: ")
            name = input("Enter Name (or leave blank to keep current): ")
            age = input("Enter Age (or leave blank to keep current): ")
            grade = input("Enter Grade (or leave blank to keep current): ")
            sms.update_student(student_id, name=name if name else None, age=age if age else None, grade=grade if grade else None)
        
        elif choice == '4':
            student_id = input("Enter Student ID to view: ")
            sms.view_student(student_id)
        
        elif choice == '5':
            sms.view_all_students()
        
        elif choice == '6':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
   
