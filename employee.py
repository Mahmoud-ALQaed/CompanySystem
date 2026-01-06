from abc import ABC, abstractmethod
from enums import EmployeeType


class Employee(ABC):
    def __init__(self, emp_id, name, age, salary, employee_type: EmployeeType):
        self._id = emp_id
        self._name = name
        self._age = age
        self._salary = salary
        self._employee_type = employee_type

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value

    @property
    def employee_type(self):
        return self._employee_type

    @abstractmethod
    def calculate_salary(self):
        pass

    def display(self):
        print(f"ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Type: {self._employee_type.value}")
        print(f"Final Salary: {self.calculate_salary()}")


class Worker(Employee):
    def __init__(self, emp_id, name, age, salary):
        super().__init__(emp_id, name, age, salary, EmployeeType.WORKER)

    def calculate_salary(self):
        return self._salary


class Manager(Employee):
    def __init__(self, emp_id, name, age, salary, bonus):
        super().__init__(emp_id, name, age, salary, EmployeeType.MANAGER)
        self._bonus = bonus

    @property
    def bonus(self):
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        if value >= 0:
            self._bonus = value

    def calculate_salary(self):
        return self._salary + self._bonus
