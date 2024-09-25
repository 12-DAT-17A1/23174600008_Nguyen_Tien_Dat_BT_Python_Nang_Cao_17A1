class Date:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day:02d}/{self.month:02d}/{self.year}"
class Employee:
    def __init__(self, full_name: str, birth_date: Date, start_date: Date):
        self.full_name = full_name
        self.birth_date = birth_date
        self.start_date = start_date

    def __str__(self):
        return (f"Employee Name: {self.full_name}\n"
                f"Birth Date: {self.birth_date}\n"
                f"Start Date: {self.start_date}")



class EmployeeManagement:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        print(f"Thêm nhân viên: {employee.full_name}")

    def list_employees(self):
        if not self.employees:
            print("Danh sách nhân viên trống.")
            return
        for emp in self.employees:
            print(emp)

# Sử dụng các lớp đã tạo
if __name__ == "__main__":
    # Tạo một đối tượng quản lý nhân viên
    emp_mgmt = EmployeeManagement()

    # Thêm nhân viên
    emp1 = Employee("Alice", Date(15, 5, 1990), Date(1, 1, 2020))
    emp2 = Employee("Bob", Date(22, 8, 1985), Date(15, 3, 2019))

    emp_mgmt.add_employee(emp1)
    emp_mgmt.add_employee(emp2)

    # Liệt kê nhân viên
    print("\nList of employees:")
    emp_mgmt.list_employees()




