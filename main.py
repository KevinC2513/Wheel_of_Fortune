import Midterm


def get_player_name(num):
    player_name = input(f"Player {num}, please enter your name")
    return player_name


def guessed_before(guessed_letters, user_guess):
    return user_guess in guessed_letters


def main():
    puzzle = Midterm.get_wheel_puzzles()
    wheel_value = Midterm.get_wheel_values()
    random_puzzle = Midterm.choose_puzzle(puzzle)
    solved_puzzle = Midterm.turn_puzzle_into_underscores(random_puzzle)
    puzzle_with_characters_and_underscores = random_puzzle
    # mixed_puzzle = Midterm.change_puzzle_to_underscore(puzzle)
    # mixed puzzle's original value is just _____ so it can be joined later on, this is bc there are no
    # letters guessed at the start

    player_1_name = get_player_name(1)
    player_2_name = get_player_name(2)
    player_3_name = get_player_name(3)

    player_1 = Midterm.Player(player_1_name, 0)
    player_2 = Midterm.Player(player_2_name, 0)
    player_3 = Midterm.Player(player_3_name, 0)

    current_player = player_1

    score = 0

    guessed_letters = []

    print(current_player.get_name(), "Player is the current player with", current_player.get_score(), "dollars")
    print(f"The Puzzle is {solved_puzzle}")
    while Midterm.are_letters_left_to_guess(solved_puzzle) == True:
        print(random_puzzle)
        playornoplay = input("Would you like to spin or solve? Input 1 for spin or 2 for solve")
        if playornoplay == "1":
            spin_value = Midterm.spin_wheel(wheel_value)
            if spin_value == "-1":
                print("Your spin is: Bankrupt!")
                current_player.set_score(0)
                current_player = Midterm.change_player(current_player, player_1, player_2, player_3)
                print(current_player.get_name())
                print("You have", current_player.get_score(), "dollars")

            elif spin_value == "-2":
                print("Your spin is: Lose Turn!")
                current_player = Midterm.change_player(current_player, player_1, player_2, player_3)
                print(current_player.get_name())
                print("You have", current_player.get_score(), "dollars")

            else:
                print(f"The value of this spin is {spin_value}")
                user_guess = input("Please guess a vowel or consonant")[0].lower()
                guessed = guessed_before(guessed_letters, user_guess)
                if guessed == True:
                    print("You entered a repeat, You lose your turn!")
                    current_player = Midterm.change_player(current_player, player_1, player_2, player_3)
                    print(current_player.get_name())
                    print("You have", current_player.get_score(), "dollars")

                if Midterm.count_number_of_times_in_puzzle(user_guess, random_puzzle) > 0:
                    guessed_letters.append(user_guess)
                    solved_puzzle = Midterm.show_letter_in_solved_puzzle(user_guess, solved_puzzle, random_puzzle)
                    print(solved_puzzle)
                    number_of_times_a_letter_in_word = Midterm.count_number_of_times_in_puzzle(user_guess,
                                                                                               random_puzzle)
                    score = Midterm.compute_player_score(current_player, number_of_times_a_letter_in_word, spin_value)
                    current_player.set_score(score)
                    print("You have", current_player.get_score(), "dollars")

                else:
                    print("Your letter is not in the puzzle")
                    solved_puzzle = Midterm.show_letter_in_solved_puzzle(user_guess, solved_puzzle, random_puzzle)
                    print(puzzle_with_characters_and_underscores)
                    current_player = Midterm.change_player(current_player, player_1, player_2, player_3)
                    print(current_player.get_name())
                    print("You have", current_player.get_score(), "dollars")

        elif playornoplay == "Solve" or "solve":
            user_guess_solve = input("What is the Puzzle?").lower()
            if user_guess_solve == random_puzzle.lower():
                print(f"{current_player.get_name()} WINS with {current_player.get_score()} DOLLARS")
            break


main()
