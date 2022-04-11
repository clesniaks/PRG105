class Employee:

    def __init__(self, employee_name, employee_num):
        self.__employee_name = employee_name
        self.__employee_num = employee_num

    def set_employee_name(self, name):
        self.__employee_name = name

    def set_employee_num(self, num):
        self.__employee_num = num

    def get_employee_name(self):
        return self.__employee_name

    def get_employee_num(self):
        return self.__employee_num

    def __str__(self):
        print("Employee Name: " + self.get_employee_name())
        print("Employee Number: " + str(self.get_employee_num()))
