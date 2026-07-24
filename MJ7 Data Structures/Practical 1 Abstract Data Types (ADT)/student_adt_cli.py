class Student:
    def __init__(self, roll, name, age):
        self.roll = roll
        self.name = name
        self.age = age

students = []

while True:
    print("\n===== Student ADT Menu =====")
    print("1. Create Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Display Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        students.append(Student(roll, name, age))
        print("Student Added Successfully.")

    elif choice == "2":
        roll = int(input("Enter Roll No to Update: "))
        found = False
        for s in students:
            if s.roll == roll:
                s.name = input("Enter New Name: ")
                s.age = int(input("Enter New Age: "))
                print("Student Updated Successfully.")
                found = True
                break
        if not found:
            print("Student Not Found.")

    elif choice == "3":
        roll = int(input("Enter Roll No to Delete: "))
        found = False
        for s in students:
            if s.roll == roll:
                students.remove(s)
                print("Student Deleted Successfully.")
                found = True
                break
        if not found:
            print("Student Not Found.")

    elif choice == "4":
        if len(students) == 0:
            print("No Students Available.")
        else:
            print("\nStudent Records")
            for s in students:
                print("Roll:", s.roll, "| Name:", s.name, "| Age:", s.age)

    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")