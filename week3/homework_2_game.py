from random import *
import random
import time
import sys


name = raw_input("Enter your name > ")


# charactors setting

gender = ['a female', 'a male', 'an agender', 'a transgender']
race = ['human', 'elf', 'hobbit', 'dworf']
raceAttribue = ['demigod-', 'halfdemon-', 'dark ', '']


# Pick random attributes from the charactors setting list

g = sample(gender, 1) 
gender4print = g[0]

rA = sample(raceAttribue, 1)
raceAttribue4print = rA[0]

r = sample(race, 1)
race4print = r[0]



# Charactors setting list

charactor = "You are " + gender4print + " " + raceAttribue4print + race4print + "."


# mission

mission = "\033[5;31;47m" + 'Your mission is to rescue the princess from a dragon.' + "\033[0m"



# Location Setting
 
location = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
 
l = sample(location,  1)   # Pick a random item from the list
princessLocation = l[0]



# Graphic 

def printGraphic(graphic):
    if (graphic == "dragon"):
        print "                                     _/|__       "
        print "            _,-------,        _/ -|  \_     /~>. "
        print "         _-~ __--~~/\ |      (  \   /  )   | / | "
        print "      _-~__--    //   \\      \ *   * /   / | || "
        print "   _-~_--       //     ||      \     /   | /  /|   < HAHAHA! The princess is mine!"
        print "  ~ ~~~~-_     //       \\     |( . )|  / | || / "
        print "          \   //         ||    | VWV | | /  ///  "
        print "    |\     | //           \\ _/      |/ | ./ |   "
        print "    | |    |// __         _-~         \// |  /   "
        print "   /  /   //_-~  ~~--_ _-~  /          |\// /    "
        print " |  |   /-~        _-~    (     /   |/ / /       "
        print " /   /           _-~  __    |   |____|/          "
        print "|   |__         / _-~  ~-_  (_______  `\         "
        print "|      ~~--__--~ /  _     \        __\)))        "
        print " \               _-~       |     ./  \           "
        print "  ~~--__        /         /    _/     |          "
        print "        ~~--___/       _-_____/      /           "
        print "         _____/     _-_____/      _-~            "
        print "      /^<  ___       -____         -____         "
        print "         ~~   ~~--__      ``\--__       ``\      "
        print "                    ~~--\)\)\)   ~~--\)\)\)      "

    if (graphic == "dragonMad"):
        print "                                     _/|__       "
        print "            _,-------,        _/ -|  \_     /~>. "
        print "         _-~ __--~~/\ |      (  \   /  )   | / | "
        print "      _-~__--    //   \\      \ \   / /   / | || "
        print "   _-~_--       //     ||      \     /   | /  /|   < I will destroy you!!!!!!!"
        print "  ~ ~~~~-_     //       \\     |( . )|  / | || / "
        print "          \   //         ||    | VWV | | /  ///  "
        print "    |\     | //           \\ _/      |/ | ./ |   "
        print "    | |    |// __         _-~         \// |  /   "
        print "   /  /   //_-~  ~~--_ _-~  /          |\// /    "
        print " |  |   /-~        _-~    (     /   |/ / /       "
        print " /   /           _-~  __    |   |____|/          "
        print "|   |__         / _-~  ~-_  (_______  `\         "
        print "|      ~~--__--~ /  _     \        __\)))        "
        print " \               _-~       |     ./  \           "
        print "  ~~--__        /         /    _/     |          "
        print "        ~~--___/       _-_____/      /           "
        print "         _____/     _-_____/      _-~            "
        print "      /^<  ___       -____         -____         "
        print "         ~~   ~~--__      ``\--__       ``\      "
        print "                    ~~--\)\)\)   ~~--\)\)\)      "


    if(graphic == "princess"):
        print "   _                           _           "
        print "  / `._        \+O+/        _.' \          "
        print " ( @ : `.      //`\\      .' : @ )         "
        print "  \  `.  `.   ((> <))   .'  .'  /          "
        print "   \;' `.  `.((( o ))).'  .' `;/    < Save me ~~~ "
        print "    \`.  `.  ((()=()))  .'  .'/            "
        print "     ) :-._`/`(( Y ))`\'_.-: (             "
        print "     (`..../ /(_ * _)\ \....')             "
        print "     >---/ /  )   (  \ \---<               "
        print "     / .'.\ \_/\\_//\_/ /.'. \             "
        print "     |o _.-\/_) '*' (_\/-._ o|             "
        print "     |`'   ;/         \;   `'|             "
        print "     |.o_.-/           \-._o.|             "
        print "       |._/             \_.|               "
        print "         /               \                 "
        print "        /                 \                "
        print "       /                   \               "
        print "      /                     \              "
        print "     /                       \             "
        print "     `----....._____.....----'             "

    if(graphic == "fairy"):
        print "            |^^|"
        print "  EEEEE     |__|     EEEEE  "
        print "  EEEEEEE  (    )   EEEEEEE"
        print "  EEEEEEE  (|**|)  EEEEEEE  "
        print "    EEEEE  /\  /\  EEEEE    "
        print "      EEEEE)_||_(EEEEE      "
        print "        ee/|\__/|\ee   |    "
        print "       eee|( __ )|eee- * -  "
        print "      eeee||\  /||eeee/|    "
        print "       ee ||/  \|| ee/      "
        print "        __/(    )\__/       "
        print "         -  \  /  -         "
        print "            |  |            "
        print "            |  |            "
        print "            |  |            "
        print "            |__|            "
        print "            \/\/            "


    if(graphic == "title"):
        print "       __                                                              "
        print "      /\ \                                                             "
        print "      \_\ \  __  __    ___      __      __    ___     ___     ____     "
        print "      /'_` \/\ \/\ \ /' _ `\  /'_ `\  /'__`\ / __`\ /' _ `\  /',__\    "
        print "     /\ \L\ \ \ \_\ \/\ \/\ \/\ \L\ \/\  __//\ \L\ \/\ \/\ \/\__, `\   "
        print "     \ \___,_\ \____/\ \_\ \_\ \____ \ \____\ \____/\ \_\ \_\/\____/   "
        print "      \/__,_ /\/___/  \/_/\/_/\/___L\ \/____/\/___/  \/_/\/_/\/___/    " 
        print "                                /\____/                                "
        print "                                \_/__/                                 "
        print "       ____        ____                                                " 
        print "     /|  _ \      /\  _`\                                              "
        print "     |/\   |      \ \ \/\ \  _ __    __       __     ___     ___       "
        print "      \// __`\/\   \ \ \ \ \/\`'__\/'__`\   /'_ `\  / __`\ /' _ `\     "
        print "      /|  \L>  <_   \ \ \_\ \ \ \//\ \L\.\_/\ \L\ \/\ \L\ \/\ \/\ \    "
        print "      | \_____/\/    \ \____/\ \_\\ \__/.\_\ \____ \ \____/\ \_\ \_\   "
        print "       \/____/\/      \/___/  \/_/ \/__/\/_/\/___L\ \/___/  \/_/\/_/   "
        print "                                              /\____/                  "
        print "                                              \_/__/                   "
        print "                                                                       "

# Roll Dice Function

def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print "You made " + str(result) + " points of damage!" # + str(maxNum)

    if result <= difficulty:
        print "Miss! Trying again...."
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty)

    return result



# Guess location

def challenge1():

    print "But there are almost 20 cells in the dungeon, the fairy don't know which one is the princess locked."
    playerGuess = raw_input("You have to guess Which cave is the princess in? (enter a number from 1 - 20)")
    
    if (princessLocation > playerGuess):
        printGraphic("dragon")
        print "The dragon is here. He looks angry..."


    elif (princessLocation < playerGuess):
        printGraphic("dragon")
        print "The dragon is here. He looks angry..."
    
    else:
        print "\033[5;31;47m" + "You found the princess! The dragon is very angry now!!!!!!!!!!!!!!" + "\033[0m"
        printGraphic("dragonMad")
        challenge2()
        

# Attact

def challenge2():
    print "Now, try to kill the dragon with your weapon!!!"
    raw_input("press enter >")
    difficulty = 10
    roll = rollDice(0, 20, difficulty)
    if (roll >= difficulty):
        printGraphic("princess")
        print "\033[5;31;47m" + "You defeated the dragon and save the princess~~~" + "\033[0m"


# Entrance

def entrance():
    time.sleep(1) 
# font: Larry 3D
    print "-"*31 + " welcome to " + "-"*32
    printGraphic("title")
    print "                                                                       "
    print "-"*75
    time.sleep(1)
    print " "
    print " "
    print "This is the identity for your great advanture------------------------------" +"\n"
    print " "
    print charactor
    print " "
    print "-"*75
    raw_input("press enter >")



def startPoint():
    time.sleep(1)
    print " "
    printGraphic("fairy")
    print " "
    print name + ", welcome! you are chosen to be part of the great adventure ever." 
    print "You found yourself in a forest, and there's a fairy standing infront of you."
    raw_input("press enter to talk to the fairy >")
    print " "
    print "Fairy: " + name + ", thank you for coming. My princess was kidnap by a evil dragon, would you please rescue her?"
    print " "
    question = raw_input("Do you want to rescue the princess? > (Yes/No)")

    if (question == "Yes"):
        print "\n" + "Fairy: Good! You're very brave!" + "\n"
        time.sleep(1)  
        print mission  + "\n"
        time.sleep(1)
        print "The fairy lead you to the dragon's castle."
        raw_input("Search the dungeon >")
        print " "

    elif (question == "No"): 
        print "Bye! Loser~~~"
    
    else:
        print "Try again"
        print question


def main():
    entrance()
    startPoint()
    challenge1()

main()







