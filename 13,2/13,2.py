import tkinter
import tkinter.messagebox


class MPGConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.prompt_gallons = tkinter.Label(self.top_frame, text='Enter the number of Gallons:')
        self.gallons_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_miles = tkinter.Label(self.top_frame, text='Enter the number of miles driven on a full tank:')
        self.miles_entry = tkinter.Entry(self.top_frame, width=10)
        self.prompt_gallons.pack(side='top')
        self.gallons_entry.pack(side='top')
        self.prompt_miles.pack(side='top')
        self.miles_entry.pack(side='top')
        self.calc_button = tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def convert(self):
        miles = float(self.miles_entry.get())
        gallons = float(self.gallons_entry.get())
        mpg = miles / gallons
        self.label1 = tkinter.Label(self.top_frame, text='You will get ' + str(mpg) + ' mpg')
        self.label1.pack(side='top')
        self.bottom_frame.pack()


MPG_conv = MPGConverterGUI()
