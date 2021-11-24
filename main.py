import random

play_the_game = "Y"

while play_the_game == "Y":
  #Computer picks random
  computer_choices = ['ROCK','PAPER','SCISSORS']
  computer_picks = random.choice(computer_choices)

  #Player picks input
  player_picks = input('Please pick ROCK, PAPER or SCISSORS\n').upper()

  print(f'You picked {player_picks}. The computer picked {computer_picks}!')

  #take the first letter to make the if/else neater
  computer_picks = computer_picks[0]
  player_picks = player_picks[0]

  # If/else
  if player_picks == computer_picks:
    print("It's a draw")
  elif (player_picks == 'R' and computer_picks == 'S') or (player_picks == 'P' and computer_picks == 'R') or (player_picks == 'S' and computer_picks == 'P'):
    print("You win!")
  else:
    print ("You lose :|")
  play_the_game = input("Play again? (Y/N) ").upper()

print ("Thanks for playing. Goodbye!")
