students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))

    student = {
        "roll": roll,
        "name": name,
        "marks": marks
    }

    students.append(student)
    print("Student Added Successfully!\n")

def view_students():

    if len(students) == 0:
        print("No student records found.\n")
        return

    print("\n----- Student Records -----")

    for student in students:
        print(f"Roll No : {student['roll']}")
        print(f"Name    : {student['name']}")
        print(f"Marks   : {student['marks']}")
        print("--------------------------")

def search_student():

    roll = input("Enter Roll Number to Search: ")

    for student in students:
        if student["roll"] == roll:
            print("\nStudent Found")
            print(f"Name : {student['name']}")
            print(f"Marks: {student['marks']}\n")
            return

    print("Student Not Found!\n")

def update_student():

    roll = input("Enter Roll Number to Update: ")

    for student in students:

        if student["roll"] == roll:

            new_name = input("Enter New Name: ")
            new_marks = float(input("Enter New Marks: "))

            student["name"] = new_name
            student["marks"] = new_marks

            print("Record Updated Successfully!\n")
            return

    print("Student Not Found!\n")

def delete_student():

    roll = input("Enter Roll Number to Delete: ")

    for student in students:

        if student["roll"] == roll:

            students.remove(student)

            print("Student Deleted Successfully!\n")
            return

    print("Student Not 
def class_report():

    if len(students) == 0:
        print("No Records Available.\n")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    highest = students[0]

    for student in students:
        if student["marks"] > highest["marks"]:
            highest = student

    print("\n----- Class Report -----")
    print("Total Students :", len(students))
    print("Average Marks  :", round(average, 2))
    print("Top Student    :", highest["name"])
    print("Highest Marks  :", highest["marks"])
    print("------------------------\n")


# Main Program
while True:

    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Report")
    print("7. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        class_report()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.\n")
