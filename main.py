import random
from replit import clear
from game_data import data
from art import logo, vs


def random_selector(prev):
  account_gen = {}
  if prev in data:
    data_ = data
    data_.remove(prev)
    account_gen = random.choice(data_)
  else:
    account_gen = random.choice(data)
  return account_gen


def evaluate_score(a, b):
  if a["follower_count"] >= b["follower_count"]:
    return a
  else:
    return b


def higher_or_lower():

  print(logo)
  score = 0
  play_again = True
  prev_acc = {}

  while play_again:

    if prev_acc == {}:
      acc_a = random_selector(prev_acc)
    else:
      acc_a = prev_acc
    acc_b = random_selector(acc_a)

    print(
      f"    Compare A: {acc_a['name']}, a {acc_a['description']} from {acc_a['country']}."
    )

    print(f"\n{vs}\n")

    print(
      f"\n    Against B: {acc_b['name']}, a {acc_b['description']} from {acc_b['country']}. "
    )

    winner = evaluate_score(acc_a, acc_b)

    choice = input(
      "\n    Which account do you think has more followers? Type 'A' or 'B': "
    ).lower()

    if choice == 'a':
      selection = acc_a
    elif choice == 'b':
      selection = acc_b

    clear()
    print(logo)

    if selection == winner:
      score += 1
      print(f"\nYou're right! Your score: {score}.\n")
      if prev_acc == winner:
        prev_acc = {}
      else:
        prev_acc = winner

    elif selection != winner:
      print(f"\nYou're wrong! Your final score: {score}.\n")
      play_again = False


higher_or_lower()
