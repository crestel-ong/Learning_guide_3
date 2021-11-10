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

    print("He opens the door to reveal a magnicenet scene before you.")
    print("A window allows you to peer out to the outside.")
    print("A bueatiful city lies infront of you lit up by algeas and glowing aquatic life.")
    print("You wispher under your breath: Wow, this is so unbeliveable\n. ")
    print("Nobo: Marvelous isn't it?")
    print("Nobo looks at you as your jaw is still dropped.")
    print("You: It's indescribable, I've never seen something so amazing.\n")

    print("You spend the next 6 months learning about the Fauna culture, ettequite and it inhabitents.")
    print("Although the bueaty of the colony you yearn to go back to the surface.")
    print("The Vrauqrids despise my species and most look desguested whenever they see me.")
    print("You don't belong here, you want to go back up.")
    print("You asked Nobo if you can and he says that you need to make a request with thier leader first.")
    print("You have been mentally preparing the past two weeks for this meeting.")
    print("Today is finally the day that you get to meet the king of the Fauna colony.")
    print("Nobo guides you to the throne room. He opens the door and presents us to the king.")
    print("Nobo: Luckliy for you the king too speaks your ancient languge.")
    print("Nobo: Behold your holiness {0} the Human, they have a request of you.".format(name))
    print("Vrauqrid King: {0} what a werid name.".format(name))
    print("Vrauqrid King: Anyways...")
    print("The massive Vrauqrid glances down towards you curious of your request.")
    print("You: I want to return to the surface.")
    print("Vrauqrid King: Intresting... Why? *his voice filled with gravitas*")
    print("You: I just don't belong here. I know that I have been treated politely here, but i can see the hatred towards me under Vrauqrids' fake smiles.")
    print("You: I need to get back to where i belong, the surface.")
    print("Vrauqrid King: To be honest I'm quite pleased with this request.")
    print("Vrauqrid King: You are correct the beings of my domain dislike your presents as a reminder of a sick part of our otherwise sacififul history.")
    print("Vrauqrid King: That being that we are decdants of those wicked humans.")
    print("Vrauqrid King: I am more happy to let you go.",end ='')
    print("But before that you must complete 3 challanges, as tests to say if you are ready to leave.\n")

    print("Vrauqrid King: The three tasks will all be tests of intelect.")
    print("Vrauqrid King: Oh, also once you leave we will never take you back in.")
    print("Vrauqrid King: Even if you beg and plead we will ignore your cries.")
    print("You: I accept those requirements.\n")
    print("Vrauqrid King: Prepare yourself tomorrow it will start.")

    print("CHALLANGE ONE\n")
    print("The next day in some a room of the palace.")
    print("Nobo: As requested by the King, I will be here to lead the challanges.")
    print("Nobo: Any questions?")
    print("You: Ah, actually yes.")
    print("Nobo: Nothing? Good. *He states rudely*")
    print("Nobo: Sorry {0}, its kind of a sarcastic question.")
    print("Nobo: Those atempting these tasks aren't allowed to ask questions.")
    print("You: Okay, I guess?")
    print("Nobo: Let us begin.")
    print("Nobo: The Vrauqrid King, is fair and thought that it would be unjust for you to solve problems in our languge.")
    print("Nobo: You will be given problems from your time even the greatest minds of Vrauqrids' had difficulity solving.\n")
    print("What is 3 x 25 equal?")

    while True:
        challenge1 = input("> ")
        challenge1 = challenge1.upper()
        if challenge1 == "75" or challenge1 == "SEVENTY-FIVE":
            print("Nobo: Very impressive, you passed the first test.\n")
            break
        else:
            print("Nobo: Wrong, don't worry though I'll give you another chance.\n")

    print("Nobo: Congrats {0}, you solved the first task!\n".format(name))
    print("Nobo: I'll give you an hour break and than you start your second challange.")
    print("*1 HOUR LATER*\n")
    print("CHALLANGE TWO\n")
    print("Nobo: I think thats enough time lets start the second round.")
    print("Nobo: This one is similar to the last but even harder.\n")
    print("Nobo: What is 121 ÷ 11 equal to?\n")

    while True:
        challenge2 = input("> ")
        challenge2 = challenge2.upper()
    if challenge2 == "11" or challenge2 == "ELEVEN":
        print("Nobo: WOW! That was fast it took our teams 3 months to crack that code!")
        print("You passed the second test, good job!\n")
        break
    else:
        print("Nobo: I'll let you try again.\n")

    print("Nobo: Nice job! You figured out round two.\n")
    print("Nobo: For this last one I won't give you time to recoperate.\n")
    print("CHALLANGE THREE\n")
    print("Nobo: We start NOW!")
    print("Nobo: Solve this riddle.")
    print("Nobo: Even our all-wise king had a hard time with this one.\n")
    print("Nobo: What has hands but no arms and a face but no eyes?\n")

    while True:
        challenge3 = input("> ")
        challenge3 = challenge3.upper()
    if challenge3 == "CLOCK":
        print("Nobo: I am beyond surprised! That was the hardest one.")
        print("You passed all the tests!")
        break
    else:
        print("Nobo: Take another try.")
        print("*HINT* Tick tock, tick tock.\n")

    print("Well done, my friend!")
    print("Go rest you deserve it, I'll get you tommorw to meet with the king.\n")

    print("*NEXT DAY*")
    print("Nobo: The king is waiting for us.")
    print("You and Nobo wait infront of the door with the gaurds before the king gives you the go ahead.")
    print("Vrauqrid King: ENTER!")
    print("Vrauqrid King: I heard that you passed all the challanges.")
    print("Honestly I'm a little surprised but I digress.")
    print("So I'll let you take one of our ancient ships, you should have everything in there to surface, plus some rations.")
    print("You: Thank you so much! I will never forget your kindness.")
    print("No need for the pleasentures, just remember you can neer return once you leave.\n")
    print("Although")









if __name__ == "__main__":
    main()
