import random
def play():
    user_input =  input('Enter R for rock, P for paper, S for Scissors: ').lower()
    computer_choice = random.choice(['r', 'p', 's'])
    if user_input == computer_choice:
        return "it's a tie"
    #r > s, s > p, and p > r
    if is_win(user_input, computer_choice):
        return 'You have won'
    return 'you have lost'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, and p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or (player == 'p' and opponent == 'r'):
        return True

print(play())



