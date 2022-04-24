import tkinter


class ShowInfo:
    def __init__(self, counts):
        # Create the main window widget.
        self.count = counts
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        self.my_button = tkinter.Button(self.bottom_frame, text='Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        self.my_button.pack(side='left')
        self.quit_button.pack(side='right')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def show_info(self):
        if self.count == 0:
            self.label1 = tkinter.Label(self.top_frame, text='Chase Lesniak')
            self.label2 = tkinter.Label(self.top_frame, text='5155 Landers dr.')
            self.label3 = tkinter.Label(self.top_frame, text='Arlington Heights, IL 60192')
            self.label1.pack(side='top')
            self.label2.pack(side='top')
            self.label3.pack(side='top')
            self.top_frame.pack()
            self.count = 1


name_and_address = ShowInfo(0)
