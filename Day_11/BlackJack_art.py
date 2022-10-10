logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

concealed_card = [
    "┌─────────┐",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "│░░░░░░░░░│",
    "└─────────┘"
    ]

def printConcealedCards(no):
  for index in concealed_card:
    print(f"{index}   "*no)

revealed_card = [
  "┌─────────┐",
  "│{:<2}       │",
  "│         │",
  "│         │",
  "│    {}    │",
  "│         │",
  "│         │",
  "│       {:>2}│",
  "└─────────┘"
]

card_values = [11,2,3,4,5,6,7,8,9,10,10,10,10]
card_nums = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
card_symbols = ["♥️","♦️","♣️","♠️"]


def printCards(cards_list,concealed_cards = 0):
  
  num = len(cards_list)
  if(concealed_cards > 0):
    num = 1
  for index in range(len(revealed_card)):
    for i in range(0,num+concealed_cards):
      str = revealed_card[index]
      if(i >= num):
        str = concealed_card[index]
      else:
        if(index == 1 or index == 7):
          str = str.format(card_nums[cards_list[i]["num"]])
        elif(index == 4):
          str = str.format(card_symbols[cards_list[i]["type"]])
      print(f"{str}   ",end="")
    print()