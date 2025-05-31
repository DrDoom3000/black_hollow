import random
import math
import time
import os

seeds = []
jump = 0
hollowb = 0
def generate_seed():
    seed = str(random.randint(10000000000000000000, 99999999999999999999))
    while True:
        seed = str(random.randint(10000000000000000000, 99999999999999999999))
        if not seed in seeds:
            break
    seeds.append(seed)
    return seed

def split_seed(seed):
    values = []
    values.extend(int(digit) for digit in str(seed))
    return values

def generate_story(values):
    location = ""
    difficulty = 0
    character = ""
    perks = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cube_fields = 0
    boss = ""
    if values[1] < 3:
        location = "Tenebris"
    elif values[1] < 7 and values[1] >= 3:
        location = "Veilthorn"
    elif values[1] >= 7:
        location = "Nyxterra"
    if values[2] < 2:
        character = "Selene"
    elif values[2] < 4 and values[2] >= 2:
        character = "Orin"
    elif values[2] < 6 and values[2] >= 4:
        character = "Malrik"
    elif values[2] < 8 and values[2] >= 6:
        character = "Thyra"
    elif values[2] >= 8:
        character = "Dain"
    if values[5] < 5:
        cube_fields = 8
    else:
        cube_fields = 16
    if values[6] < 3:
        boss = "Dolmora"
    elif values[6] < 6 and values[6] >= 3:
        boss = "Vaermor"
    else:
        boss = "Xal'tharan"
    difficulty = values[0]
    perks[values[3]] = 1
    if values[3] == values[4] and not values[4] == 9:
        values[4] += 1
    elif values[3] == values[4] and values[4] == 9:
        values[4] -= 1
    perks[values[4]] = 1
    return location, character, difficulty, cube_fields, boss, perks

seed = generate_seed()
split = split_seed(seed)
location, character, difficulty, cube_fields, boss, perks = generate_story(split)

def dice(seed, difficulty, cube_fields):
    change_val = random.randint(1, 13) + 6
    result = 0
    try:
        roll_times = seed[change_val]
    except IndexError:
        roll_times = 1 

    max_value = cube_fields - math.floor(0.3 * difficulty)
    if max_value < 1:
        max_value = 1

    for i in range(0, roll_times):
        result = random.randint(1, max_value)
    if result < 1:
        result = 1
    return result


def game(location, character, boss, perks, difficulty):
    jump = 0
    print(f"Welcome, player. Just returning from a small tavern, you are on your way home through the streets of Black Hollow. As you reach your house and just want to open your door, everything fades with a scream of white.")
    input("                                                                                                 Press any key to continue")
    os.system('clear')
    time.sleep(2.5)
    print(f"You wake up again. Everything feels...odd. It was always a bit foggy in Black Hollow, but now, you are struggling to see even two metres. \nAs you stand up, you fnd yourself in a small back alley...You have never been here before. As you are walking towards where you think the exit is, a strange figure appears out of the fog.")
    print("   _____   ")
    print("  /      \\  ")
    print("  | ''''  |  ")
    print("   \\_==__/")
    print("    ' | '")
    print("\nHello, wanderer! It is dangerous in Black Hollow, what are you doing here? \n1 - Talk to the figure\n2 - Ignore it and walk past\n3 - Run away.")
    while True:
        answer = input()
        if answer == "2":
            time.sleep(1.5)
            print("Ending 1: You didn't care about the figure. As you walked past it, you tripped over a rock.\nYou didn't make it.")
            exit()
        elif answer == "1":
            time.sleep(1.5)
            break
        elif answer == "3":
            time.sleep(1.5)
            print("You ran away from the figure. As you turned around, it disappeared. You feel as if you missed something. \nWhen you turn back, you see a box lying in front of you. \n1 - Open it \n2 - Ignore it")
            ans = input()
            if ans == "1":
                time.sleep(1.5)
                print(f"A small dice lies in the box. Strangely, it has {cube_fields} sides and looks as if it was made from bones. Maybe you should go home...")
                jump = 1
                break
            elif ans == "2":
                time.sleep(1.5)
                print("   _____   ")
                print("  /      \\  ")
                print("  | ''''  |  ")
                print("   \\_==__/")
                print("    ' | '")
                time.sleep(1.5)
                print("The figure appears again. 'Why did you run away? I don't want to hurt you' \n")
                input()
                break
    if not jump == 1:
        time.sleep(1)
        print("'What is your name, wanderer?'")
        input()
        time.sleep(1)
        print(f"'My name is {character}'")
        input()
        time.sleep(1)
        print(f"'So, {character}, what are you doing in the endless fog of Black Hollow?'")
        input()
        time.sleep(1)
        print("'In the...endless fog? I just...came hom from the tavern...and then, everything faded. I woke up in that back alley...'")
        input()
        time.sleep(1)
        print("'So...you survived it?'")
        input()
        time.sleep(1)
        print("'Survived what?'")
        input()
        time.sleep(1)
        print("'The fog. You know, not everyone made it...'")
        input()
        time.sleep(1)
        print("'What do you mean, not everyone made it?'")
        input()
        time.sleep(1)
        print("'Well, I had a hotel here. But when the fog came, I became...this'")
        input()
        time.sleep(1)
        print(f"'I have something for you, {character}. Use it carefully.")
        input()
        time.sleep(1)
        print(f"You get handed a strange die with {cube_fields} sides. It reminds you of bones.\nWhen you look up again, the figure disappeared.\nMaybe you should go home.")
    print("1 - Go home\n2 - Go to the tavern")
    while True:
        answer = input()
        if answer == "1":
            time.sleep(1)
            print("You try to remember where your house was...You have never seen this area here. You try to make your way.")
            for i in range(0, 1):
                time.sleep(2)
                print("Wrong way here...")
            time.sleep(2)
            print("You reach your house.But it looks a bit...different. That one window...it's never been there.\nAs you try to open the door, the door handle breaks. The house doesn't have any other entrances, so you decide to go to the tavern.")
            break
        elif answer == "2":
            break
    time.sleep(1)
    print("As you reach the tavern, a strange shimmer from the inside runs a shiver down your spine. Something is off. \n1 - Enter the tavern\n2 - Leave")
    while True:
        answer = input()
        if answer == "2":
            time.sleep(1)
            print("Not everyone needs to be a hero. Ending 2: Someone else could do that.")
            exit()
        elif answer == "1":
            break
    time.sleep(1)
    print("When you enter the tavern, a strange smell hangs in the air. The once so welcoming sign at the counter has all of its words scratched out,\n only portions of light are provided by candles. A skeletal figure sits behind the counter. It awaits you.")
    input()
    time.sleep(1)
    print("'Play, wanderer. The Hollow welcomes you.'")
    input()
    time.sleep(1)
    print(f"In fear, you slowly take a seat at the counter. The dice feels...strange. It moves in your pocket. \nAs you lay it on the table, the Hollow gives you two cards.")
    print("'These are two cards for you, wanderer. They could come in handy.'")
    print("The cards look strangely old, but still some kind of familiar. The cards say:")
    cards = []
    if perks[0] == 1:
        print("Lantern's Glow: Get a new card\n")
        cards.append("Lantern's Glow")
    if perks[1] == 1:
        print("Hollow's blessing: Convert a bad roll into a neutral outcome\n")
        cards.append("Hollow's blessing")
    if perks[2] == 1:
        print("Flesh Dice Set: Get 1.5 times luck\n")
        cards.append("Flesh Dice Set")
    if perks[3] == 1:
        print("Traveler's Deck: Reshuffle your cards\n")
        cards.append("Traveler's Deck")
    if perks[4] == 1:
        print("The Clock Chimes: Skip one Dice Roll\n")
        cards.append("The Clock Chimes")
    if perks[5] == 1:
        print("Shifting Fate: Swap your dice result with your previous one\n")
        cards.append("Shifting Fate")
    if perks[6] == 1:
        print("Severed Thread: Remove a random card from your deck\n")
        cards.append("Severed Thread")
    if perks[7] == 1:
        print("The Hollow's Mercy: The next dice roll can't harm you\n")
        cards.append("Hollow's Mercy")
    if perks[8] == 1:
        print("Wretched Pact: Trade a random card for a guaranteed high dice roll\n")
        cards.append("Wretched Pact")
    if perks[9] == 1:
        print("The Hour strikes: Is your next dice roll high, immediately go forward 1 hour. is it low, go backwards 1 hour.\n")
        cards.append("The Hour strikes")
    input()
    print("'You will get 3 new cards every round, wanderer. If you make it to 12 o'clock, you will be free.'")
    print("'The dice will decide your fate.'")
    input()
    timex = 1
    rcount = 0
    stored_result = 1
    score = 1000
    while not timex == 13:
        val = input()
        if val == "mq17":
            score = 0
        elif val == "go25":
            timex = 13
        njump = 0
        safe = 0
        hstrikes = 0
        result = 0
        hollowb = 1
        high = 0
        if rcount == 2:
            rcount = 0
            timex += 1
        print(f"It is now {timex} o'clock. Your current score is {score}.")
        draw = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        fdraw = random.randint(0, 9)
        sdraw = random.randint(0, 9)
        tdraw = random.randint(0, 9)
        while sdraw == fdraw or sdraw == tdraw or fdraw == tdraw:
            sdraw = random.randint(0, 9)
            tdraw = random.randint(0, 9)
        draw[fdraw] = 1
        draw[sdraw] = 1
        draw[tdraw] = 1
        if draw[0] == 1:
            print("Lantern's Glow: Get a new card\n")
            cards.append("Lantern's Glow")
        if draw[1] == 1:
            print("Hollow's blessing: Convert a bad roll into a neutral outcome\n")
            cards.append("Hollow's blessing")
        if draw[2] == 1:
            print("Flesh Dice Set: Get 1.5 times luck\n")
            cards.append("Flesh Dice Set")
        if draw[3] == 1:
            print("Traveler's Deck: Reshuffle your cards\n")
            cards.append("Traveler's Deck")
        if draw[4] == 1:
            print("The Clock Chimes: Skip one round\n")
            cards.append("The Clock Chimes")
        if draw[5] == 1:
            print("Shifting Fate: Swap your dice result with your previous one\n")
            cards.append("Shifting Fate")
        if draw[6] == 1:
            print("Severed Thread: Remove a random card from your deck\n")
            cards.append("Severed Thread")
        if draw[7] == 1:
            print("The Hollow's Mercy: The next dice roll can't harm you\n")
            cards.append("Hollow's Mercy")
        if draw[8] == 1:
            print("Wretched Pact: Trade a random card for a guaranteed high dice roll\n")
            cards.append("Wretched Pact")
        if draw[9] == 1:
            print("The Hour strikes: Is your next dice roll high, immediately go forward 1 hour. is it low, go backwards 1 hour.\n")
            cards.append("The Hour strikes")
        if draw[0] == 1:
            print("Lantern's Glow: Get a new card\n")
            cards.append("Lantern's Glow")
        fshow = random.randint(0, len(cards)-1)
        sshow = random.randint(0, len(cards)-1)
        while fshow == sshow:
            sshow = random.randint(0, len(cards)-1)
        print(f"First Card:     {cards[fshow]}\nSecond Card:        {cards[sshow]}")
        print("Press 1 or 2 to select a card")
        select = input()
        while True:
            if select == "1":
                selected_card = cards[fshow]
            elif select == "2":
                selected_card = cards[sshow]
            else:
                print("Invalid selection. Choose 1 or 2.")
                select = input()
                continue

            print(f"You selected: {selected_card}")
       
            if selected_card == "Lantern's Glow":
                new_card = random.randint(0, 9)
                newcard2 = ""
                if new_card == 0:
                    cards.append("Lantern's Glow")
                    new_card2 = "Lantern's Glow"
                elif new_card == 1:
                    cards.append("Hollow's blessing")
                    new_card2 = "Hollow's blessing"
                elif new_card == 2:
                    cards.append("Flesh Dice Set")
                    new_card2 = "Flesh Dice Set"
                elif new_card == 3:
                    cards.append("Traveler's Deck")
                    new_card2 = "Traveler's Deck"
                elif new_card == 4:
                    cards.append("The Clock Chimes")
                    new_card2 = "The Clock Chimes"
                elif new_card == 5:
                    cards.append("Shifting Fate")
                    new_card2 = "Shifting Fate"
                elif new_card == 6:
                    cards.append("Severed Thread")
                    new_card2 = "Severed Thread"
                elif new_card == 7:
                    cards.append("Hollow's Mercy")
                    new_card2 = "Hollow's Mercy"
                elif new_card == 8:
                    cards.append("Wretched Pact")
                    new_card2 = "Wretched Pact"
                elif new_card == 9:
                    cards.append("The Hour strikes")
                    new_card2 = "The Hour strikes"
                print(f"You drew: {new_card2}")
                break

            elif selected_card == "Hollow's blessing":
                hollowb = 1
                break
            elif selected_card == "Flesh Dice Set":
                difficulty = difficulty / 1.5
                break
            elif selected_card == "Traveler's Deck":
                break
            elif selected_card == "The Clock Chimes":
                rcount += 1
                njump = 1
                break
            elif selected_card == "Shifting Fate":
                njump = 1
                result = stored_result
                break
            elif selected_card == "Severed Thread":
                if cards:
                    del cards[random.randint(0, len(cards)-1)]
                break
            elif selected_card == "Hollow's Mercy":
                safe = 1
                break
            elif selected_card == "Wretched Pact":
                if cards:
                    del cards[random.randint(0, len(cards)-1)]
                high = 1
                break
            elif selected_card == "The Hour strikes":
                hstrikes = 1
                break

        if not njump == 1:
            time.sleep(1)
            print("'So then, wanderer, roll the dice'")
            time.sleep(0.5)
            print("...")
            input()
            time.sleep(1)
            result = dice(split, difficulty, cube_fields)
            if hollowb == 1 and result < math.floor((cube_fields / 2) - 1) and safe == 1:
                result = cube_fields/2
            elif result < (cube_fields/2)+1 and high == 1:
                result = (cube_fields/2)+1
            print(f"You rolled a {result}")
            input()
            time.sleep(1)
            print("'Your fate has been sealed'")
        stored_result = result
        if result < math.floor((cube_fields/2)):
            score -= 340
            print("'This was not your best luck, wanderer.'")
            print("The fog spreads...")
        elif result >= math.floor((cube_fields/2)) and result <= math.floor((cube_fields/2)+2):
            score -= 100
            print("'Well, wanderer, it looks as if the fog keeps where it is.'")
            print("Nothing happens...")
        elif result > math.floor((cube_fields/2)-2):
            score += 335
            print("'Ouch...That hurts'")
            print("'The fog withdraws...")
        if score < 1:
            print(f"As everyone before, another soul lost in the fog...Maybe {character} will be forgotten...Maybe {character} will return...\nBut who knows if anyone will care about him in the endless fog?")
            print("   _____   ")
            print("  /      \\  ")
            print("  | ''''  |  ")
            print("   \\_==__/")
            print("    ' | '")
            input()
            os.system('clear')
            print("I like cats.")
            msg1 = " (\___/) "
            msg2 = " (=⋅.⋅=)"
            msg3 = ' (")(")_/'
            print(msg1)
            print(msg2)
            print(msg3)
            input()
            exit()
        rcount += 1
    print("'You...made it. You are the first to survive.But who knows...The next one might not be that lucky. When I'm back in 19 years, pray that you are not in town.'")
    input()
    time.sleep(1)
    print("The Hollow disappears with the fog.")
    input()
    time.sleep(1)
    print(f"Your score was {score}.")
    input()
    os.system('clear')
    print("I like cats.")
    msg1 = " (\___/) "
    msg2 = " (=⋅.⋅=)"
    msg3 = ' (")(")_/'
    print(msg1)
    print(msg2)
    print(msg3)
    input()
    exit()

game(location, character, boss, perks, difficulty)
