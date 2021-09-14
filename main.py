import random


def get_response(user_input):
  responses = [
    "So cool!",
    "OMG!",
    "Thank you!",
    "Impressive!",
    "Very nice program!",
    "Nice programming!",
    "I like this very much!"
  ]
  return random.choice(responses)



def start_chat():
  end_character = 'end'

  user_input = input("Hello, how are you? (Type [end] to end the program!\n")

  while user_input != end_character:
    user_input = input(get_response(user_input) + "\n")



if __name__ == "__main__":
  start_chat()