emp_file = open("employees.txt", "w")
emp_file.write("id, name, salary\n")
emp_file.close()

def add_employee():
    emp_file = open("employees.txt", "a")
    emp_id = input("Enter employee ID: ")
    emp_name = input("Enter employee name: ")
    emp_salary = input("Enter employee salary: ")
    emp_file.write(f"{emp_id}, {emp_name}, {emp_salary}\n")
    emp_file.close()

def display_employees():
    emp_file = open("employees.txt", "r")
    print(emp_file.read())
    emp_file.close()

def find_employee_by_id(emp_id):
    emp_file = open("employees.txt", "r")
    for line in emp_file.readlines()[1:]:  # Skip header
        id, name, salary = line.strip().split(", ")
        if id == emp_id:
            print(f"Employee Found: ID={id}, Name={name}, Salary={salary}")
            emp_file.close()
            return
    print("Employee not found.")
    emp_file.close()

def update_employee_salary(emp_id, new_salary):
    emp_file = open("employees.txt", "r")
    lines = emp_file.readlines()
    emp_file.close()
    
    with open("employees.txt", "w") as emp_file:
        for line in lines:
            id, name, salary = line.strip().split(", ")
            if id == emp_id:
                emp_file.write(f"{id}, {name}, {new_salary}\n")
            else:
                emp_file.write(line)

def delete_employee(emp_id):
    emp_file = open("employees.txt", "r")
    lines = emp_file.readlines()
    emp_file.close()
    
    with open("employees.txt", "w") as emp_file:
        for line in lines:
            id, name, salary = line.strip().split(", ")
            if id != emp_id:
                emp_file.write(line)

while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Find Employee by ID")
    print("4. Update Employee Salary")
    print("5. Delete Employee")
    print("6. Exit")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        add_employee()
    elif choice == '2':
        display_employees()
    elif choice == '3':
        emp_id = input("Enter employee ID to find: ")
        find_employee_by_id(emp_id)
    elif choice == '4':
        emp_id = input("Enter employee ID to update salary: ")
        new_salary = input("Enter new salary: ")
        update_employee_salary(emp_id, new_salary)
    elif choice == '5':
        emp_id = input("Enter employee ID to delete: ")
        delete_employee(emp_id)
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")  

