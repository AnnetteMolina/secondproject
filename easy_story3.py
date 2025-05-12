def easy_story3():
    print("\nYou've selected: Easy Story 3")

    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    place = input("Enter a place: ")
    adjective3 = input("Enter a third adjective: ")
    verb = input("Enter a verb: ")
    past_tense_verb = input("Enter a past-tense verb: ")
    adverb = input("Enter an adverb: ")
    food = input("Enter a type of food: ")
    adjective4 = input("Enter a fourth adjective: ")
    adjective5 = input("Enter a fifth adjective: ")
    verb2 = input("Enter another verb: ")
    adverb2 = input("Enter a second adverb: ")

    story = f"""
    In the morning, it was {adjective} outside. The {adjective2} car took off and drove down the road.
    I decided I wanted to go to the {place}. While I was there, it got too {adjective3}.
    I was immediately frightened, so I started to {verb}. I {past_tense_verb} out of there {adverb}.
    I ran all of the way home. Since I was running so much, I got hungry.
    I decided that I wanted to eat {food}. When I took my first bite, I decided it was too {adjective4}.
    I immediately felt {adjective5}, so I decided to {verb2}. My day went {adverb2}!
    """
    print(story)