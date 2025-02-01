from abc import ABC, abstractmethod
from typing import List

# Step 1: Define Employee interface using Abstract Base Class (ABC)
class Employee(ABC):
    @abstractmethod
    def work(self) -> str:
        pass
    
    @abstractmethod
    def get_salary(self) -> float:
        pass

    @abstractmethod
    def working_hours(self) -> float:
        pass


# Step 2: Create concrete classes for different types of employees

class Manager(Employee):
    def __init__(self, name: str, salary: float, working: float):
        self.name = name
        self.salary = salary
        self.working= working

    def work(self) -> str:
        return f"{self.name} is managing the team."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self):
        return self.working

class Developer(Employee):
    def __init__(self, name: str, salary: float, working):
        self.name = name
        self.salary = salary
        self.working= working

    def work(self) -> str:
        return f"{self.name} is writing code."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self):
        return self.working


class Intern(Employee):
    def __init__(self, name: str, salary: float, working):
        self.name = name
        self.salary = salary
        self.working= working

    def work(self) -> str:
        return f"{self.name} is learning and assisting."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self):
        return self.working


# Step 3: Define Department class that manages Employees

class Department:
    def __init__(self, name: str):
        self.name = name
        self.employees: List[Employee] = []

    def hire(self, employee: Employee) -> None:
        self.employees.append(employee)
        print(f"{employee.name} has been hired.")

    def fire(self, employee: Employee) -> None:
        self.employees.remove(employee)
        print(f"{employee.name} has been fired.")

    def promote(self, employee:Employee) -> None:
        if employee.working>50:
            if employee.name== "Alice":
                print("Congratulations Alice, you are promoted as Product Manager!")
            if employee.name=="Bob":
                print("Congratulations Bob, You are promoted as Associate Developer!")
            if employee.name=="Charlie":
                print("Congratulations Charlie, You are promoted as Assistant developer!")
            if employee.name=="Ram":
                print("Congratulations Ram, You are promoted as Head of Security!")
        else:
            print(f"{employee.name}, You have Not been Promoted")

    def get_total_salary(self) -> float:
        return sum(employee.get_salary() for employee in self.employees)

    def show_employee_details(self) -> None:
        print(f"Employees in {self.name} Department:")
        for employee in self.employees:
            print(f"- {employee.name}, - Working hours: {employee.working}, - Salary: {employee.get_salary()}, - Role: {employee.work()}")

class Security(Employee):
    def __init__(self, name: str, salary: float,working: float):
        self.name = name
        self.salary = salary
        self.working=working

    def work(self) -> str:
        return f"{self.name} is Securing the assets."

    def get_salary(self) -> float:
        return self.salary
    
    def working_hours(self):
        return self.working
    
# Step 4: Create department and add employees

# Create employees
manager = Manager("Alice", 80000,35)
developer = Developer("Bob", 60000,89)
intern = Intern("Charlie", 20000,49)
securitystaff=Security("Ram",5000,57)

# Create a department and hire employees
it_department = Department("IT")

it_department.hire(manager)
it_department.hire(developer)
it_department.hire(intern)
it_department.hire(securitystaff)
# Show employee details
it_department.show_employee_details()
it_department.promote(manager)
it_department.promote(developer)
it_department.promote(intern)
it_department.promote(securitystaff)

# Total salary in the department
total_salary = it_department.get_total_salary()
print(f"Total salary expense for {it_department.name} department: ${total_salary}")