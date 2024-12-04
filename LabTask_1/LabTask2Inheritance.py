class Person:
    def _init_(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def _init_(self, first_name, last_name, graduation_year):
        super()._init_(first_name, last_name)
        self.graduation_year = graduation_year

    def display(self):
        return f"{super().display()}, Graduation Year: {self.graduation_year}"

class Teacher(Person):
    def _init_(self, first_name, last_name, joining_year):
        super()._init_(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, Joining Year: {self.joining_year}"

class Admin(Person):
    def _init_(self, first_name, last_name, joining_year):
        super()._init_(first_name, last_name)
        self.joining_year = joining_year

    def display(self):
        return f"{super().display()}, Joining Year: {self.joining_year}"

class Employee(Person):
    def _init_(self, first_name, last_name, employee_id):
        super()._init_(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        return f"{super().display()}, Employee ID: {self.employee_id}"

class Alumni(Student):
    def _init_(self, first_name, last_name, graduation_year, passing_year):
        super()._init_(first_name, last_name, graduation_year)
        self.passing_year = passing_year

    def display(self):
        return f"{super().display()}, Passing Year: {self.passing_year}"

class CurrentStudent(Student):
    def _init_(self, first_name, last_name, graduation_year, current_semester):
        super()._init_(first_name, last_name, graduation_year)
        self.current_semester = current_semester

    def display(self):
        return f"{super().display()}, Current Semester: {self.current_semester}"