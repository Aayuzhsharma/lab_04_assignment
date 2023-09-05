class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, age):
        results = [emp for emp in self.employees if emp.age == age]
        return results

    def search_by_name(self, name):
        results = [emp for emp in self.employees if emp.name == name]
        return results

    def search_by_salary(self, operator, salary):
        if operator == ">":
            results = [emp for emp in self.employees if emp.salary > salary]
        elif operator == "<":
            results = [emp for emp in self.employees if emp.salary < salary]
        elif operator == ">=":
            results = [emp for emp in self.employees if emp.salary >= salary]
        elif operator == "<=":
            results = [emp for emp in self.employees if emp.salary <= salary]
        else:
            results = []
        return results

def main():
    emp_db = EmployeeDatabase()
    
    emp_db.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_db.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_db.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_db.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_db.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("AAYUSH SHARMA(E22CSEU1109)")
    print("Choose a search parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary (>, <, <=, >=)")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        age = int(input("Enter age to search: "))
        results = emp_db.search_by_age(age)
    elif choice == 2:
        name = input("Enter name to search: ")
        results = emp_db.search_by_name(name)
    elif choice == 3:
        operator = input("Enter operator (> or < or >= or <=): ")
        salary = int(input("Enter salary to search: "))
        results = emp_db.search_by_salary(operator, salary)
    else:
        print("Invalid choice")
        return

    if results:
        print("Search Results:")
        for emp in results:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Age: {emp.age}, Salary: {emp.salary}")
    else:
        print("No matching records found.")

if __name__ == "__main__":
    main()
