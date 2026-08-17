class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        return 0


class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, monthly_salary):
        super().__init__(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours, rate):
        super().__init__(name, employee_id)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate


class Payroll:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def generate_payroll(self):
        print("\nEmployee Payroll")
        print("-" * 45)

        for employee in self.employees:
            salary = employee.calculate_salary()

            print(
                f"{employee.name:15}"
                f"ID: {employee.employee_id:<5}"
                f"Salary: ₹{salary}"
            )


payroll = Payroll()

payroll.add_employee(
    FullTimeEmployee("Alice", 101, 50000)
)

payroll.add_employee(
    PartTimeEmployee("Bob", 102, 80, 500)
)

payroll.add_employee(
    FullTimeEmployee("Charlie", 103, 65000)
)

payroll.generate_payroll()
