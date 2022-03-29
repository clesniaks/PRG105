import Question


def main():
    q1 = Question.Question("What is the rarest M&M color?", "Brown", "Red", "Green", "Yellow", 1)
    q2 = Question.Question("Which country consumes the most chocolate per capita?", "Greenland", "Switzerland", "United States", "Mexico", 2)
    q3 = Question.Question("What is the most consumed manufactured drink in the world?", "Pepsi", "Coke", "Coffee", "Tea", 4)
    q4 = Question.Question("Which of these foods items never spoil?", "Honey", "Pecans", "Lemon Juice", "Milk", 1)
    q5 = Question.Question("Which country invented ice cream?", "China", "United States", "Germany", "U.K.", 1)
    q6 = Question.Question("What is the rarest M&M color?", "Brown", "Red", "Green", "Yellow", 1)
    q7 = Question.Question("Which country consumes the most chocolate per capita?", "Greenland", "Switzerland", "United States", "Mexico", 2)
    q8 = Question.Question("What is the most consumed manufactured drink in the world?", "Pepsi", "Coke", "Coffee", "Tea", 4)
    q9 = Question.Question("Which of these foods items never spoil?", "Honey", "Pecans", "Lemon Juice", "Milk", 1)
    q10 = Question.Question("Which country invented ice cream?", "China", "United States", "Germany", "U.K.", 1)
    store = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
    player1_score = 0
    player2_score = 0
    question_count = 0
    print("Welcome to food trivia! Player one will go first")
    for place in store:
        print("\n")
        if question_count == 5:
            print('_'*34)
            print("It's Player 2's turn")
            print('_'*34)
        print(place.get_question())
        print("1. " + place.get_a1())
        print("2. " + place.get_a2())
        print("3. " + place.get_a3())
        print("4. " + place.get_a4())
        guess = int(input("Please enter the number of the correct answer: "))
        if question_count >= 5:
            if guess == place.get_ra():
                print("That is correct!")
                player2_score += 1
        else:
            if guess == place.get_ra():
                print("That is correct!")
                player1_score += 1
        question_count += 1
    print('_'*34)
    print("Player 1 got " + str(player1_score) + " Points and Player 2 got " + str(player2_score) + " Points")
    if player1_score == player2_score:
        print("Both Players Tied!")
    elif player1_score > player2_score:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")


main()
