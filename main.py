import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
options = [ROCK, PAPER, SCISSORS]


def get_choices():
    player_choice = input(f"Enter a choice ({ROCK}, {PAPER}, {SCISSORS}) => ").lower()

    if player_choice not in options:
        print(f"Please enter only ({ROCK}, {PAPER}, {SCISSORS}) [{player_choice} is invalid!]")
        return None

    computer_choice = random.choice(options)
    return {"player": player_choice, "computer": computer_choice}


def check_win(player, computer):
    print(f"You chose => {player}, computer chose => {computer}")
    if player == computer:
        return "It's a tie"
    elif player == ROCK:
        return "Rock smashes scissors! You Win!" if computer == SCISSORS else "Paper covers rock! You Lose!"
    elif player == PAPER:
        return "Paper covers rock! You Win!" if computer == ROCK else "Scissors cuts paper! You Lose!"
    elif player == SCISSORS:
        return "Scissors cuts paper! You Win!" if computer == PAPER else "Rock smashes scissors! You Lose!"


def check_final_result(p_win, c_win, tie):
    if p_win == c_win:
        print('Final Result => TIE')
    elif p_win > c_win:
        print(f"Final Result => Player WIN!!! {p_win}/{tie}/{c_win}")
    else:
        print(f"Final Result => Computer WIN!!! {c_win}/{tie}/{p_win}")


limit = 10
count = 0
player_win = 0
computer_win = 0
tie_match = 0

while count < limit:
    choices = get_choices()
    if choices is None:
        continue

    result = check_win(choices['player'], choices['computer'])
    print(result)

    if "Win" in result:
        player_win += 1
    elif "Lose" in result:
        computer_win += 1
    else:
        tie_match += 1

    count += 1
    if count == 10:
        check_final_result(player_win, computer_win, tie_match)
