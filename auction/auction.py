import os

def clear():
  os.system('cls')  # for Windows

from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_hight_bidder(bidding_record):
   highest_bid = 0
   winner = ""
   for bidder in bidding_record:
      bid_amount = bidding_record[bidder]
      if bid_amount > highest_bid:
         highest_bid = int(bid_amount)
         winner = bidder
   print(f"The winner is the {winner} won with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name:")
    price = int(input("How much are you bidding: $"))
    bids[name] = price
    should_contine = input("Are there any other bidders? Type 'yes' or 'No'.")
    if should_contine == "no":
       bidding_finished = True
       find_hight_bidder(bids)
    elif should_contine == "yes":
       clear()








