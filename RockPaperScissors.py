"""
This is a simple game of rock paper scissors against a bot.
"""

import random

def get_choices():
  """
  Receives the choice of the player
  """
  options = ["rock", "paper", "scissors"]
  while True:
    player_choice = input("Enter a choice (rock, paper, scissors): ").lower()
    if player_choice in options:
      break
    else:
      print("That is not an option. Try again.")

  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  """
  Checks which player won
  """
  global user_score
  global bot_score
  print (f"You chose {player}, computer chose {computer}")
  if player == computer:
    return "It's a tie!"
  elif player == "rock":
    if computer == "scissors":
      user_score += 1
      return f"Rock smashes scissors! You win!\nUser: {user_score}  Bot: {bot_score}"
    else:
      bot_score += 1
      return f"Paper covers rock! You lose.\nUser: {user_score}  Bot: {bot_score}"
  elif player == "paper":
    if computer == "rock":
      user_score += 1
      return f"Paper covers rock! You win!\nUser: {user_score}  Bot: {bot_score}"
    else:
      bot_score += 1
      return f"Scissors cuts paper! You lose.\nUser: {user_score}  Bot: {bot_score}"
  elif player == "scissors":
    if computer == "paper":
      user_score += 1
      return f"Scissors cuts paper! You win!\nUser: {user_score}  Bot: {bot_score}"
    else:
      bot_score += 1
      return f"Rock smashes scissors! You lose.\nUser: {user_score}  Bot: {bot_score}"

#Runs game
while True:
  global answer
  try:
    answer = int(input("Best out of how many games? "))
    if answer % 2 == 1:
      break
    else:
      print("Answer must be an odd integer. Try again.")
  except ValueError:
      print("Answer must be an odd integer. Try again.")

user_score = 0
bot_score = 0
while user_score < (answer//2 + 1) and bot_score < (answer//2 + 1):
  choices = get_choices()
  print(check_win(choices["player"], choices["computer"]))
if user_score == answer/2 + 1:
  print(f"You won the best of {answer} match!")
else:
  print(f"You lost the best of {answer} match")