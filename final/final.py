# Import Module
import pickle
import tkinter
import random
from tkinter import messagebox


class YahtzeeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Yahtzee')
        # Loading Images and resizing
        # self.photo = Image.open('Dice1.png')
        # self.dice2_photo = Image.open('Dice2.png')
        # self.dice3_photo = Image.open('Dice3.png')
        # self.dice4_photo = Image.open('Dice4.png')
        # self.dice5_photo = Image.open('Dice5.png')
        # self.dice6_photo = Image.open('Dice6.png')
        # self.photo = self.photo.resize((50, 50))
        # self.dice2_photo = self.photo.resize((50, 50))
        # self.dice3_photo = self.photo.resize((50, 50))
        # self.dice4_photo = self.photo.resize((50, 50))
        # self.dice5_photo = self.photo.resize((50, 50))
        # self.dice6_photo = self.photo.resize((50, 50))
        # self.photo = ImageTk.PhotoImage(self.photo)
        # self.dice2_photo = ImageTk.PhotoImage(self.dice2_photo)
        # self.dice3_photo = ImageTk.PhotoImage(self.dice3_photo)
        # self.dice4_photo = ImageTk.PhotoImage(self.dice4_photo)
        # self.dice5_photo = ImageTk.PhotoImage(self.dice5_photo)
        # self.dice6_photo = ImageTk.PhotoImage(self.dice6_photo)

        # creating three frames
        self.top_frame = tkinter.Frame(self.master)
        self.middle_frame = tkinter.Frame(self.master)
        self.bottom_frame = tkinter.Frame(self.master)
        # creating string_var and int_var objects
        self.total_score = 0
        self.num_rolls = 0
        self.submitted_ones = False
        self.submitted_twos = False
        self.submitted_threes = False
        self.submitted_fours = False
        self.submitted_fives = False
        self.submitted_sixes = False
        self.submitted_three_of_a_kind = False
        self.submitted_four_of_a_kind = False
        self.submitted_yahtzee = False
        self.submitted_chance = False
        self.submitted_large_straight = False
        self.submitted_small_straight = False
        self.submitted_full_house = False
        self.radio_var = tkinter.IntVar()
        self.one_score = tkinter.StringVar()
        self.two_score = tkinter.StringVar()
        self.three_score = tkinter.StringVar()
        self.four_score = tkinter.StringVar()
        self.five_score = tkinter.StringVar()
        self.six_score = tkinter.StringVar()
        self.three_of_a_kind_score = tkinter.StringVar()
        self.four_of_a_kind_score = tkinter.StringVar()
        self.yahtzee_score = tkinter.StringVar()
        self.chance_score = tkinter.StringVar()
        self.large_straight_score = tkinter.StringVar()
        self.small_straight_score = tkinter.StringVar()
        self.full_house_score = tkinter.StringVar()

        self.dice_var = tkinter.StringVar()
        self.dice_var2 = tkinter.StringVar()
        self.dice_var3 = tkinter.StringVar()
        self.dice_var4 = tkinter.StringVar()
        self.dice_var5 = tkinter.StringVar()

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        # setting int_var objects to 0 for check buttons, 1 for radio button
        self.one_score.set('0')
        self.two_score.set('0')
        self.three_score.set('0')
        self.four_score.set('0')
        self.five_score.set('0')
        self.six_score.set('0')
        self.three_of_a_kind_score.set('0')
        self.four_of_a_kind_score.set('0')
        self.yahtzee_score.set('0')
        self.chance_score.set('0')
        self.large_straight_score.set('0')
        self.small_straight_score.set('0')
        self.full_house_score.set('0')

        self.dice_var.set('0')
        self.dice_var2.set('0')
        self.dice_var3.set('0')
        self.dice_var4.set('0')
        self.dice_var5.set('0')

        self.radio_var.set(1)
        self.cb_var1.set(1)
        self.cb_var2.set(1)
        self.cb_var3.set(1)
        self.cb_var4.set(1)
        self.cb_var5.set(1)

        # creating labels for the dice values
        self.dice_label1 = tkinter.Label(self.top_frame, textvariable=self.dice_var, font=("Helvetica", 60), padx=10)
        self.dice_label2 = tkinter.Label(self.top_frame, textvariable=self.dice_var2, font=("Helvetica", 60), padx=10)
        self.dice_label3 = tkinter.Label(self.top_frame, textvariable=self.dice_var3, font=("Helvetica", 60), padx=10)
        self.dice_label4 = tkinter.Label(self.top_frame, textvariable=self.dice_var4, font=("Helvetica", 60), padx=10)
        self.dice_label5 = tkinter.Label(self.top_frame, textvariable=self.dice_var5, font=("Helvetica", 60), padx=10)

        # create the check buttons
        self.cb1 = tkinter.Checkbutton(self.middle_frame, text='Roll dice 1', font=("Helvetica", 15),
                                       variable=self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.middle_frame, text='Roll dice 2', font=("Helvetica", 15),
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.middle_frame, text='Roll dice 3', font=("Helvetica", 15),
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.middle_frame, text='Roll dice 4', font=("Helvetica", 15),
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.middle_frame, text='Roll dice 5', font=("Helvetica", 15),
                                       variable=self.cb_var5)

        # create radio buttons and variable labels for scoring
        self.scoringlabel = tkinter.Label(self.middle_frame, text='Categories', font=("Helvetica", 20))
        self.upper_label = tkinter.Label(self.middle_frame, text='Upper Section:', font=("Helvetica", 15))
        self.rb_score1 = tkinter.Radiobutton(self.middle_frame, text='Ones: ', variable=self.radio_var, value=1,
                                             font=("Helvetica", 15))
        self.ones_label = tkinter.Label(self.middle_frame, textvariable=self.one_score, font=("Helvetica", 14))
        self.rb_score2 = tkinter.Radiobutton(self.middle_frame, text='Twos', variable=self.radio_var, value=2,
                                             font=("Helvetica", 15))
        self.twos_label = tkinter.Label(self.middle_frame, textvariable=self.two_score, font=("Helvetica", 14))
        self.rb_score3 = tkinter.Radiobutton(self.middle_frame, text='Threes', variable=self.radio_var, value=3,
                                             font=("Helvetica", 15))
        self.threes_label = tkinter.Label(self.middle_frame, textvariable=self.three_score, font=("Helvetica", 14))
        self.rb_score4 = tkinter.Radiobutton(self.middle_frame, text='Fours', variable=self.radio_var, value=4,
                                             font=("Helvetica", 15))
        self.fours_label = tkinter.Label(self.middle_frame, textvariable=self.four_score, font=("Helvetica", 14))
        self.rb_score5 = tkinter.Radiobutton(self.middle_frame, text='Fives', variable=self.radio_var, value=5,
                                             font=("Helvetica", 15))
        self.fives_label = tkinter.Label(self.middle_frame, textvariable=self.five_score, font=("Helvetica", 14))
        self.rb_score6 = tkinter.Radiobutton(self.middle_frame, text='Sixes', variable=self.radio_var, value=6,
                                             font=("Helvetica", 15))
        self.sixes_label = tkinter.Label(self.middle_frame, textvariable=self.six_score, font=("Helvetica", 14))
        self.rb_score7 = tkinter.Radiobutton(self.middle_frame, text='Three-Of-A-Kind', variable=self.radio_var,
                                             value=7,
                                             font=("Helvetica", 15))
        self.lower_label = tkinter.Label(self.middle_frame, text='Lower Section:',
                                         font=("Helvetica", 15))
        self.three_of_a_kind_label = tkinter.Label(self.middle_frame, textvariable=self.three_of_a_kind_score,
                                                   font=("Helvetica", 15))
        self.rb_score8 = tkinter.Radiobutton(self.middle_frame, text='Four-Of-A-Kind', variable=self.radio_var, value=8,
                                             font=("Helvetica", 15))
        self.four_of_a_kind_label = tkinter.Label(self.middle_frame, textvariable=self.four_of_a_kind_score,
                                                  font=("Helvetica", 15))
        self.rb_score9 = tkinter.Radiobutton(self.middle_frame, text='Yahtzee', variable=self.radio_var, value=9,
                                             font=("Helvetica", 15))
        self.yahtzee_label = tkinter.Label(self.middle_frame, textvariable=self.yahtzee_score,
                                           font=("Helvetica", 15))
        self.rb_score10 = tkinter.Radiobutton(self.middle_frame, text='Chance', variable=self.radio_var, value=10,
                                              font=("Helvetica", 15))
        self.chance_label = tkinter.Label(self.middle_frame, textvariable=self.chance_score,
                                          font=("Helvetica", 15))
        self.rb_score11 = tkinter.Radiobutton(self.middle_frame, text='Large Straight', variable=self.radio_var,
                                              value=11,
                                              font=("Helvetica", 15))
        self.large_straight_label = tkinter.Label(self.middle_frame, textvariable=self.large_straight_score,
                                                  font=("Helvetica", 15))
        self.rb_score12 = tkinter.Radiobutton(self.middle_frame, text='Small Straight', variable=self.radio_var,
                                              value=12,
                                              font=("Helvetica", 15))
        self.small_straight_label = tkinter.Label(self.middle_frame, textvariable=self.small_straight_score,
                                                  font=("Helvetica", 15))
        self.rb_score13 = tkinter.Radiobutton(self.middle_frame, text='Full House', variable=self.radio_var,
                                              value=13,
                                              font=("Helvetica", 15))
        self.full_house_label = tkinter.Label(self.middle_frame, textvariable=self.full_house_score,
                                              font=("Helvetica", 15))
        # pack the check buttons and labels for the dice and the checkboxes
        self.dice_label1.pack(side='left')
        self.dice_label2.pack(side='left')
        self.dice_label3.pack(side='left')
        self.dice_label4.pack(side='left')
        self.dice_label5.pack(side='left')
        self.cb1.pack(side='left')
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb5.pack(side='left')
        # Pack the scoring labels and Radio buttons
        self.scoringlabel.pack(side='top')
        self.upper_label.pack(side='top')
        self.rb_score1.pack(side='top')
        self.ones_label.pack(side='top')
        self.rb_score2.pack(side='top')
        self.twos_label.pack(side='top')
        self.rb_score3.pack(side='top')
        self.threes_label.pack(side='top')
        self.rb_score4.pack(side='top')
        self.fours_label.pack(side='top')
        self.rb_score5.pack(side='top')
        self.fives_label.pack(side='top')
        self.rb_score6.pack(side='top')
        self.sixes_label.pack(side='top')
        self.lower_label.pack(side='top')
        self.rb_score7.pack(side='top')
        self.three_of_a_kind_label.pack(side='top')
        self.rb_score8.pack(side='top')
        self.four_of_a_kind_label.pack(side='top')
        self.rb_score9.pack(side='top')
        self.yahtzee_label.pack(side='top')
        self.rb_score10.pack(side='top')
        self.chance_label.pack(side='top')
        self.rb_score11.pack(side='top')
        self.large_straight_label.pack(side='top')
        self.rb_score12.pack(side='top')
        self.small_straight_label.pack(side='top')
        self.rb_score13.pack(side='top')
        self.full_house_label.pack(side='top')

        # create submit score, roll button, help and quit buttons
        self.score = tkinter.Button(self.bottom_frame, text='Submit score', command=self.submit_score, padx=30,
                                    font=("Helvetica", 30))
        self.ok_button = tkinter.Button(self.bottom_frame, text='Roll', command=self.show_selection, padx=30,
                                        font=("Helvetica", 30))
        self.help_button = tkinter.Button(self.bottom_frame, text='Help', command=self.help, padx=30,
                                          font=("Helvetica", 30))
        self.quit_button = tkinter.Button(self.bottom_frame, text='QUIT', command=self.master.destroy, padx=30,
                                          font=("Helvetica", 30))

        # pack the buttons
        self.ok_button.pack(side='left')
        self.score.pack(side='left')
        self.help_button.pack(side='left')
        self.quit_button.pack(side='left')

        # pack the frames
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    # method for rolling the dice if checkbox is checked roll that dice and update the dice.var
    def show_selection(self):
        # Limit player to 3 rolls
        if self.num_rolls < 3:
            if self.cb_var1.get() == 1:
                dice1.roll()
                self.dice_var.set(dice1.side_up)
            if self.cb_var2.get() == 1:
                dice2.roll()
                self.dice_var2.set(dice2.side_up)
            if self.cb_var3.get() == 1:
                dice3.roll()
                self.dice_var3.set(dice3.side_up)
            if self.cb_var4.get() == 1:
                dice4.roll()
                self.dice_var4.set(dice4.side_up)
            if self.cb_var5.get() == 1:
                dice5.roll()
                self.dice_var5.set(dice5.side_up)
            self.num_rolls += 1
            self.score_it(dice_list)
        else:
            # player has used 3 rolls
            messagebox.showinfo("Warning",
                                "You have used all of your rolls for this turn! Please choose a box to score.")

    # This method handles updating the scoring labels with the dice_list that were just rolled
    def score_it(self, dice_lists):
        # variables for dice value count:
        ones = 0
        twos = 0
        threes = 0
        fours = 0
        fives = 0
        sixes = 0
        # variables for score placeholders
        three_of_a_kind = 0
        four_of_a_kind = 0
        yahtzee = 0
        large_straight = 0
        small_straight = 0
        full_house = 0
        # getting the dice value counts and assigning them
        for dice in dice_lists:
            if int(dice.side_up) == 1:
                ones = ones + 1
            if int(dice.side_up) == 2:
                twos = twos + 1
            if int(dice.side_up) == 3:
                threes = threes + 1
            if int(dice.side_up) == 4:
                fours = fours + 1
            if int(dice.side_up) == 5:
                fives = fives + 1
            if int(dice.side_up) == 6:
                sixes = sixes + 1
        # Conditions for scoring
        # scoring for three of a kind is the summation of dice values
        if ones == 3 or twos == 3 or threes == 3 or fours == 3 or fives == 3 or sixes == 3:
            for dice in dice_lists:
                three_of_a_kind += int(dice.side_up)
        # scoring for four of a kind is the summation of dice values
        if ones == 4 or twos == 4 or threes == 4 or fours == 4 or fives == 4 or sixes == 4:
            for dice in dice_lists:
                four_of_a_kind += int(dice.side_up)
        # scoring for yahtzee is 50 points
        if ones == 5 or twos == 5 or threes == 5 or fours == 5 or sixes == 5:
            yahtzee = 50
        # scoring for large straight is 40 pts
        if (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1) or (
                twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1 and sixes >= 1):
            large_straight = 40
        # scoring for small straight is 30 points
        if (ones >= 1 and twos >= 1 and threes >= 1 and fours >= 1) or (
                twos >= 1 and threes >= 1 and fours >= 1 and fives >= 1) or (
                threes >= 1 and fours >= 1 and fives >= 1 and sixes >= 1):
            small_straight = 30
        # scoring for full house is 25 points
        if (ones == 3 or twos == 3 or threes == 3 or fours == 3 or fives == 3 or sixes == 3) and (
                ones == 2 or twos == 2 or threes == 2 or fours == 2 or fives == 2 or sixes == 2):
            full_house = 25
        # updating stringvar scores to update category labels
        self.one_score.set(ones)
        self.two_score.set(2 * twos)
        self.three_score.set(3 * threes)
        self.four_score.set(4 * fours)
        self.five_score.set(5 * fives)
        self.six_score.set(6 * sixes)
        self.three_of_a_kind_score.set(three_of_a_kind)
        self.four_of_a_kind_score.set(four_of_a_kind)
        self.yahtzee_score.set(yahtzee)
        self.chance_score.set(ones + 2 * twos + 3 * threes + 4 * fours + 5 * fives + 6 * sixes)
        self.large_straight_score.set(large_straight)
        self.small_straight_score.set(small_straight)
        self.full_house_score.set(full_house)

    def submit_score(self):
        if self.num_rolls == 0:
            messagebox.showinfo("User no roll", "Please roll the dice before scoring")
        else:
            if self.radio_var.get() == 1 and not self.submitted_ones:
                self.total_score += int(self.one_score.get())
                self.submitted_ones = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score1.destroy()
                self.ones_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 2 and not self.submitted_twos:
                self.total_score += int(self.two_score.get())
                self.submitted_twos = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score2.destroy()
                self.twos_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 3 and not self.submitted_threes:
                self.total_score += int(self.three_score.get())
                self.submitted_threes = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score3.destroy()
                self.threes_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 4 and not self.submitted_fours:
                self.total_score += int(self.four_score.get())
                self.submitted_fours = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score4.destroy()
                self.fours_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 5 and not self.submitted_fives:
                self.total_score += int(self.five_score.get())
                self.submitted_fives = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score5.destroy()
                self.fives_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 6 and not self.submitted_sixes:
                self.total_score += int(self.six_score.get())
                self.submitted_sixes = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score6.destroy()
                self.sixes_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 7 and not self.submitted_three_of_a_kind:
                self.total_score += int(self.three_of_a_kind_score.get())
                self.submitted_three_of_a_kind = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score7.destroy()
                self.three_of_a_kind_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 8 and not self.submitted_four_of_a_kind:
                self.total_score += int(self.four_of_a_kind_score.get())
                self.submitted_four_of_a_kind = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score8.destroy()
                self.four_of_a_kind_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 9 and not self.submitted_yahtzee:
                self.total_score += int(self.yahtzee_score.get())
                self.submitted_yahtzee = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score9.destroy()
                self.yahtzee_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 10 and not self.submitted_chance:
                self.total_score += int(self.chance_score.get())
                self.submitted_chance = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score10.destroy()
                self.chance_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 11 and not self.submitted_large_straight:
                self.total_score += int(self.large_straight_score.get())
                self.submitted_large_straight = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score11.destroy()
                self.large_straight_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 12 and not self.submitted_small_straight:
                self.total_score += int(self.small_straight_score.get())
                self.submitted_small_straight = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score12.destroy()
                self.small_straight_label.destroy()
                self.cbvar_reset()
            elif self.radio_var.get() == 13 and not self.submitted_full_house:
                self.total_score += int(self.full_house_score.get())
                self.submitted_full_house = True
                self.num_rolls = 0
                messagebox.showinfo("New Turn", "New turn")
                self.set_new_dice(dice_list)
                self.rb_score13.destroy()
                self.full_house_label.destroy()
                self.cbvar_reset()
            elif self.submitted_ones and self.submitted_twos and self.submitted_threes and self.submitted_fours and self.submitted_fives and self.submitted_sixes and self.submitted_three_of_a_kind and self.submitted_four_of_a_kind and self.submitted_yahtzee and self.submitted_chance and self.submitted_large_straight and self.submitted_small_straight and self.submitted_full_house:
                _ = Highscores(self.master, self.total_score)
                self.scoringlabel.destroy()
                self.lower_label.destroy()
                self.upper_label.destroy()
            else:
                messagebox.showinfo("Warning", "You have already scored this box!")

    def set_new_dice(self, dice_lists):
        for dice in dice_lists:
            dice.set_side_up('0')
        self.dice_var.set(dice1.side_up)
        self.dice_var2.set(dice2.side_up)
        self.dice_var3.set(dice3.side_up)
        self.dice_var4.set(dice4.side_up)
        self.dice_var5.set(dice5.side_up)
        self.score_it(dice_list)

    def help(self):
        messagebox.showinfo("Help",
                            "How to play:" + "\n" + "The goal of yahtzee is to score the most points in a variety of categories.\n" + "Select all of your dice using the middle checkboxes and click the roll button to roll them.\n" + "You may de-select the dice at any time by clicking on the checkbox for the dice you wish tp de-select.\n" + "You only get 3 rolls until you submit your dice towards points in a category for scoring.\n" + "select a category on the right side of the screen and click submit score.\n" + "Once you submit your points into every category, you can add your highscore to the list by clicking the Submit score button after all categories are filled.")

    def cbvar_reset(self):
        self.cb_var1.set(1)
        self.cb_var2.set(1)
        self.cb_var3.set(1)
        self.cb_var4.set(1)
        self.cb_var5.set(1)


class Highscores:

    def __init__(self, master, total_score):
        try:
            input_file = open("highscores.dat", 'rb')
            self.highscores = pickle.load(input_file)
            input_file.close()
        except (FileNotFoundError, IOError):
            self.highscores = {}
        self.adds = tkinter.Toplevel(master)
        self.adds.title('Adding Score')
        self.totalscore = total_score

        self.top_frame = tkinter.Frame(self.adds)
        self.middle_frame = tkinter.Frame(self.adds)
        self.bottom_frame = tkinter.Frame(self.adds)

        self.prompt_name = tkinter.Label(self.top_frame, text='Enter the name of the User:')
        self.name_entry = tkinter.Entry(self.top_frame, width=10)
        self.show_score = tkinter.Label(self.middle_frame, text='Your score was:' + str(self.totalscore))
        self.show_score.pack()

        self.save_button = tkinter.Button(self.bottom_frame, text='Add Score', command=self.add)
        self.show_highscores = tkinter.Button(self.bottom_frame, text='Show Highscores', command=self.highscore_UI)
        self.back_button = tkinter.Button(self.bottom_frame, text='Main Menu', command=self.back)

        self.save_button.pack(side='left')
        self.show_highscores.pack(side='left')
        self.back_button.pack(side='left')

        self.prompt_name.pack(side='top')
        self.name_entry.pack(side='top')

        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()

    def highscore_UI(self):
        self.name_entry.destroy()
        self.prompt_name.destroy()
        self.show_score.destroy()
        self.save_button.destroy()
        self.adds.title("Highscores")
        for names in self.highscores:
            label = tkinter.Label(self.middle_frame, text=str(self.highscores.get(names)) + ",", font=("Helvetica", 20))
            label2 = tkinter.Label(self.middle_frame, text=names, font=("Helvetica", 20))
            label2.pack(side='left')
            label.pack(side='left')
        self.show_highscores.destroy()

    def back(self):
        self.adds.destroy()

    def add(self):
        name = self.name_entry.get()
        score = self.totalscore
        self.highscores[name] = score
        self.save()

    def save(self):
        messagebox.showinfo("Saved Successfully", "Your score was saved.")
        save_file = open('highscores.dat', 'wb')
        pickle.dump(self.highscores, save_file)
        save_file.close()


class Dice:
    def __init__(self):
        self.side_up = '0'

    def roll(self):
        dice_num = random.randint(1, 6)
        if dice_num == 1:
            self.side_up = '1'
        elif dice_num == 2:
            self.side_up = '2'
        elif dice_num == 3:
            self.side_up = '3'
        elif dice_num == 4:
            self.side_up = '4'
        elif dice_num == 5:
            self.side_up = '5'
        else:
            self.side_up = '6'

    def get_side_up(self):
        return self.side_up

    def set_side_up(self, side):
        self.side_up = side


dice1 = Dice()
dice2 = Dice()
dice3 = Dice()
dice4 = Dice()
dice5 = Dice()
dice_list = [dice1, dice2, dice3, dice4, dice5]


def main():
    # create a window
    root = tkinter.Tk()
    # call the GUI and send it the root menu
    # use _ as variable name because the variable will not be needed after instantiating GUI
    # the GUI itself will handles the remaining program logic
    _ = YahtzeeGUI(root)
    # control the mainloop from main instead of the class
    root.mainloop()


main()
