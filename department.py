class Department:
    def __init__(self, dept_id, name):
        self._id = dept_id
        self._name = name
        self._employees = []

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
    def employees(self):
        return self._employees

    def add_employee(self, emp):
        self._employees.append(emp)

    def remove_employee(self, emp):
        self._employees.remove(emp)
