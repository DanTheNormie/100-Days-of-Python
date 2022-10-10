from Day_11.BlackJack_art import *
import random
import os
from time import sleep



def generateRandomCard():
  card = {"type": random.randint(0, 3), "num": random.randint(0, 12)}
  return card



def printGameScore(ps,ds,hc):

  
  d_score = f"Dealer's Score : {ds}"
  if(hc>0):
    d_score += " + ?"

  p_score = f"Your Score : {ps}"
  
  print()
  print(p_score)
  print(d_score)
  print()

def printGame(
  players_card_list,
  dealers_card_list,
  player_score,
  dealer_score,              
  dealers_hidden_cards,
  is_first_time = False
):
  sleep(1)
  os.system('cls')

  print("Your hand :- ")
  printCards(players_card_list)
  print("Dealer's hand :- ")
  printCards(dealers_card_list, dealers_hidden_cards)

  if(not is_first_time):
    a = dealer_score
    if(dealers_hidden_cards>0):
      a = card_values[dealers_card_list[0]["num"]]
  
    printGameScore(player_score,a,dealers_hidden_cards)

def getScoreFromCardList(card_list):
  score = 0
  no_of_A = 0
  for i in card_list:
    card_value = card_values[i["num"]]
    if(card_value == 11):
      no_of_A += 1
    score += card_value

  
  while(score > 21 and no_of_A>0):
    score -= 10 
    no_of_A -=1
  return score



def addRandomCards(num,list):
  for i in range(num):
    list.append(generateRandomCard())


def decideGameState(ps,ds,play_state = "in_play",prints = True):
  msg = ""
  in_play = True
  if(ps <= 21 and play_state == "in_play"):
    in_play = True
  else:
    if (ds > 21):
      msg = "Dealer went bust. You Win. \n\n"
      in_play = False
    elif(ps > 21):
      msg = "Your Score is over 21. You lose. \n\n"
      in_play = False
    elif (ps > ds):
      msg = "You beat the dealer's hand, You Win. \n\n"
      in_play = False
    elif (ps < ds):
      msg = "Your score is less than dealer's score, You Lose. \n\n"
      in_play = False
    elif (ps == ds):
      msg = "Your score and the dealer's score are equal. Draw!!! \n\n"
      in_play = False
    else:
      print("how does this happen ? \n\n")
      in_play = True
    
  if((not in_play) and prints):
    print(f"Result :-\n\n  {msg}")
  return in_play

def canDealerHit(ds,card_list):

  probability_of_success = 0
  probability_of_failure = 0
  
  for i in card_values:
    if(ds+i <= 21):
      probability_of_success += 1
    else:
      probability_of_failure += 1
  
  if(probability_of_success>=probability_of_failure):
    return True
  else:
    return False

def start_game():
  player_card_list = []
  dealer_card_list = []
  dealers_hidden_cards = 0
  player_score = 0
  dealer_score = 0
  in_play = True

  for i in range(4):
    flag = True
    if(i%2==0):
      addRandomCards(1,player_card_list)
    else:
      addRandomCards(1,dealer_card_list)
      if(i==3):
        dealers_hidden_cards += 1
        flag = False
        
    player_score = getScoreFromCardList(player_card_list)
    dealer_score = getScoreFromCardList(dealer_card_list)
    
    printGame(
    player_card_list, 
    dealer_card_list, 
    player_score, 
    dealer_score, 
    dealers_hidden_cards,
    flag
  )
    
  while(in_play):
    print("Choose your action :\n1. Hit\n2. Stand\n4. Quit\n")
    play = input("Type a number from above : ")
  
    if (play == "1"):
      addRandomCards(1,player_card_list)
  
      player_score = getScoreFromCardList(player_card_list)

      in_play = decideGameState(player_score,dealer_score,"in_play",False)
      if(not in_play):
        
        printGame(player_card_list, dealer_card_list, player_score,dealer_score, 0)
        decideGameState(player_score,dealer_score)
      else:
        printGame(player_card_list, dealer_card_list, player_score,dealer_score, dealers_hidden_cards)
  
    elif (play == "2"):

      in_play = False

      dealer_score = getScoreFromCardList(dealer_card_list)
      printGame(player_card_list, dealer_card_list, player_score,dealer_score, 0)
      
      while(canDealerHit(dealer_score,dealer_card_list) or player_score > dealer_score):
      
        addRandomCards(1,dealer_card_list)
        dealer_score = getScoreFromCardList(dealer_card_list)
      
        printGame(player_card_list, dealer_card_list, player_score,dealer_score, 0)
      
      decideGameState(player_score,dealer_score,"over")

    elif(play == "4"):
      in_play = False
    
  if (input("Do you want to play a new game ? type y/n : ") == "y"):
    start_game()

print(logo)

if (input("Do you want to start the game ? type y/n : ") == "y"):
  start_game()
