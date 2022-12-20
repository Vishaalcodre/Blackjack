#Create a deal_card() function that uses the List below to *return* a random card. #11 is the Ace
import random
from replit import clear
from logo import art

#Create a function to assign the numbers in a deck of cards and return a random number from the deck of cards
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

#Create a function called calculate_score() that takes a List of cards as input and returns the score.
#Look up the sum() function to help you do this.
def calculate_score(list):

#Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game
  if sum(list) == 21 and len(list) == 2:
    return 0

#Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
  if 11 in list and sum(list) > 21:
    list.remove(11)
    list.append(1)

  else:
    return sum(list)

#Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(usr_score,cmp_score):
  if usr_score > 21 and cmp_score > 21:
    return "You went over. You lose 😤"
  elif usr_score == cmp_score:
    return "Draw"

  elif usr_score == 0:
    return "You won with a Blackjack! 😎"

  elif cmp_score == 0:
    return "You lose, opponent has a Blackjack 😲"
  elif usr_score > 21:
    return "You went over. You lose 😭"
  elif cmp_score > 21:
    return "Opponent went over, You win! 😉"
  elif usr_score > cmp_score:
    return "You win 😃"
  elif usr_score < cmp_score:
    return "You lose 😤"

def play_game():
  print(logo)

#Deal the user and computer 2 cards each using deal_card()
  usr_cards = []
  cmp_cards = []
  start_game = True

  for i in range(2):
    usr_cards.append(deal_card())
    cmp_cards.append(deal_card())

#The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
  while start_game:
    usr_score = calculate_score(usr_cards)
    cmp_score = calculate_score(cmp_cards)
    print(f"Your cards are {usr_cards} and the total of your cards is {usr_score}")
    print(f"Computer's first card {cmp_cards[0]}")

    if usr_score == 0 or cmp_score == 0 or usr_score > 21:

      start_game = False

    else:
#If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
      wanna_hit = input("Type 'y' to get another card, type 'n' to pass: ")
      if wanna_hit == 'y':
        usr_cards.append(deal_card())

      else:
        start_game = False

#Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
  while cmp_score != 0 and cmp_score < 17:
    cmp_cards.append(deal_card())
    cmp_score = calculate_score(cmp_cards)

  print(f"Your final hand: {usr_cards}, final score: {usr_score}")
  print(f"Computer's final hand: {cmp_cards}, final score: {cmp_score}")
  print(compare(usr_score,cmp_score))

#Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Would you like to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
  clear()
  play_game()
