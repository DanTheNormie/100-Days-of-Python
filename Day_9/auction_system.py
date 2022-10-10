from Day_9.auction_system_art import logo
import os
#HINT: You can call clear() to clear the output in the console.

print(logo)
print("Welcome to the secret auction program \n")

new_bids_exist = True
bid_log = {}

def add_bid(name,bid_amount):
  bid_log[name] =  bid_amount


while(new_bids_exist):
  name = input("What's your name ? : ")
  bid_amount = int(input("\nWhat's your bid ? : "))
  add_bid(name,bid_amount)

  if(input("\nAre there any other bidders ? type y/n : ").lower() == "n"):
    new_bids_exist = False
  os.system('cls')
  
highest_bid_info = {}

highest_bid = 0
for key in bid_log:
  if(bid_log[key] >= highest_bid):
    highest_bid = bid_log[key]
    bidder_name = key

print(f"\nThe winner is {bidder_name} with a bid of {highest_bid}")




