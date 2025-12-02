FILENAME = "employees.txt"

# Create file if not exists & ensure header
def initialize_file():
    try:
        with open(FILENAME, "x") as f:  # 'x' = create only if not exists
            f.write("id,name,salary\n")
    except FileExistsError:
        pass  # File already exists


def add_employee():
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_salary = input("Enter employee salary: ")

    with open(FILENAME, "a") as f:
        f.write(f"{emp_id},{emp_name},{emp_salary}\n")

    print("Employee added successfully!\n")


def display_employees():
    with open(FILENAME, "r") as f:
        print("\n--- Employee List ---")
        print(f.read())
        print("----------------------\n")


def find_employee_by_id(emp_id):
    with open(FILENAME, "r") as f:
        for line in f.readlines()[1:]:  # skip header
            id, name, salary = line.strip().split(",")
            if id == emp_id:
                print(f"\nEmployee Found:")
                print(f"ID: {id}")
                print(f"Name: {name}")
                print(f"Salary: {salary}\n")
                return
    print("Employee not found.\n")


def update_employee_salary(emp_id, new_salary):
    with open(FILENAME, "r") as f:
        lines = f.readlines()

    updated = False
    with open(FILENAME, "w") as f:
        f.write(lines[0])  # write header back
        for line in lines[1:]:
            id, name, salary = line.strip().split(",")
            if id == emp_id:
                f.write(f"{id},{name},{new_salary}\n")
                updated = True
            else:
                f.write(line)

    if updated:
        print("Salary updated successfully!\n")
    else:
        print("Employee not found.\n")


def delete_employee(emp_id):
    with open(FILENAME, "r") as f:
        lines = f.readlines()

    deleted = False
    with open(FILENAME, "w") as f:
        f.write(lines[0])  # header back
        for line in lines[1:]:
            id, name, salary = line.strip().split(",")
            if id != emp_id:
                f.write(line)
            else:
                deleted = True

    if deleted:
        print("Employee deleted successfully!\n")
    else:
        print("Employee not found.\n")


# --------------------------
# Main Program
# --------------------------

initialize_file()

while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Find Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        emp_id = input("Enter employee ID to find: ")
        find_employee_by_id(emp_id)
    elif choice == "4":
        emp_id = input("Enter employee ID to update salary: ")
        new_salary = input("Enter new salary: ")
        update_employee_salary(emp_id, new_salary)
    elif choice == "5":
        emp_id = input("Enter employee ID to delete: ")
        delete_employee(emp_id)
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.\n")
