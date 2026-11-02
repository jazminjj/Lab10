# my_main.py
# Author: Jazmin Joseph

from my_assistant import MenuHelper
from my_tool import MenuBoard

MENU = {
    "latte": 4.50,
    "cappuccino": 4.25,
    "iced coffee": 3.75,
    "blueberry muffin": 3.00,
    "croissant": 2.75,
}

menu_board = MenuBoard(MENU)
bot = MenuHelper("Mocha", "You help customers with menu items and prices.", menu_board)

print("Type a message, or type quit to stop.")
user_message = input("You: ")
while user_message != "quit":
    print(f"{bot.name}: {bot.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(bot.history)}")
