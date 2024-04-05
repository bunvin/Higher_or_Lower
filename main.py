import game_data
import random

print("welcome to the higher lower game!!")


score = 0
first_choice = random.choice(game_data.data)
second_choice = random.choice(game_data.data)

option_A_print = print(f"Option A: {first_choice['name']},\na {first_choice['description']} has {first_choice['follower_count']} followers.")

print ("\nvs\n")

option_B_print = print(f"Option B: {second_choice['name']}, a {second_choice['description']}")

higher_or_lower = input("is option A has higher or lower followers than option B ? ")

if higher_or_lower == "higher":
  if first_choice['follower_count'] > second_choice['follower_count']:
    print("you are correct")
    first_choice = second_choice
    score += 1
  else:
    print("you are wrong")
    print(f"your score is {score}")