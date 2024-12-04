class InvalidVoterException(Exception):
    def _init_(self, message="Age is less than 18. Not eligible to vote."):
        self.message = message
        super()._init_(self.message)

# Handling the custom exception
try:
    age = int(input("Enter age: "))
    if age < 18:
        raise InvalidVoterException()
    print("You are eligible to vote.")
except InvalidVoterException as e:
    print(e)

    class SalaryNotInRange(Exception):
      def _init_(self, message="Salary is not in the valid range (10000 - 50000)."):
        self.message = message
        super()._init_(self.message)

class Employee:
    def _init_(self, name, salary):
        self.name = name
        self.salary = salary
        if not (10000 <= self.salary <= 50000):
            raise SalaryNotInRange()

    def displaySalary(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

# Handling the custom exception
try:
    name = input("Enter employee name: ")
    salary = int(input("Enter employee salary: "))
    emp = Employee(name, salary)
    print(emp.displaySalary())
except SalaryNotInRange as e:
    print(e)

    arr = [10, 5, 15, 20]
try:
    divisor = int(input("Enter divisor: "))
    for num in arr:
        print(f"{num} / {divisor} = {num / divisor}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter a valid integer.")
except Exception as e:
    print(f"Unexpected error: {e}")
else:
    print("Division performed successfully.")
finally:
    print("Operation complete.")


    class InsufficientBalance(Exception):
      def _init_(self, message="Withdrawal amount exceeds balance."):
        self.message = message
        super()._init_(self.message)

class BankAccount:
    def _init_(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance()
        self.balance -= amount
        return self.balance

# Handling the custom exception
try:
    account = BankAccount(10000)
    withdrawal_amount = int(input("Enter withdrawal amount: "))
    remaining_balance = account.withdraw(withdrawal_amount)
    print(f"Withdrawal successful. Remaining balance: {remaining_balance}")
except InsufficientBalance as e:
    print(e)
except ValueError:
    print("Error: Please enter a valid amount.")