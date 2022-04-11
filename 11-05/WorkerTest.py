import ProductionWorker


def main():
    newworker = ProductionWorker.ProductionWorker(input("Please enter Name: "), input("Please enter Employee Number: "),
                                                  input("Please enter Shift Number(1-2): "),
                                                  input("Please enter hourly rate: "))
    print("This objects attributes are.....")
    print("Name: " + newworker.get_employee_name())
    print("Number: " + str(newworker.get_employee_num()))
    print("Shift Number: " + str(newworker.get_shift_num()))
    print("Hourly Rate: " + str(newworker.get_pay_rate()))


main()
