#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Nov 2021
# this is a text-based game for learning guide 3
# its name is Finding My Way Home!


def main():
    print("Welcome to Finding My Way Home!")
    print("This is a text-based game. If you have some ", end="")
    print("trouble during the story, ", end="")
    print("some hints might be dropped to help you!\n")
    print("You groggily open your eyes, ", end="")
    print("they strain against the odd-looking lights above.")
    print("A revolting, indistinguishable, foul stench fills your ", end="")
    print("lungs as you take a deep breath.")
    print("Unfamiliar noises blare in your ears as you struggle.")
    print("Looking around, you see your hands and feet are ", end="")
    print("bound to the table you lay upon.\n")

    while True:
        # get input for 1st scene
        action = input("> ")
        action1 = action.upper()
        if action1 == "SCREAM" or action1 == "YELL" or action1 == "SHOUT":
            print("Someone bonks your head and you fall unconscious.\n")
            break
        elif action1 == "BREAK" or action1 == "DESTROY" or action1 == "RIP":
            print("Whatever is holding you down is too strong to break.\n")
        elif action1 == "STAND" or action1 == "MOVE" or action1 == "UP":
            print("You're bound, you can't move.\n")
        else:
            print("That verb is unrecognized, try something else.")
            print("*HINT* use your voice.\n")

    print("You wake up and hear muffled voices in the next room.", end="")
    print(" Your mouth is taped shut.")
    print("Heavy steps become increasingly louder. ", end="")
    print("You hurry and try to break out of the restraints.")
    print("A hideous slimy fish-humanoid creature enters the room. ", end="")
    print("The tape silences your fearful screams.")
    print("Tears stream down your face and your heart starts to beat", end="")
    print(" erratically as the ugly monster peers its beady eyes into yours.\n")
    print("Fish-man: Hey could you please calm down, you are freaking me out.")
    print("Fish-man: I'm going to explain everything just stop panicking.")
    print("Fish-man: Do you understand? Nod yes or no.\n")

    while True:
        action2 = input("> ")
        action2 = action2.upper()
        if action2 == "YES":
            print("You settle down and nod your head yes.")
            print("Fish-man: Okay, good let me begin then.\n")
            break
        elif action2 == "NO":
            print("Fish-man: You need to calm down before ", end="")
            print("I start explaining, understand now?\n")
        else:
            print("You shrug your shoulders confused")
            print("Fish-man: I don't understand that response.")
            print("*HINT* enter yes or no.\n")

    print("Fish-man: Firstly, my name is Nobo.")
    print("Nobo: You are currently in the Fauna Colony, ", end= '')
    print("home of many Vrauqrids like myself.")
    print("Nobo: Around 800 years ago a toxic nerve agent was globally released.")
    print("Nobo: Humans were dying by the millions, some fled to bunkers ", end= '')
    print("others to the tiny underwater colonies. The rest died.")
    print("Nobo: We barely managed to survive in these colonies, ", end= '')
    print("eventually we started to evolve and mutate into what we are now, Vrauqrids.")
    print("Nobo: Part human, part aquatic animal.\n")
    print("Nobo: When it comes to you, we found you inside a cyrochamber. ")
    print("Nobo: Some ancient technology was salvaged and we were able ", end='')
    print("to uncover some things.")
    print("Nobo: It seems that you were some sort of researcher or scientist. ")
    print("Nobo: You with a small group of others were researching the ocean bottom.")
    print("Nobo: Some sort of creature attacked your submarine ", end= '')
    print("and you got into the cryo-chamber as a last resort we figure.")
    print("Nobo: You have been asleep for around 1789 years.")
    print("Nobo: You are probably the last living human left on Earth.")
    print("Nobo: You have been sleeping in our infirmary for a month now.")
    print("Nobo: We have underwater tsunamis so its just expected to restrain patients like this.")
    print("Nobo: I'm going to remove the tape and restraints now so you can answer one of my questions.\n")

    print("Nobo unties your hands and feet and takes of the tape.")
    print("You sit up and can now breath more clearly.")
    print("The creature in front of you still scares you but it seems oddly nice.")
    print("Nobo: Do you remember your name?\n")

    while True:
        action3 = input(">  ")
        action3 = action3.upper()
        if action3 == "YES":
            print("Nobo: Nice!")
            print("A goofy smile is plastered on its face, displaying its sharpended yellow teeth.\n")
            break
        elif action3 == "NO":
            print("Nobo: You can choose a new name.\n")
            break
        else:
            print("Nobo: It's a simple yes or no awnser.")
            print("Yes or no?\n")

    print("So what's your name?")
    name = input(">  ")

    print("\nNobo: Good to offically meet you {0}.".format(name))
    print("Nobo: I know that we got off on the wrong foot, rather flipper...")
    print("Nobo starts chuckling at his own joke.")
    print("Nobo: but i'm going to be your guide and the Vrauqrid showing you around the ropes.")
    print("Nobo: Luckily for you, you are welcome to live with us here in Fauna.")
    print("Nobo: Unfortunately for you, only a few know your acient languge, me being one of those folks.\n")

    print("Nobo: The best way for you to learn about this place is for you to explerance it yourself.")
    print("He leads you out of the room, down the hall way to a large marble door lined with gold and ingraved details.")

    print("He opens the door to reveal a magnicenet ")



if __name__ == "__main__":
    main()
