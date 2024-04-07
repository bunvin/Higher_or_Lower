import random
from replit import clear

import game_data

print("welcome to the higher lower game!!\n")

def new_game():
  score = 0
  game_over = False
  first_choice = random.choice(game_data.data)
  second_choice = random.choice(game_data.data)
  
  while not game_over:
    print(f"Option A: {first_choice['name']},a {first_choice['description']} \nhas {first_choice['follower_count']}M followers.")
    
    print("\nVS.\n")
    
    print(f"Option B: {second_choice['name']}, a {second_choice['description']}\n")
    
    user_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
      
    if user_choice == "A":
       if first_choice['follower_count'] > second_choice['follower_count']:
         print("\nyou are correct !")
         score += 1
         print(f"your score is {score}\n")
         first_choice = second_choice
         second_choice = random.choice(game_data.data)
       else:
         print(f"\nyou are wrong ! \n{second_choice['name']} has {second_choice['follower_count']} followers")
         print(f"your score is {score}")
         game_over = True
    
    elif user_choice == "B":
         if first_choice['follower_count'] < second_choice['follower_count']:
           print("\nyou are correct !")
           score += 1
           print(f"your score is {score}\n")
           first_choice = second_choice
           second_choice = random.choice(game_data.data)
         else:
           print(f"\nyou are wrong ! \n{second_choice['name']} has {second_choice['follower_count']} followers")
           print(f"your score is {score}")
           game_over = True
    else:
      print("invalid input")
      game_over = True

  play_again = input("\nwould you like to play a game? type 'y' or 'n': ").lower()
  
  if play_again == "y":
    clear()
    new_game()
  else:
    print("thank you for playing")
  
new_game()