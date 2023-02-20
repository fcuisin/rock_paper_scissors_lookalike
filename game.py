import random
from enum import IntEnum


class Action(IntEnum):
    Boar = 1
    Squirrel = 2
    Wolf = 3
    Lizard = 4
    Tourist = 5


victories = {
    Action.Boar: [Action.Squirrel, Action.Tourist],
    Action.Squirrel: [Action.Wolf, Action.Lizard],
    Action.Wolf: [Action.Boar, Action.Tourist],
    Action.Lizard: [Action.Wolf, Action.Boar],
    Action.Tourist: [Action.Lizard, Action.Squirrel]
}


def get_user_selection():
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action


def get_computer_selection():
    selection = random.randint(1, len(Action))
    action = Action(selection)
    return action


def determine_winner(user_action, computer_action):
    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. It's a tie!")
    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You win!")
    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose.")


def play_game():
    num_of_games = None
    played_games = 0

    num_of_games = int(input(f"Choose how many games you want to play: "))

    is_playing = True

    while is_playing:
        try:
            user_action = get_user_selection()
        except ValueError as e:
            print(
                f"Invalid selection. Enter a value between 1 and {len(Action)}!")
            continue

        computer_action = get_computer_selection()
        determine_winner(user_action, computer_action)
        played_games += 1

        if played_games >= num_of_games:
            is_playing = False
            play_again = input("Play again? (y/n): ")
            if play_again.lower() == "y":
                play_game()


play_game()
