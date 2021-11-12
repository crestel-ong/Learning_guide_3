#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Nov 2021
# this is a text-based game for learning guide 3
# its name is Finding My Way Home!

import time


def main():
    print("Welcome to Finding My Way Home!")
    print("This is a text-based game.")
    print("If you have some trouble during the story, ", end="")
    print("some hints might be dropped to help you!\n")
    print("You groggily open your eyes, ", end="")
    print("they strain against the odd-looking lights above.")
    print("A revolting, indistinguishable, foul stench fills your ", end="")
    print("lungs as you take a deep breath.")
    print("Unfamiliar noises blare in your ears as you struggle.")
    print("Looking around, you see your hands and feet are ", end="")
    print("bound to the table you lay upon.\n")

    while True:
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
    print("Tears stream down your face.")
    print("Your heart starts to beat erratically as ", end="")
    print("the ugly monster peers its beady eyes into yours.\n")
    time.sleep(20)
    print("Fish-man: Hey could you please calm down, you are freaking me out.")
    time.sleep(3)
    print("Fish-man: I'm going to explain everything just stop panicking.")
    time.sleep(3)
    print("Fish-man: Do you understand? Nod yes or no.\n")

    while True:
        action2 = input("> ")
        action2 = action2.upper()
        if action2 == "YES":
            print("You settle down and nod your head yes.\n")
            print("Fish-man: Okay, good let me begin then.\n")
            break
        elif action2 == "NO":
            print("Fish-man: You need to calm down before ", end="")
            print("I start explaining, understand now?\n")
        else:
            print("You shrug your shoulders confused.")
            print("Fish-man: I don't understand that response.")
            print("*HINT* enter yes or no.\n")

    print("Fish-man: Firstly, my name is Nobo.")
    time.sleep(3)
    print("Nobo: You are currently in the Fauna Colony, ", end="")
    print("home of many Vrauqrids like myself.")
    time.sleep(3)
    print("Nobo: Around 800 years ago a toxic super nerve agent ", end="")
    print("was globally released.")
    time.sleep(3)
    print("Nobo: Humans were dying by the tens of millions daily.")
    time.sleep(3)
    print(
        "Nobo: Some fled to bunkers, some to space ships, and others to the tiny underwater colonies."
    )
    time.sleep(5)
    print("Nobo: The rest died.")
    time.sleep(3)
    print("Nobo: We barely managed to survive in these colonies, ", end="")
    print("eventually we started to evolve and mutate into what we are now, Vrauqrids.")
    time.sleep(3)
    print("Nobo: Part human, part aquatic animal.\n")
    print("The vrauqrid rests its webbed fingered hand on its face.")
    print("He pauses for a second and contemplates what to say next.\n")
    time.sleep(10)
    print("Nobo: When it comes to you, we found you inside a cryo chamber. ")
    print("Nobo: Some ancient technology was salvaged and we were able ", end="")
    print("to uncover some things.")
    time.sleep(5)
    print("Nobo: It seems that you were some sort of researcher or scientist. ")
    time.sleep(4)
    print("Nobo: You with a small group of others were researching the ocean bottom.")
    time.sleep(4)
    print("Nobo: Some sort of creature attacked your submarine ", end="")
    print("and you got into the cryo chamber as a last resort we figure.")
    time.sleep(4)
    print("Nobo: You have been asleep for around 1789 years.")
    time.sleep(4)
    print("Nobo: You are probably the last living human left on Earth.")
    time.sleep(4)
    print("Nobo: You have been in a coma in our infirmary, for a month now.")
    time.sleep(4)
    print(
        "Nobo: We have underwater tsunamis so it's just expected to restrain patients like this."
    )
    time.sleep(4)
    print(
        "Nobo: Also I know its unorthodox but the doctor wasn't here and you kept on screaming so I bonked your head."
    )
    time.sleep(4)
    print("Nobo: I was worried you would start screaming again, so I taped your mouth.")
    print("Nobo: You aren't the only patient here you know.")
    time.sleep(4)
    print(
        "Nobo: And I'm forbidden to administer any medicine, so tape was the only way.\n"
    )
    time.sleep(4)
    print("He pauses and takes a moment to think.")
    print("Nobo: I can imagine it was super scary waking up here though.")
    time.sleep(4)
    print(
        "He looks at you empathetically, or at least that's what you assume is empathy.\n"
    )
    time.sleep(3)
    print(
        "Nobo: I'm going to remove the tape and restraints now so you can answer my questions."
    )
    time.sleep(4)
    print("Nobo unties your hands and feet and takes off the tape.")
    time.sleep(4)
    print("Nobo: Can you remember anything from before waking up here?")
    time.sleep(4)
    print("Me: I'm starting to remember a few things here and there.")
    time.sleep(4)
    print("Nobo: Well that's good!\n")
    time.sleep(4)
    print("Nobo: Oh, also do you remember your name?\n")

    while True:
        action3 = input(">  ")
        action3 = action3.upper()
        if action3 == "YES":
            print("Nobo: Nice!")
            print(
                "A goofy smile is plastered on its face, displaying its sharpened yellow teeth.\n"
            )
            break
        elif action3 == "NO":
            print("Nobo: You can choose a new name.\n")
            break
        else:
            print("Nobo: It's a simple yes or no answer.")
            print("Nobo: So, yes or no?\n")

    print("Nobo: So what's your name?")
    name = input(">  ")

    print("\nNobo: Good to officially meet you {0}.".format(name))
    time.sleep(4)
    print(
        "Nobo: Luckily for you, the gracious King Atreyu, welcomes you to live with us here in Fauna."
    )
    time.sleep(4)
    print("Nobo: Not that you have any other place to go. *says under his breath*")
    time.sleep(4)
    print("Nobo: Unfortunately for you only a few know your ancient language.")
    time.sleep(4)
    print("Nobo: Me being one of them, for that reason I'll be your guide.")
    time.sleep(4)
    print(
        "Nobo: Once you're done with me you should know everything there is to know about this colony."
    )
    time.sleep(4)
    print("Nobo: First let me show you around.\n")
    time.sleep(2)
    print("Nobo leads you out of the room, down the hall to a large marble door.")
    print("The door is beautifully adorned with gold and engraved details.")
    print("These engravings build a complex yet elegant patterned design.")
    print("Nobo opens the doors to reveal the outside.")
    print("The room is made of a clear material that exposes the nature of Fauna.\n")
    time.sleep(26)
    print("Me: Wow it's an underwater city. *you say in astonishment*\n")
    print("You can see an otherworldly civilization in front of you.")
    print(
        "Buildings are formed in unique shapes tall and small wide and thin, curved and straight."
    )
    print("Gorgeous algae and some magical technology that lights up the colony.")
    print("Aquatic life swims all around.")
    print(
        "Seaweed grows tall and the coral incases much of the ground and underwater mountains."
    )
    print(
        "It's bursting with life. So many vrauqrids or all ages enjoying their lives, a paradise."
    )
    print("You can see that they can breathe underwater.")
    print("You can spot some in glass-like domes enjoying the pleasantries of life.")
    print("Some vrauqrids use dolphins as pets and modes of transportation.")
    print("It looks like your home, the surface.")
    print("It's similar but also so different.\n")
    time.sleep(60)

    print("SIX MONTHS LATER\n")
    print(
        "You have spent the last six months learning the customs, culture, history, creatures, religion, of the vrauqrids."
    )
    print(
        "You know the ins and outs of this colony, what drives their survival, the state of their society etc."
    )
    print(
        "Although much different the vrauqrids are better than humans were in your day, in many aspects."
    )
    print("You discovered that this was a utopia.")
    print(
        "You mostly stayed inside the waterless buildings but whenever you went outside used a special suit."
    )
    print("The suit gives you mobility and you can stay in it for a couple of hours.")
    print(
        "You tried to get along with other vrauqrids, but Nobo was the only one to accept you."
    )
    print("Maybe it was the language gap or maybe it was something deeper.\n")
    time.sleep(45)

    print("ONE RANDOM DAY\n")
    print(
        "Me: Hey Nobo I was wondering, is it possible if I could go back to the surface?"
    )
    time.sleep(4)
    print(
        "Nobo: Before you say more {0}, you need to request this of the king.".format(
            name
        )
    )
    time.sleep(4)
    print(
        "Nobo: Asking me is pointless, he is the overseer of our people he will decide your fate."
    )
    time.sleep(4)
    print("Nobo: Making such a request is a grave insult to us.")
    time.sleep(4)
    print("Nobo: We have welcomed you into our home and you insult our kindness.")
    time.sleep(4)
    print(
        "Me: I'm so sorry I didn't know that was disrespectful. I didn't mean to offend you."
    )
    time.sleep(4)
    print("Nobo: Well you have and it's too late to take it back.")
    time.sleep(4)
    print(
        "Nobo: I will inform the king of your request and I'll get you when he wishes to speak to you.\n"
    )
    time.sleep(4)
    print("Nobo stomps off angrily.")
    time.sleep(5)

    print("\nONE WEEK LATER\n")
    print("Nobo has brought you to make your request in person to the king.\n")
    time.sleep(4)
    print("Nobo: Fortunately for you, he speaks your ancient tongue. *he whispers*")
    time.sleep(4)
    print("King Atreyu: ENTER! *he roughly commands*")
    time.sleep(4)
    print("Nobo: Your highness King Atreyu this is {0} the Human.".format(name))
    time.sleep(4)
    print("King Atreyu: {0}, what an odd name. *he states bluntly*".format(name))
    time.sleep(4)
    print("King Atreyu: Well human, what is your request of me?")
    time.sleep(4)
    print("Me: I want to return to the surface. *you say with confidence*")
    time.sleep(4)
    print("King Atreyu: Interesting... Why? *his voice filled with gravitas*")
    time.sleep(4)
    print("Me: I just don't belong here.")
    time.sleep(4)
    print(
        "Me: I have been treated politely here, but I can see the dislike towards me under Vrauqrids' fake smiles."
    )
    time.sleep(4)
    print("King Atreyu: More like hatred but yes I understand.")
    time.sleep(4)
    print("King Atreyu: Honestly I'm satisfied with the request.")
    time.sleep(4)
    print("King Atreyu: You are correct the beings of my domain dislike your presents.")
    time.sleep(4)
    print(
        "King Atreyu: You're a reminder of the wicked humans that lead to the suffering of our ancestors."
    )
    time.sleep(4)
    print("King Atreyu: Humans are the only flaw on our otherwise divine history.")
    time.sleep(4)
    print("King Atreyu: But you do understand we have no idea what's up there, right?")
    time.sleep(4)
    print("Me: I'm aware I just know that the surface is where I truly belong.")
    time.sleep(4)
    print("King Atreyu: I agree with you.")
    time.sleep(4)
    print("King Atreyu: Before I let you go you must complete three challenges.")
    time.sleep(4)
    print("King Atreyu: Oh, also once you leave we will never take you back in.")
    time.sleep(4)
    print("King Atreyu: Even if you beg and plead we will ignore your cries.")
    time.sleep(4)
    print("Me: I accept those requirements.\n")
    time.sleep(4)
    print("King Atreyu: Prepare yourself, tomorrow it will start.\n")
    time.sleep(4)

    print("THE NEXT DAY\n")
    time.sleep(4)
    print("CHALLANGE ONE\n")
    time.sleep(4)
    print("Nobo: As requested by King Atreyu, I will lead the challanges.")
    time.sleep(4)
    print("Nobo: Any questions?")
    time.sleep(2)
    print("Me: Ah, actually yes.")
    time.sleep(4)
    print("Nobo: Nothing? Good. *He states rudely*")
    time.sleep(4)
    print("Nobo: Sorry {0}, its kind of a sarcastic question.".format(name))
    time.sleep(4)
    print("Nobo: Those attempting these tasks aren't allowed to ask questions.")
    time.sleep(4)
    print("You: Okay, I guess?")
    time.sleep(4)
    print("Nobo: Let us begin.")
    time.sleep(4)
    print(
        "Nobo: The King, is fair and thought that it would be unjust for you to solve problems in our language."
    )
    time.sleep(4)
    print("Nobo: You'll be given problems from your time from your languge.")
    time.sleep(4)
    print(
        "Nobo: Even greatest minds of Fauna had difficulty solving these questions.\n"
    )
    time.sleep(4)
    print("Nobo: The question is - What does 3 x 25 equal?")

    while True:
        challenge1 = input("> ")
        challenge1 = challenge1.upper()
        if challenge1 == "75" or challenge1 == "SEVENTY-FIVE":
            print("Nobo: Very impressive, you passed the first test.\n")
            break
        else:
            print("Nobo: Wrong, don't worry though I'll give you another chance.\n")

    print("Nobo: Congrats {0}, you solved the first task!\n".format(name))
    print("Nobo: I'll give you a break and than you start your second challenge.")

    print("ONE HOUR LATER\n")
    print("CHALLANGE TWO\n")
    print("You get a quick nap to refresh your mind and body.")
    print("Nobo wakes you up.")
    print("Nobo: I think that's more then enough time, let's start the second round.")
    print("Nobo: This one is similar to the last but even harder.\n")
    print("Nobo: What is 121 ÷ 11 equal to?\n")

    while True:
        challenge2 = input("> ")
        challenge2 = challenge2.upper()
        if challenge2 == "11" or challenge2 == "ELEVEN":
            print(
                "Nobo: WOW! That was fast it took our teams 3 months to crack that code!"
            )
            print("Nobo: You passed the second test, good job!\n")
            break
        else:
            print("Nobo: I'll let you try again.\n")

    print("Nobo: Nice job! You figured out round two.\n")
    print("Nobo: For this last one I won't give you time to recoperate.\n")
    time.sleep(4)
    print("CHALLENGE THREE\n")
    print("Nobo: We start NOW!")
    time.sleep(4)
    print("Nobo: Solve this riddle.")
    time.sleep(4)
    print("Nobo: Even our all-wise king had a hard time with this one.\n")
    time.sleep(4)
    print("Nobo: What has hands but no arms and a face but no eyes?\n")

    while True:
        challenge3 = input("> ")
        challenge3 = challenge3.upper()
        if challenge3 == "CLOCK":
            print("Nobo: I am beyond surprised! That was the hardest one.")
            print("Nobo: You passed all the tests!\n")
            break
        else:
            print("Nobo: Take another try.")
            print("*HINT* Tick tock, tick tock.\n")

    print("Well done, my friend!")
    time.sleep(4)
    print("Go rest you deserve it, I'll get you tomorrow to meet with the king.\n")

    print("*NEXT DAY*\n")
    print("Nobo: The king is waiting for us.")
    time.sleep(4)
    print(
        "You and Nobo wait in front of the door with the guards before the king gives you the go-ahead."
    )
    time.sleep(4)
    print("King Atreyu: ENTER!")
    time.sleep(4)
    print("King Atreyu: I heard that you passed all the challenges.")
    time.sleep(4)
    print("King Atreyu: Honestly I'm a little surprised but I digress.")
    time.sleep(4)
    print(
        "King Atreyu: Also I don't know if it was clear or not but if you didn't pass those tests of intellect..."
    )
    time.sleep(4)
    print("King Atreyu: You would never survive the ocean by yourself.")
    time.sleep(4)
    print("King Atreyu: Anyways, I'll let you take one of our ships.")
    time.sleep(4)
    print(
        "King Atreyu: You should have everything to get to the surface and some extra rations."
    )
    time.sleep(4)
    print("You: Thank you so much! I will never forget your kindness.")
    time.sleep(4)
    print(
        "King Atreyu: No need for the pleasantries, just remember you can never return once you leave.\n"
    )
    time.sleep(3)
    print("But you were fine, it was just a small error.\n")
    print("*COUPLE HOURS LATER*")
    print("You reach the surface and see a beautiful beach.")
    print("The plant life is exotic and unfamiliar.")
    print("You hear the song of birds in the air, fresh oxygen fills your lungs.")
    print("I'm finally here what should I do?\n")
    time.sleep(70)

    while True:
        end = input("> ")
        end = end.upper()
        if end == "" or end == "SLEEP" or end == "REST" or end == "NAP":
            #find ppl
            print("You are incredibly tired after that journey and you fall asleep.")
            print("You wake up to figures in strange masks poking you with a stick.")
            print("You move and they all jump up in fear.")
            print("They take ropes and secure you to a tree.")
            print("One of them takes off their mask and under it is a middle-aged woman.")
            print("Stranger 1: OH MY GOD! Are you a human!?")
            print("Me: uh, yes.")
            print("We haven't seen a human outside our tribe in centuries.")
            print("They are incredible joyful of your presence, and celebrate you.")
            print("You get assimilated into their culture and become a part of the clan. You found your way home.\n")
            time.sleep(50)
            break
        elif end == "FOOD" or end == "EAT" or end == "HUNGRY":
            print("After a couple of days on this island you run out of food.")
            print("You are forced to eat some suspicious-looking berries.")
            print("Unfortunately, for you those berries were poisonous.")
            print("You pass away looking at the beautiful scenery around you, the trees, animals, and waterfalls.")
            print("At least you died feeling like you returned home.\n")
            break
        elif end == "CLIMB" or end == "SCAVANGE":
            # find others and live with other humans
            print("You get up from a high hilltop and look down at the surrounding area.")
            print("You see a village and you jump with joy.")
            print("They welcome you into their tribe and you find a new home with them.")
            break
        elif end == "SING" or end == "YELL" or end == "SCREAM" or end == "SHOUT":
            # find other people
            print("You act very loudly.")
            print("You find some local tribesmen and they find the loud noises a battle cry.")
            print("They attack you.")
            print("You plead with them to stop but they don't speak your language.")
            print("Me: Guess life only allows you to escape death a couple of times! *you chuckle in agony* ")
            print("You die afraid but at least glad you were able to see the surface one last time, your home.")
            break
        else:
            print("That verb is unrecognized, try something else.")

    print("THE END.")


if __name__ == "__main__":
    main()
