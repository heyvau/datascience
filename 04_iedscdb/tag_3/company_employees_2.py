from __future__ import annotations


class Company:
  
    def __init__(self, name):
      self.name = name


    def __repr__(self) -> str:
        return f"Company {self.name}"


    def add_employee(self, employee: Employee):
        if not isinstance(employee, Employee):
            raise TypeError("argument type: Employee")

        employee.company = self

    @property
    def employees(self):
        return [
            employee
            for employee in Employee.employees
            if employee.company == self
        ]


class Employee:
  
    employees = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.company = None
        Employee.employees.append(self)


    def __repr__(self) -> str:
        return f"Employee {self.first_name} {self.last_name}"


    @property
    def company(self):
        return self._company


    @company.setter
    def company(self, company):
        if not isinstance(company, Company) and company is not None:
            raise TypeError("argument type: Company")
        self._company = company


if __name__ == "__main__":

    bmw = Company(name="BMW")

    employees = [
        Employee(first_name="Bobby", last_name="Fisher"),
        Employee(first_name="Alice", last_name="Smith"),
        Employee(first_name="Tom", last_name="Jones")
    ]

    for emp in employees:  
        bmw.add_employee(emp)

    print(bmw.employees)
