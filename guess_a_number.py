import random

def play_game():
    computer_number = random.randint(1,100)

    number_of_guesses = 0
    level_choice = input("What level do you want to play? Type 'e' for easy level or type 'h' for hard level. ").lower()

    while True:
        if level_choice == "e":
            number_of_guesses = 10
            break
        elif level_choice == "h":
            number_of_guesses = 5
            break
        else:
            print(f"Invalid choice. Try again")
            level_choice = input("What level do you want to play? Type 'e' for easy level or type 'h' for hard level. ").lower()


    while number_of_guesses > 0:
        player_guess = input("Guess the number (1-100) ")

        if not player_guess.isdigit():
            print("Invalid input. Please try again.")
            continue

        player_guess = int(player_guess)
        number_of_guesses -= 1

        if player_guess == computer_number:
            print(f"*********** You guessed the number! ***********")
            new_game = input("Do you want to play again? Type 'y' for yes or 'n' for no. ").lower()
            if new_game == "y":
                play_game()
            else:
                print("Goodbye!")
                break

        if number_of_guesses == 0:
            print(f"*********** You lost! ***********")

            new_game = input("Do you want to play again? Type 'y' for yes or 'n' for no. ").lower()
            if new_game == "y":
                play_game()
            else:
                print("Goodbye!")
                break
        else:
            if player_guess > computer_number:
                print("*******************************************")
                print("Too high. Try again.")

            elif player_guess < computer_number:
                print("*******************************************")
                print("Too low. Try again.")

            print("*******************************************")
            print(f"You have {number_of_guesses} guesses left.")

play_game()