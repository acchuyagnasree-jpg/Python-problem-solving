class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display_employee(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def display_manager(self):
        print("Department:", self.department)


class TeamLeader(Manager):
    def __init__(self, emp_id, name, salary, department, team_size):
        super().__init__(emp_id, name, salary, department)
        self.team_size = team_size

    def display_team(self):
        print("Team Size:", self.team_size)


leader = TeamLeader(
    101,
    "Acchu",
    75000,
    "AI & ML",
    12
)

leader.display_employee()
leader.display_manager()
leader.display_team()
