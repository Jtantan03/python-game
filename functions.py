# from math import inf 

# id
# enumerate
# Setup



# yes_no = ["yes", "no"]
# directions = ["left", "right", "forward", "backward"]
 
# Introduction
# def starting_game():
#     global name
#     yes_no = ["yes", "no"]
#     directions = ["left", "right", "forward", "backward"]
#     name = input("What is your name, adventurer?\n")
#     print("Greetings, " + name + ". Let us go on a quest!")
#     print("You find yourself on the edge of a dark forest.")
#     print("Can you find your way through?\n")
 
# # Start of game
#     response = ""
#     while response not in yes_no:
#         response = input("Would you like to step into the forest?\nyes/no\n")
#         if response == "yes":
#          print("You head into the forest. You hear crows cawwing in the distance.\n")
#         elif response == "no":
#             print("You are not ready for this quest. Goodbye, " + name + ".")
#             quit()
#         else: 
#             print("I didn't understand that.\n")
 
# # Next part of game
#     response = ""
#     while response not in directions:
#         print("To your left, you see a bear.")
#         print("To your right, there is more forest.")
#         print("There is a rock wall directly in front of you.")
#         print("Behind you is the forest exit.\n")
#         response = input("What direction do you move?\nleft/right/forward/backward\n")
#         if response == "left":
#             print("The bear eats you. Farewell, " + name + ".")
#             quit()
#         elif response == "right":
#             print("You head deeper into the forest.\n")
#         elif response == "forward":
#             print("You cannot scale the wall.\n")
#             response = "" 
#         elif response == "backward":
#             print("You leave the forest. Do you want to go back, " + name + ".")
#             new_game()
#         else:
#             print("I didn't understand that.\n")

# starting_game()

# def new_game():
#     global name
#     yes_no = ["yes", "no"]
#     # directions = ["left", "right", "forward", "backward"]
#     response = ""
#     while response not in yes_no:
#         if response == "yes":
#             starting_game()
#         elif response == "no":
#             print("You are not ready for this quest. Goodbye, " + name + ".")
#             quit()
# starting_game()
# def forest():
#     yes_no = ["yes", "no"]
#     directions = ["left", "right", "forward", "backward"]


# def starting_game():
#     print( """You are about to face your most scariest moment of your life, \n
#     telling you mother to shhhhh, "reason? "You were dared to do it" """)
#     print("""Any normal day is acceptable given that she is in the good mood \n
#     however you were dare to accomplisg it within 12 Hr period.""")
#     print("""Given that circumstances, you have to do it no matter what.\n
#      """)
#     print (""" you ask your self, what are the things you should plan to.\n
#     and you come up to an idea. To make an conversation to your mom and once she start \n
#     explaining you will say the magic word.""")

#     print( """However! the moment your mom came from home you notice that 
#      """)


# def scene1():
# def scene2():
# def scene3():
# def scene4():
# def scene5():


# def new_game():
# def end_game():


from random import choice
import time
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        (mins, secs)
        # print(time_sec)
        time.sleep(1)
        time_sec -= 1
        if time_sec == 4:
            print("""\033[34m                   _    
                  | |   
    _ __ ___   ___| | __
   | '__/ _ \ / __| |/ /
   | | | (_) | (__|   < 
   |_|  \___/ \___|_|\_\.
                       
                       \033[37m""")
        if time_sec == 3:
            print("""\033[31m    _ __   __ _ _ __   ___ _ __ 
   | '_ \ / _` | '_ \ / _ \ '__|
   | |_) | (_| | |_) |  __/ |   
   | .__/ \__,_| .__/ \___|_|   
   | |         | |              
   |_|         |_|      \033[37m""")
        if time_sec == 2:
            print("""\033[33m
             _                        
            (_)                       
    ___  ___ _ ___ ___  ___  _ __ ___ 
   / __|/ __| / __/ __|/ _ \| '__/ __|
   \__ \ (__| \__ \__ \ (_) | |  \__ \

   |___/\___|_|___/___/\___/|_|  |___/
  \033[37m  """)
        if time_sec == 1:
            print("""\033[32m
        _                 _   
       | |               | |  
    ___| |__   ___   ___ | |_ 
   / __| '_ \ / _ \ / _ \| __|
   \__ \ | | | (_) | (_) | |_ 
   |___/_| |_|\___/ \___/ \__|
                              
 \033[36m""")
print("""\033[35m __   __                                   _                 _     _                _             
 \ \ / /__  _   _    __ _ _ __ ___    __ _| |__   ___  _   _| |_  | |_ ___    _ __ | | __ _ _   _ 
  \ V / _ \| | | |  / _` | '__/ _ \  / _` | '_ \ / _ \| | | | __| | __/ _ \  | '_ \| |/ _` | | | |
   | | (_) | |_| | | (_| | | |  __/ | (_| | |_) | (_) | |_| | |_  | || (_) | | |_) | | (_| | |_| |
   |_|\___/ \__,_|  \__,_|_|  \___|  \__,_|_.__/ \___/ \__,_|\__|  \__\___/  | .__/|_|\__,_|\__, |
                                                                             |_|            |___/ """)
time.sleep(3)
print("""\033[31m
⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[33m⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
⠀\033[31m⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[33m⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
\033[31m⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀\033[33m⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
\033[31m⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇\033[33m⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
\033[31m⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿\033[33m⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
\033[31m⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀\033[33m⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
\033[31m⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀\033[33m⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
\033[31m⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀\033[33m⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
\033[31m⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀\033[33m⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
\033[32m⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀\033[33m⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀\033[33m⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀\033[33m⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀\033[32m⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀\033[32m⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
\033[32m⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\033[37m""")
time.sleep(5)
print("""\033[36m#    _____                     ______ _   _ _______ ______ _____             _                                     _       
#   |  __ \                   |  ____| \ | |__   __|  ____|  __ \           | |                                   | |      
#   | |__) | __ ___  ___ ___  | |__  |  \| |  | |  | |__  | |__) | __      _| |__   ___ _ __    _ __ ___  __ _  __| |_   _ 
#   |  ___/ '__/ _ \/ __/ __| |  __| | . ` |  | |  |  __| |  _  /  \ \ /\ / / '_ \ / _ \ '_ \  | '__/ _ \/ _` |/ _` | | | |
#   | |   | | |  __/\__ \__ \ | |____| |\  |  | |  | |____| | \ \   \ V  V /| | | |  __/ | | | | | |  __/ (_| | (_| | |_| |
#   |_|   |_|  \___||___/___/ |______|_| \_|  |_|  |______|_|  \_\   \_/\_/ |_| |_|\___|_| |_| |_|  \___|\__,_|\__,_|\__, |
#                                                                                                                     __/ |
#  \033[37m\033[33m""")
input("")
time.sleep(1)
while True:
    score = 0
    user_action = input("\033[33mEnter a choice (rock, paper, scissors): \033[37m")
    
    
    rock = """  ⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀
    ⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀
    ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇
    ⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿
    ⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏
    ⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁
    ⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀
    ⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀"""
    paper = """   ⠀⠀⠀⠀⠀⠀⠀  ⠀ ⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀
    ⠀ ⠀⠀⠀⠀     ⠀⠀⢀⡼⠋ ⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
     ⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀ ⠀⣰⠏ ⢀⣤⣤⣄⡀⠀
     ⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
     ⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
    ⠀ ⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀ ⠀⣠⠶⠋⠁⠀⠀⠀
     ⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
    ⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
    ⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
    ⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀
    ⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀
     ⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚"""
    scissors = """  ⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀
    ⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀
    ⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀
    ⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀ """

    possible_actions = (rock, paper, scissors)
    computer_action = choice(possible_actions)
    # print(f"\nYou chose\n {user_action}\n, computer chose\n {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "rock":
        if computer_action == scissors:
            score += 1
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{rock}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m  computer chose.\n")
            time.sleep(1)
            print("\033[33mRock smashes scissors!\033[37m")
            time.sleep(2)
            print("""\033[32m                               _       _ 
  _   _  ___  _   _  __      _(_)_ __ | |
 | | | |/ _ \| | | | \ \ /\ / / | '_ \| |
 | |_| | (_) | |_| |  \ V  V /| | | | |_|
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)
  |___/\033[37m""")
        elif computer_action == paper:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{rock}\033[36m \n \033[31m{computer_action}\033[37m   \033[33m computer chose.\n")
            time.sleep(1)
            print("\033[33mPaper covers rock!\033[37m")
            time.sleep(2)
            print("""\033[31m                      _                _ 
  _   _  ___  _   _  | | ___  ___  ___| |
 | | | |/ _ \| | | | | |/ _ \/ __|/ _ \ |
 | |_| | (_) | |_| | | | (_) \__ \  __/_|
  \__, |\___/ \__,_| |_|\___/|___/\___(_)
  |___/\033[37m""")
        elif computer_action == rock:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{rock}\033[36m \n \033[31m{computer_action}\033[37m   \033[33m computer chose.\n")
            time.sleep(1)
            print(f"\033[33mBoth players selected {user_action}.\033[37m")
            time.sleep(2)
            print("""\033[36m      _                    _ 
   __| |_ __ __ ___      _| |
  / _` | '__/ _` \ \ /\ / / |
 | (_| | | | (_| |\ V  V /|_|
  \__,_|_|  \__,_| \_/\_/ (_)\033[37m""")
    elif user_action == "paper":
        if computer_action == rock:
            score += 1
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{paper}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m computer chose.\n")
            time.sleep(1)
            print("\033[33mPaper covers rock!\033[37m")
            time.sleep(2)
            print("""\033[32m                               _       _ 
  _   _  ___  _   _  __      _(_)_ __ | |
 | | | |/ _ \| | | | \ \ /\ / / | '_ \| |
 | |_| | (_) | |_| |  \ V  V /| | | | |_|
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)
  |___/\033[37m""")
        elif computer_action == scissors:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{paper}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m computer chose.\n")
            time.sleep(1)
            print("\033[33mScissors cuts paper!.\033[37m")
            time.sleep(2)
            print("""\033[31m                      _                _ 
  _   _  ___  _   _  | | ___  ___  ___| |
 | | | |/ _ \| | | | | |/ _ \/ __|/ _ \ |
 | |_| | (_) | |_| | | | (_) \__ \  __/_|
  \__, |\___/ \__,_| |_|\___/|___/\___(_)
  |___/\033[37m""")
        elif computer_action == paper:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{paper}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m computer chose.\n")
            time.sleep(1)
            print(f"\033[33mBoth players selected {user_action}.\033[37m")
            time.sleep(2)
            print("""\033[36m      _                    _ 
   __| |_ __ __ ___      _| |
  / _` | '__/ _` \ \ /\ / / |
 | (_| | | | (_| |\ V  V /|_|
  \__,_|_|  \__,_| \_/\_/ (_)\033[37m""")
    elif user_action == "scissors":
        if computer_action == paper:
            score += 1
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{scissors}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m computer chose.\n")
            time.sleep(1)
            print("\033[33mScissors cuts paper!\033[37m")
            time.sleep(2)
            print("""\033[32m                               _       _ 
  _   _  ___  _   _  __      _(_)_ __ | |
 | | | |/ _ \| | | | \ \ /\ / / | '_ \| |
 | |_| | (_) | |_| |  \ V  V /| | | | |_|
  \__, |\___/ \__,_|   \_/\_/ |_|_| |_(_)
  |___/\033[37m""")
        elif computer_action == rock:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{scissors}\033[36m \n \033[31m{computer_action}\033[37m  \033[33m  computer chose.\n")
            time.sleep(1)
            print("\033[33mRock smashes scissors!\033[37m")
            time.sleep(2)
            print("""\033[31m                      _                _ 
  _   _  ___  _   _  | | ___  ___  ___| |
 | | | |/ _ \| | | | | |/ _ \/ __|/ _ \ |
 | |_| | (_) | |_| | | | (_) \__ \  __/_|
  \__, |\___/ \__,_| |_|\___/|___/\___(_)
  |___/ \033[37m""")
        elif computer_action == scissors:
            countdown(5)
            print(f"\n\033[33mYou chose\n \033[34m{scissors}\033[36m \n \033[31m{computer_action}\033[37m   \033[33m computer chose.\n")
            time.sleep(1)
            print(f"\033[33mBoth players selected {user_action}.\033[37m")
            time.sleep(2)
            print("""\033[36m      _                    _ 
   __| |_ __ __ ___      _| |
  / _` | '__/ _` \ \ /\ / / |
 | (_| | | | (_| |\ V  V /|_|
  \__,_|_|  \__,_| \_/\_/ (_)\033[37m""")
    else:
        print("\033[31minvalid action counts as loss\033[37m")
    print(score)
    play_again = input("\033[33mPlay again? (y/n): ")
    if play_again.lower() != "y":
        break

