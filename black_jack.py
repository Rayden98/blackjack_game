## The imports 
import art
import random

## The variables
suit = [1,2,3,4,5,6,7,8,9,10,10,10,10]

decks = []
for n in range(0,8):
  
  four_suits = {}
  four_suits["suit"] = suit.copy()
  four_suits["number"] = n
  decks.append(four_suits)


  
print(decks)

print(art.logo)
"""
Do you want to play a game of Blackjack? Type 'y' or 'n':


   Your cards: [11, 5], current score: 16
   Computer's first card: 9
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [5, 7, 1], current score: 13
   Computer's first card: 9
Type 'y' to get another card, type 'n' to pass: y
   Your cards: [5, 7, 1, 10], current score: 23
   Computer's first card: 9
   Your final hand: [5, 7, 1, 10], final score: 23
   Computer's final hand: [9, 3, 4, 2], final score: 18
You went over. You lose 😭
Do you want to play a game of Blackjack? Type 'y' or 'n': 
"""

#want_play = print(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))

#Creating my own pair of cards and the pair of card for the machine\
my_random_1 = ""
my_random_2 = ""
machine_random_1 = ""
machine_random_2 = ""
dictionary_cards_in_game = {}
#Get my randoms card 
def get_my_randoms():
  my_dictionary_randoms = dict ()
  my_random_1 = random.randint(0,7)
  my_random_2 = random.randint(0,12)
  
  my_dictionary = decks[my_random_1]
  my_number = my_dictionary["suit"][my_random_2]

  if my_number == "_":
    its_number = False 
    while its_number == False: 
      my_dictionary_randoms = dict ()
      my_random_1 = random.randint(0,7)
      my_random_2 = random.randint(0,12)
    
      my_dictionary = decks[my_random_1]
      my_number = my_dictionary["suit"][my_random_2]
      if not my_number == "_":
        its_number = True
  
  #Replacing with "_"
  decks[my_random_1]['suit'][my_random_2] = "_"
  
  my_dictionary_randoms["card"] = my_number
  return my_dictionary_randoms

def get_machine_randoms():
  machine_dictionary_randoms = dict ()
  machine_random_1 = random.randint(0,7)
  machine_random_2 = random.randint(0,12)

  machine_dictionary = decks[machine_random_1]
  machine_number = machine_dictionary['suit'][machine_random_2]
  if machine_number == "_":
    its_number = False 
    while its_number == False: 
      machine_dictionary_randoms = dict ()
      machine_random_1 = random.randint(0,7)
      machine_random_2 = random.randint(0,12)
    
      machine_dictionary = decks[machine_random_1]
      machine_number = machine_dictionary['suit'][machine_random_2]
      if not machine_number == "_":
        its_number = True
      
  #Replacing with "_"
  decks[machine_random_1]['suit'][machine_random_2] = "_"

  print(decks)
  machine_dictionary_randoms["card"] = machine_number
  
  return machine_dictionary_randoms

#First two cards 
count_of_my_cards = 0
count_of_machine_cards = 0
dictionary_randoms_my = "dictionary_randoms_my"

#get another card for me 
def get_another_card_me():
  global count_of_my_cards
  dictionary_cards_in_game[f"dictionary_randoms_my {count_of_my_cards}"] = get_my_randoms()
  count_of_my_cards = count_of_my_cards + 1
def get_another_card_machine():
  global count_of_machine_cards
  dictionary_cards_in_game[f"dictionary_randoms_machine {count_of_machine_cards}"]  = get_machine_randoms()
  count_of_machine_cards = count_of_machine_cards + 1


get_another_card_me()
get_another_card_me()
get_another_card_machine()
get_another_card_machine()

print(dictionary_cards_in_game)


list_of_my_cards = []
list_of_machine_cards = []

for n in range(count_of_my_cards):  
    print(count_of_my_cards)
    key = f"dictionary_randoms_my {n}"
    if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
        card = dictionary_cards_in_game[key]['card']
        list_of_my_cards.append(card)

print(list_of_my_cards)

for n in range(count_of_machine_cards):  
    print(count_of_machine_cards)
    key = f"dictionary_randoms_machine {n}"
    if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
        card = dictionary_cards_in_game[key]['card']
        list_of_machine_cards.append(card)

print(list_of_machine_cards)
def current_score():
  addition = 0
  for n in list_of_my_cards:
    addition += n
  return addition
def who_wins ():
  current_my_score = 0
  current_machine_score = 0
  for n in list_of_my_cards:
    current_my_score += n

  for n in list_of_machine_cards:
    current_machine_score += n
  print(current_machine_score)
  
  if current_my_score == 21: 
    if current_machine_score == 21:
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's cards: {list_of_machine_cards}, current score: {current_machine_score}")
      print("Both has Black Jack, PUSH1")
    else:
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}\n Black Jack You Won!!!!2")
  elif current_my_score > 21:
    if current_machine_score > 21:
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's cards: {list_of_machine_cards}, current score: {current_machine_score}")
      print("Both has Black Jack, PUSH3")
    else:
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's cards: {list_of_machine_cards}, current score: {current_machine_score}")
      print("Computer WON!!!!4")
  else: 
    if current_my_score > current_machine_score:
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's cards: {list_of_machine_cards}, current score: {current_machine_score}")
      print("You WON!!!!5")
    else: 
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's cards: {list_of_machine_cards}, current score: {current_machine_score}")
      print("Computer WON!!!!6")
current_score = current_score()

print(f"Your cards: {list_of_my_cards}, current score: {current_score}")
print(f"Computer's first card: {list_of_machine_cards[0]}")

cycle_of_want_another = True
while cycle_of_want_another == True: 
    want_anothercard = input("Type 'y' to get another card, type 'n' to pass: y, type 'd' for double the bet\n")
    
    if want_anothercard == 'y':
      get_another_card_me()
      print(dictionary_cards_in_game)
      list_of_my_cards.clear()
      for n in range(count_of_my_cards):  
        print(count_of_my_cards)
        key = f"dictionary_randoms_my {n}"
        if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
            card = dictionary_cards_in_game[key]['card']
            
            list_of_my_cards.append(card)
      
    
      print(list_of_my_cards)
      
      current_my_score = 0
      current_machine_score = 0
      for n in list_of_my_cards:
        current_my_score += n
    
      print(f"Your cards: {list_of_my_cards}, current score: {current_my_score}")
      print(f"Computer's first card: {list_of_machine_cards[0]}")
      who_wins()
    elif want_anothercard == 'n':
       
      current_my_score = 0
      current_machine_score = 0
      for n in list_of_my_cards:
        current_my_score += n
    
      for n in list_of_machine_cards:
        current_machine_score += n
      print(list_of_machine_cards)
      print(current_machine_score)
      
      
      if 19 <= current_machine_score <= 20:
        number_random_about = random.randint(0,10)
        if number_random_about > 8:
          get_another_card_machine()
          print(dictionary_cards_in_game)
          list_of_machine_cards.clear()
          for n in range(count_of_machine_cards):  
            print(count_of_my_cards)
            key = f"dictionary_randoms_machine {n}"
            if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
                card = dictionary_cards_in_game[key]['card']
            
                list_of_machine_cards.append(card)
                
    
        print(list_of_machine_cards)
        
      elif 17 <= current_machine_score < 19:
        number_random_about = random.randint(0,10)
        if number_random_about > 7:
          get_another_card_machine()
          print(dictionary_cards_in_game)
          list_of_machine_cards.clear()
          for n in range(count_of_machine_cards):  
            print(count_of_my_cards)
            key = f"dictionary_randoms_machine {n}"
            if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
                card = dictionary_cards_in_game[key]['card']
            
                list_of_machine_cards.append(card)
              
    
        print(list_of_machine_cards)
        
      elif 14 <= current_machine_score < 17:
        number_random_about = random.randint(0,10)
        if number_random_about > 5:
          get_another_card_machine()
          print(dictionary_cards_in_game)
          list_of_machine_cards.clear()
          for n in range(count_of_machine_cards):  
            print(count_of_my_cards)
            key = f"dictionary_randoms_machine {n}"
            if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
                card = dictionary_cards_in_game[key]['card']
            
                list_of_machine_cards.append(card)
      
    
        print(list_of_machine_cards)
    
      elif current_machine_score < 14:
        number_random_about = random.randint(0,10)
        if number_random_about > 0:
          get_another_card_machine()
          print(dictionary_cards_in_game)
          list_of_machine_cards.clear()
          for n in range(count_of_machine_cards):  
            print(count_of_my_cards)
            key = f"dictionary_randoms_machine {n}"
            if key in dictionary_cards_in_game and 'card' in dictionary_cards_in_game[key]:
                card = dictionary_cards_in_game[key]['card']
            
                list_of_machine_cards.append(card)
      
    
        print(list_of_machine_cards)
      who_wins()
      cycle_of_want_another = False




        
#elif want_anothercard == 'd':