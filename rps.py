import random
import time


def tas_kagit_makas_RecepBATTAL():
    """
    This function is a normal rock-paper-scissors game with the addition of
    lizard and Spock. The game is played between the player and the computer.
    The player can choose between rock, paper, scissors, lizard, and Spock.
    The computer randomly selects one of these options. The game is played
    until one of the players win the first 2 matches. The player can exit the
    game at any time by typing 'exit'. After each game, the player can choose
    to play another game.
    """
    options = ["rock", "paper", "scissors", "lizard", "spock", "exit"]

    print("Welcome to Rock, Paper, Scissors, Lizard, Spock Game!")
    print("Rules:")
    print("Rock crushes scissors and lizard, scissors cuts paper and lizard")
    print("paper covers rock and disproves Spock")
    print("lizard poisons Spock and eats paper")
    print("Spock smashes scissors and vaporizes rock.")
    print("If you want to exit the game, type 'exit'.")
    print("Good luck!")

    game_count = 0

    while True:
        game_count += 1
        print(f"\nGame {game_count} is starting!")

        player_wins = 0
        computer_wins = 0
        round_num = 0

        while round_num < 3:
            round_num += 1
            print(f"\nRound {round_num}")

            while True:
                player_choice = input(
                    "Make your choice (rock/paper/scissors/lizard/spock): "
                ).lower()
                if player_choice == "exit":
                    print("The game has ended. Goodbye!")
                    return
                if player_choice in options:
                    break
                print("Invalid choice. Please try again.")

            computer_choice = random.choice(options)

            print(f"Your choice: {player_choice}")
            print(f"Computer's choice: {computer_choice}")

            if player_choice == computer_choice:
                print("It's a tie!")
            elif (
                (player_choice == "rock" and
                 computer_choice in ["scissors", "lizard"])
                or (player_choice == "paper" and
                    computer_choice in ["rock", "spock"])
                or (player_choice == "scissors" and
                    computer_choice in ["paper", "lizard"])
                or (player_choice == "lizard" and
                    computer_choice in ["spock", "paper"])
                or (player_choice == "spock" and
                    computer_choice in ["scissors", "rock"])
            ):
                print("You won!")
                player_wins += 1
            else:
                print("Computer won!")
                computer_wins += 1

            print(f"Score: You {player_wins} - {computer_wins} Computer")

            if player_wins == 2 or computer_wins == 2:
                break

        if player_wins == computer_wins:
            print("\nIt's a draw!")
        elif player_wins > computer_wins:
            print("\nCongratulations! You won the game!")
        else:
            print("\nUnfortunately, the computer won the game.")

        player_continue = input("Do you want to play another game? (yes/no): ")
        player_continue = player_continue.lower()
        if player_continue not in ["yes", "no"]:
            print("Invalid choice. The game has ended.")
            break

        print("Computer, do you want to play?")

        for i in range(1, 4):
            print("Computer is thinking" + "." * i)
            time.sleep(0.5)

        computer_continue = random.choice(["yes", "no"])

        if computer_continue == "yes":
            print("The computer wants to play")
        else:
            print("The computer doesn't want to play")

        if player_continue != "yes" and computer_continue != "no":
            print("The computer wanted to play, but you didn't.")
            break
        if player_continue != "yes" or computer_continue != "yes":
            print("The game is over. Thank you for playing!")
            break

        print("A new game is starting!")
    print("The game has ended. Goodbye!")


if __name__ == "__main__":
    tas_kagit_makas_RecepBATTAL()
