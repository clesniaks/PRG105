class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, right_answer):
        self.question = question
        self.a1 = answer_1
        self.a2 = answer_2
        self.a3 = answer_3
        self.a4 = answer_4
        self.r_A = right_answer

    def get_question(self):
        return self.question

    def get_a1(self):
        return self.a1

    def get_a2(self):
        return self.a2

    def get_a3(self):
        return self.a3

    def get_a4(self):
        return self.a4

    def get_ra(self):
        return self.r_A

    def set_question(self, new_question):
        self.question = new_question

    def set_a1(self, new_a1):
        self.a1 = new_a1

    def set_a2(self, new_a2):
        self.a2 = new_a2

    def set_a3(self, new_a3):
        self.a3 = new_a3

    def set_a4(self, new_a4):
        self.a4 = new_a4

    def set_ra(self, new_ra):
        self.r_A = new_ra
        
