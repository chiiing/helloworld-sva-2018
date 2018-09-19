# let the user know what's going on
print ("Welcome to Ching's MadLibs! \n ^_________^ ")
print ("Answer the questions below to play.")
print ("\n")
print ("-----------------------------------")


# variables

name = raw_input("Enter a male's name")
food1 = raw_input("Enter a kind of vagetable")
adjective = raw_input("Enter a adjective")
meat2 = raw_input("Enter a random kind of meat")
meat1 = raw_input("Enter another kind of meat you likes")
food3 = raw_input("Enter another kind of vegetable")




# Story

story = "Long long time ago, there was a " + food1 + " named " + name + ". " \
+ name + " was not a ordinary " + food1 + " , but a carnivorous and " + adjective + " " + food1 +"! " \
+ "Normally, " + name + " likes to stay at home with his " + meat2 + ". But recently, he is addicted to eat " \
+ meat1 + ". He is sooooooo addicted to " + meat1 + " so that he ignores his best friend " + meat2 \
+ ". " + meat2 + " is really upset, so he determines to escape from home and leave " + name + " forever. " \
+ "After " + name + "'s " + meat2 + " disappears, " + name + " still keep eating " + meat1 + ", but he knows," \
"something deep inside his heart is missing. " + name + " decides to get some help, and go to rehab center of meat and become a vegetarian. " \
+ "During his time in the rehab center, he meets his love of the life -- " + food3 + ". He thought he will never let " \
+ food3 + " go, he has to seize the opportunity to make things right again, so " + name + " and " + food3 + " live happily ever after and have a lot of vage babies." \

print ("\n")
print ("-----------------------------------")
print story