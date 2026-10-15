class Student:

    # Constructor
    def __init__(self):
        print("Constructor called")

        self.name = input("Enter Student Name: ")
        self.roll_no = input("Enter Roll Number: ")
        self.fy = float(input("Enter FY CGPA: "))
        self.sy = float(input("Enter SY CGPA: "))
        self.ty = float(input("Enter TY CGPA: "))
        self.btech = float(input("Enter B.Tech CGPA: "))

    # Display student information
    def display_student_info(self):
        print("\n----- STUDENT INFORMATION -----")
        print("Student Name :", self.name)
        print("Roll Number  :", self.roll_no)
        print("FY CGPA      :", self.fy)
        print("SY CGPA      :", self.sy)
        print("TY CGPA      :", self.ty)
        print("B.Tech CGPA  :", self.btech)


    # Destructor
    def __del__(self):
        print("\nDestructor called")
        print("Student object deleted")


# Creating object
student = Student()

# Display information
student.display_student_info()