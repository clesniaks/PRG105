import Employee


class ProductionWorker(Employee.Employee):

    def __init__(self, employee_name, employee_num, shift_num, pay_rate):
        Employee.Employee.__init__(self, employee_name, employee_num)
        self.__shift_num = shift_num
        self.__pay_rate = pay_rate

    def set_shift_num(self, num):
        self.__shift_num = num

    def set_pay_rate(self, rate):
        self.__pay_rate = rate

    def get_shift_num(self):
        return self.__shift_num

    def get_pay_rate(self):
        return self.__pay_rate

    def __str__(self):
        Employee.Employee.__str__()
        print("Shift Number: " + str(self.get_shift_num()))
        print("Pay Rate: " + str(self.get_pay_rate()))
