from storage import load_students, save_students

students = load_students()

def generate_id():
    if not students:
        return 1
    return max(student["id"] for student in students) + 1


# Add Student

def add_student():
    name = input("Name: ")

    while True:
          try:
           age = int(input("Age: "))
           break
          except ValueError:
            print("Please enter a valid integer.")

    field = input("Field of study: ")

    student = {
        "id": generate_id(),
        "name": name,
        "age": age,
        "field": field
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")

# View Students

def view_students():
    if not students:
        print("No students found.")
        return
    
    for student in students:
        print(
            f'ID: {student["id"]} | '
            f'{student["name"]}, '
            f'{student["age"]} yrs, '
            f'{student["field"]}'
        )

# Search Student

def search_student():
    query = input("Enter name to search: ").lower()
   
    for student in students:
        if student["name"].lower() == query:
         print(
            f'ID: {student["id"]} | '
            f'{student["name"]}, '
            f'{student["age"]} yrs, '
            f'{student["field"]}'
         )
         return
         
        
    print("Student not found.")

# Update Student

def update_student():
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            print("Type new value or press enter to keep one.")

         # Handling name
            new_name = input("Name: ")
            if new_name != "":
                student["name"] = new_name

         # Handling age
            while True:
              new_age_str = input("Enter new age: ")
              if new_age_str == "":
                break
              try:
                  student["age"] = int(new_age_str)
                  break
              except ValueError:
                  print("Please enter a valid integer.")

         # Handling field
            new_field = input("Field of study: ")
            if new_field != "":
                student["field"] = new_field
            
            save_students(students)
            print("Student information updated.")
            return
    print("Student not found.")

# Delete Student
def get_valid_id(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def delete_student():
    student_id = get_valid_id("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted.")
            return
    print("Student not found.")


# Menu Loop 

while True:
   print("\nStudent Record Manager")
   print("1. Add a Student")
   print("2. Search for a Student")
   print("3. View Students")
   print("4. Update a Student")
   print("5. Delete a Student")
   print("6. Exit")

   choice = input("Choose an option: ")

   if choice == "1":
       add_student()
   elif choice == "2":
       search_student()
   elif choice == "3":
       view_students()
   elif choice == "4":
       update_student()
   elif choice == "5":
       delete_student()
   elif choice == "6":
       print("Goodbye.")
       break
   else:
       print("Invalid choice.")

