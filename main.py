from company_system import CompanySystem
from enums import EmployeeType

def main():
    system = CompanySystem()
    print("Welcome to the company management system")
    while True:
        print("""
1. Add Department
2. Add Worker
3. Add Manager
4. Show Employee
5. Show All Employees
6. Assign Employee to Department
7. Remove Employee from Department
8. Transfer Employee
9. Delete Employee
10. Delete Department
11. Show Departments with Employees
12. Calculate Salary for Employee
13. Edit employee
14. edit_department             
0. Exit
""")
        choice = input("Choose: ")

        if choice == "1":
            system.add_department()
        elif choice == "2":
            system.add_employee(EmployeeType.WORKER)
        elif choice == "3":
            system.add_employee(EmployeeType.MANAGER)
        elif choice == "4":
            system.show_employee()
        elif choice == "5":
            system.show_all_employees()
        elif choice == "6":
            system.assign_employee()
        elif choice == "7":
            system.remove_from_department()
        elif choice == "8":
            system.transfer_employee()
        elif choice == "9":
            system.delete_employee()
        elif choice == "10":
            system.delete_department()
        elif choice == "11":
            system.show_departments_with_employees()
        elif choice == "12":
            system.calculate_salary_for_employee()
        elif choice == "13":
            system.edit_employee()
        elif choice == "14":
            system.edit_department()
        elif choice == "0":
            print("Goodbye")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
