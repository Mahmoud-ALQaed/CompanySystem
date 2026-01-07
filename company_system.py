from employee import Worker, Manager
from department import Department
from utils import pause, validate_positive_int, validate_name, validate_age, validate_bonus
from enums import EmployeeType



class CompanySystem:
    def __init__(self):
        self._employees = {}
        self._departments = {}

    @property
    def employees(self):
        return self._employees

    @property
    def departments(self):
        return self._departments

    # ---------------- ADD DEPARTMENT ----------------
    def add_department(self):
        dept_id = input("Enter department ID (A positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid department ID")
            pause()
            return

        dept_id = int(dept_id)
        if dept_id in self._departments:
            print("Department ID already exists")
            pause()
            return

        name = input("Enter department name (This field cannot be empty): ")
        if not validate_name(name):
            print("Invalid department name")
            pause()
            return

        self._departments[dept_id] = Department(dept_id, name)
        print("Department added successfully")
        pause()

    # ---------------- ADD EMPLOYEE ----------------
    def add_employee(self, emp_type):
        emp_id = input("Enter employee ID (A positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id in self._employees:
            print("Employee ID already exists")
            pause()
            return

        name = input("Enter employee name (This field cannot be empty): ")
        if not validate_name(name):
            print("Invalid employee name")
            pause()
            return

        age = input("Enter age (Users under 18 cannot enter): ")
        
        if not validate_age(age):
            print("Invalid employee age")
            pause()
            return
        
        age = int(age)
        
        salary = input("Enter salary (A salary of 0 cannot be entered): ")

        if not validate_positive_int(salary):
            print("Invalid employee salary")
            pause()
            return
        
        salary = int(salary)

        if emp_type == EmployeeType.WORKER:
            self._employees[emp_id] = Worker(emp_id, name, age, salary)
        else:
            bonus = input("Enter bonus: ")
            if not validate_bonus(bonus):
                print("Invalid employee bonus")
                pause()
                return
            bonus = int(bonus)
            self._employees[emp_id] = Manager(emp_id, name, age, salary, bonus)

        print("Employee added successfully")
        pause()

    # ---------------- SHOW EMPLOYEE ----------------
    def show_employee(self):
        if not self._employees:
            print("No employees to display")
            pause()
            return

        emp_id = input("Enter employee ID: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id not in self._employees:
            print("Employee not found")
            pause()
            return

        self._employees[emp_id].display()
        pause()

    # ---------------- SHOW ALL EMPLOYEES ----------------
    def show_all_employees(self):
        if not self._employees:
            print("No employees to display")
            pause()
            return

        for emp in self._employees.values():
            emp.display()
            print("-" * 30)
        pause()

    # ---------------- SHOW DEPARTMENTS WITH EMPLOYEES ----------------
    def show_departments_with_employees(self):
        if not self._departments:
            print("No departments to display")
            pause()
            return

        for dept in self._departments.values():
            print(f"Department ID: {dept.id} | Name: {dept.name}")
            if dept.employees:
                for emp in dept.employees:
                    print("  --------------------")
                    emp.display()
            else:
                print("  No employees")
            print("-" * 30)
        pause()

    # ---------------- CALCULATE SALARY ----------------
    def calculate_salary_for_employee(self):
        if not self._employees:
            print("No employees to display")
            pause()
            return

        emp_id = input("Enter employee ID to calculate salary: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id not in self._employees:
            print("Employee not found")
            pause()
            return

        emp = self._employees[emp_id]
        print(f"Employee {emp.name} (ID: {emp.id}) final salary: {emp.calculate_salary()}")
        pause()

    # ---------------- ASSIGN EMPLOYEE ----------------
    def assign_employee(self):
        if not self._employees:
            print("No employees available")
            pause()
            return

        if not self._departments:
            print("No departments available")
            pause()
            return

        emp_id = input("Enter employee ID: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id not in self._employees:
            print("Employee not found")
            pause()
            return

        for d in self._departments.values():
            if self._employees[emp_id] in d.employees:
                print("Employee already assigned to a department")
                pause()
                return

        dept_id = input("Enter department ID: ")
        if not validate_positive_int(dept_id):
            print("Invalid department ID")
            pause()
            return

        dept_id = int(dept_id)
        if dept_id not in self._departments:
            print("Department not found")
            pause()
            return

        self._departments[dept_id].add_employee(self._employees[emp_id])
        print("Employee assigned successfully")
        pause()

    # ---------------- REMOVE EMPLOYEE FROM DEPARTMENT ----------------
    def remove_from_department(self):
        valid_departments = [d for d in self._departments.values() if d.employees]
        if not valid_departments:
            print("No departments with employees")
            pause()
            return

        dept_id = input("Enter department ID: ")
        if not validate_positive_int(dept_id):
            print("Invalid department ID")
            pause()
            return

        dept_id = int(dept_id)
        if dept_id not in self._departments:
            print("The entered ID is unavailable")
            pause()
            return

        if not self._departments[dept_id].employees:
            print("The ID is empty")
            pause()
            return

        emp_id = input("Enter employee ID: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        emp = self._employees.get(emp_id)
        if not emp or emp not in self._departments[dept_id].employees:
            print("Employee not found in this department")
            pause()
            return

        self._departments[dept_id].remove_employee(emp)
        print("Employee removed from department successfully")
        pause()

    # ---------------- TRANSFER EMPLOYEE ----------------
    def transfer_employee(self):
        if len(self._departments) < 2:
            print("Not enough departments")
            pause()
            return

        valid_departments = [d for d in self._departments.values() if d.employees]
        if not valid_departments:
            print("No departments with employees")
            pause()
            return

        source_id = input("Enter source department ID: ")
        if not validate_positive_int(source_id):
            print("Invalid department ID")
            pause()
            return

        source_id = int(source_id)
        if source_id not in self._departments:
            print("The ID is unavailable")
            pause()
            return

        if not self._departments[source_id].employees:
            print("The ID is empty")
            pause()
            return

        emp_id = input("Enter employee ID: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        emp = self._employees.get(emp_id)
        if not emp or emp not in self._departments[source_id].employees:
            print("Employee not found in source department")
            pause()
            return

        target_id = input("Enter target department ID: ")
        if not validate_positive_int(target_id):
            print("Invalid department ID")
            pause()
            return

        target_id = int(target_id)
        if target_id == source_id:
            print("Transfer failed (interface field is the same as the start field)")
            pause()
            return

        if target_id not in self._departments:
            print("Transfer failed (the entered ID does not exist)")
            pause()
            return

        self._departments[source_id].remove_employee(emp)
        self._departments[target_id].add_employee(emp)
        print("Employee transferred successfully")
        pause()

    # ---------------- DELETE EMPLOYEE ----------------
    def delete_employee(self):
        if not self._employees:
            print("No employees available")
            pause()
            return

        emp_id = input("Enter employee ID: ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id not in self._employees:
            print("Employee not found")
            pause()
            return

        emp = self._employees[emp_id]
        for d in self._departments.values():
            if emp in d.employees:
                d.remove_employee(emp)

        del self._employees[emp_id]
        print("Employee deleted successfully")
        pause()

    # ---------------- DELETE DEPARTMENT ----------------
    def delete_department(self):
        empty_departments = [d for d in self._departments.values() if not d.employees]
        if not empty_departments:
            print("No empty departments available")
            pause()
            return

        dept_id = input("Enter department ID: ")
        if not validate_positive_int(dept_id):
            print("Invalid department ID")
            pause()
            return

        dept_id = int(dept_id)
        if dept_id not in self._departments:
            print("The entered ID is unavailable")
            pause()
            return

        if self._departments[dept_id].employees:
            print("The id is not empty")
            pause()
            return

        del self._departments[dept_id]
        print("Department deleted successfully")
        pause()

  # ---------------- EDIT EMPLOYEE ----------------
    def edit_employee(self):
        if not self._employees:
            print("No employees available")
            pause()
            return

        emp_id = input("Enter employee ID (A positive numerical value must be entered): ")
        if not validate_positive_int(emp_id):
            print("Invalid employee ID")
            pause()
            return

        emp_id = int(emp_id)
        if emp_id not in self._employees:
            print("Employee not found")
            pause()
            return
        
        emp_id = self._employees[emp_id]

        name = input("Enter employee name (This field cannot be empty): ")
        if not validate_name(name):
            print("Invalid employee name")
            pause()
            return
        
        emp_id.name = name
        
        age = input("Enter age (Users under 18 cannot enter): ")
        
        if not validate_age(age):
            print("Invalid employee age")
            pause()
            return
        
        emp_id.age = int(age)
        
        salary = input("Enter salary (A salary of 0 cannot be entered): ")

        if not validate_positive_int(salary):
            print("Invalid employee salary")
            pause()
            return

        emp_id.salary = int(salary)

        if emp_id.employee_type == EmployeeType.MANAGER:
            bonus = input("Enter bonus: ")
            if not validate_bonus(bonus):
                print("Invalid employee bonus")
                pause()
                return
            
            emp_id.bonus = int(bonus)

        print("The data has been modified successfully")
        pause()

  # ---------------- EDIT DEPARTMENT ----------------
    def edit_department(self):
        if not self._departments:
            print("No departments available")
            pause()
            return
        
        dept_id = input("Enter department ID (A positive numerical value must be entered): ")
        if not validate_positive_int(dept_id):
            print("Invalid department ID")
            pause()
            return
        
        dept_id = int(dept_id)
        if dept_id not in self._departments:
            print("Department not found")
            pause()
            return
        
        dept_id = self._departments[dept_id]

        name = input("Enter department name (This field cannot be empty): ")
        if not validate_name(name):
            print("Invalid department name")
            pause()
            return

        dept_id.name = name
        print("The data has been modified successfully")
        pause()
