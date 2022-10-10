# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
import random
from blackJackArt import logo


def deal_card():
    """Function to return a random card from deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().



# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.
def calculate_score(cards):
    if sum(cards) == 21 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of
# the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace
# it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21,
# then the game ends.
# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card(
# ) function to add another card to the user_cards List. If no, then the game has ended.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user
# both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score
# is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(your_score, machine_score):
    if your_score == machine_score:
        return 'Its a Draw'
    elif machine_score == 0:
        return 'You Lose. Opponent has a Blackjack'
    elif your_score == 0:
        return 'You Win. You Have a Blackjack'
    elif your_score > 21:
        return 'You Went over. You Lose.'
    elif machine_score > 21:
        return 'Opponent went over. You Win'
    elif your_score > machine_score:
        return 'You Win'
    else:
        return 'You Lose'


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    is_over = False

    while not is_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\t Your cards: {user_cards}. current score: {user_score}")
        print(f"\t Computer's First Hand: {computer_cards[0]}")
        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_over = True
        else:
            hit = input("Type 'y' to get another card. Type 'n' to pass: ")
            if hit == 'y':
                user_cards.append(deal_card())
            else:
                is_over = True

    # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be
    # repeated until the game ends.

    # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long
    # as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\t Your Final hand is: {user_cards}, Final Score: {user_score} ")
    print(f"\t Computer's Final hand is: {user_cards}, Computer's Final Score: {user_score} ")
    print(compare(user_score, computer_score))


while input("Do You want to play a Game of BlackJack? Type 'y' or 'n': ") == 'y':
    play_game()

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game
# of blackjack and show the logo from art.py.
