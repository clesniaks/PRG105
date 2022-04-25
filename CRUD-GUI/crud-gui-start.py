import tkinter
import tkinter.messagebox
import pickle


# main (root) GUI menu
class CrudGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Welcome Menu')

        self.top_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)

        self.radio_var = tkinter.IntVar()
        self.radio_var.set(1)

        # create the radio buttons
        self.look = tkinter.Radiobutton(self.top_frame, text='Look up customer',
                                        variable=self.radio_var, value=1)
        self.add = tkinter.Radiobutton(self.top_frame, text='Add Customer',
                                       variable=self.radio_var, value=2)
        self.change = tkinter.Radiobutton(self.top_frame, text='Change customer email',
                                          variable=self.radio_var, value=3)
        self.delete = tkinter.Radiobutton(self.top_frame, text='Delete customer',
                                          variable=self.radio_var, value=4)

        # pack the radio buttons
        self.look.pack(anchor='w', padx=20)
        self.add.pack(anchor='w', padx=20)
        self.change.pack(anchor='w', padx=20)
        self.delete.pack(anchor='w', padx=20)

        # create ok and quit buttons
        self.ok_button = tkinter.Button(self.bottom_frame, text='OK', command=self.open_menu)
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy)

        # pack the buttons
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

    def open_menu(self):
        if self.radio_var.get() == 1:
            _ = LookGUI(self.master)
        if self.radio_var.get() == 2:
            _ = AddGUI(self.master)
        if self.radio_var.get() == 3:
            _ = EditGUI(self.master)
        if self.radio_var.get() == 4:
            _ = DeleteGUI(self.master)


class LookGUI:
    def __init__(self, master):

        # open the file, load to customers, close file. Do in each class
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}

        # tkinter.Toplevel() is like tkinter.Frame() but it opens in a new window
        self.look = tkinter.Toplevel(master)
        self.look.title('Search for customer')

        # create Frames for this Toplevel window
        self.top_frame = tkinter.Frame(self.look)
        self.middle_frame = tkinter.Frame(self.look)
        self.bottom_frame = tkinter.Frame(self.look)

        # widgets for top frame - label and entry box for name
        self.search_label = tkinter.Label(self.top_frame, text='Enter customer name to look for: ')
        self.search_entry = tkinter.Entry(self.top_frame, width=15)

        # pack top frame
        self.search_label.pack(side='left')
        self.search_entry.pack(side='left')

        # middle frame - label for results
        self.value = tkinter.StringVar()
        self.info = tkinter.Label(self.middle_frame, text='Results: ')
        self.result_label = tkinter.Label(self.middle_frame, textvariable=self.value)

        # pack Middle frame
        self.info.pack(side='left')
        self.result_label.pack(side='left')

        # buttons for bottom frame
        self.search_button = tkinter.Button(self.bottom_frame, text='Search', command=self.search)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        # pack bottom frame
        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def search(self):
        name = self.search_entry.get()
        result = self.customers.get(name, 'Not Found')
        self.value.set(result)

    def back(self):
        self.look.destroy()


class AddGUI:

    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'wb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}
        self.adds = tkinter.Toplevel(master)
        self.adds.title('Adding Customer')

        self.top_frame = tkinter.Frame(self.adds)
        self.middle_frame = tkinter.Frame(self.adds)
        self.bottom_frame = tkinter.Frame(self.adds)

        self.prompt_name = tkinter.Label(self.top_frame, text='Enter the name of the customer:')
        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_address = tkinter.Label(self.top_frame, text='Enter the address:')
        self.address_entry = tkinter.Entry(self.top_frame, width=10)

        self.search_button = tkinter.Button(self.bottom_frame, text='add', command=self.add)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.search_button.pack(side='left')
        self.back_button.pack(side='left')

        self.prompt_name.pack(side='top')
        self.name_entry.pack(side='top')
        self.prompt_address.pack(side='top')
        self.address_entry.pack(side='top')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def add(self):
        name = self.name_entry.get()
        address = self.address_entry.get()
        if name in self.customers:
            self.customers[name] = address
            self.save()
        else:
            print("Customer's name not found.")
            print("adding to the dictionary")
            self.customers[name] = address
            self.save()

    def back(self):
        self.adds.destroy()

    def save(self):
        print("The save file was updated with your changes")
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()


class EditGUI:

    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}
            print("Could not find file")

        self.adds = tkinter.Toplevel(master)
        self.adds.title('Change Email')

        self.top_frame = tkinter.Frame(self.adds)
        self.middle_frame = tkinter.Frame(self.adds)
        self.bottom_frame = tkinter.Frame(self.adds)

        self.prompt_name = tkinter.Label(self.top_frame, text='Enter the name of the customer:')
        self.name_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_address = tkinter.Label(self.middle_frame, text='Enter the address:')
        self.address_entry = tkinter.Entry(self.middle_frame, width=10)

        self.edit_button = tkinter.Button(self.bottom_frame, text='Edit Customer', command=self.edit)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.edit_button.pack(side='left')
        self.back_button.pack(side='left')

        self.prompt_name.pack(side='top')
        self.prompt_address.pack(side='top')

        self.name_entry.pack(side='top')
        self.address_entry.pack(side='top')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def edit(self):

        name = self.name_entry.get()
        if name in self.customers:
            self.customers[name] = self.address_entry.get()
            self.save()
        else:
            print("Customer's name not found.")
            print("Cannot Edit")

    def back(self):
        self.adds.destroy()

    def save(self):
        print("The save file was updated with your changes")
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()


class DeleteGUI:

    def __init__(self, master):
        try:
            input_file = open("customer_file.dat", 'rb')
            self.customers = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.customers = {}
            print("Could not find file")

        self.adds = tkinter.Toplevel(master)
        self.adds.title('Delete Customer')

        self.top_frame = tkinter.Frame(self.adds)
        self.middle_frame = tkinter.Frame(self.adds)
        self.bottom_frame = tkinter.Frame(self.adds)

        self.prompt_name = tkinter.Label(self.top_frame, text='Enter the name of the customer:')
        self.name_entry = tkinter.Entry(self.middle_frame, width=10)

        self.edit_button = tkinter.Button(self.bottom_frame, text='Delete Customer', command=self.delete)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.edit_button.pack(side='left')
        self.back_button.pack(side='left')

        self.prompt_name.pack(side='top')
        self.name_entry.pack(side='top')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def delete(self):

        name = self.name_entry.get()
        if name in self.customers:
            del self.customers[name]
            self.save()
        else:
            print("Customer's name not found.")
            print("Cannot Delete")

    def back(self):
        self.adds.destroy()

    def save(self):
        print("The save file was updated with your changes")
        save_file = open('customer_file.dat', 'wb')
        pickle.dump(self.customers, save_file)
        save_file.close()


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = CrudGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
