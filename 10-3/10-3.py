class PersonData:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.age = 0
        self.phone = ""

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

    def set_name(self, new_name):
        self.name = new_name

    def set_address(self, new_address):
        self.address = new_address

    def set_age(self, new_age):
        self.age = new_age

    def set_phone(self, new_phone):
        self.phone = new_phone

    def print_info(self):
        print("User: " + self.name)
        print("Age: " + str(self.age))
        print("Address: " + self.address)
        print("Phone Number: " + self.phone + "\n" + "-"*32)


def main():
    new_person = PersonData()
    newer_person = PersonData()
    newest_person = PersonData()
    new_person.set_name("Chase Lesniak")
    new_person.set_phone("8472489385")
    new_person.set_age(25)
    new_person.set_address("5155 Landers dr.")
    newer_person.set_name("Sam Miseyka")
    newer_person.set_phone("8527897426")
    newer_person.set_age(26)
    newer_person.set_address("523 Barrington Rd.")
    newest_person.set_name("James Lesniak")
    newest_person.set_age(66)
    newest_person.set_phone("8479972015")
    newest_person.set_address("5155 Landers dr.")
    new_person.print_info()
    newer_person.print_info()
    newest_person.print_info()


main()
