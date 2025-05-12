#easy_stories.py
def easy_story1():
    print("\nYou've selected: Easy Story 1")

    # Collect inputs
    adjective1 = input("Enter an adjective: ")
    food1 = input("Enter a type of food: ")
    food2 = input("Enter another type of food: ")
    noun1 = input("Enter a noun: ")
    liquid = input("Enter a liquid: ")
    plural_noun1 = input("Enter a plural noun: ")
    adjective2 = input("Enter another adjective: ")
    person_name1 = input("Enter a person's name: ")
    animal = input("Enter an animal: ")
    emotion1 = input("Enter an emotion: ")
    noun2 = input("Enter another noun: ")
    color = input("Enter a color: ")

    story = f"""
    I was so {adjective1} today that I forgot to pack my lunch!
    So, I grabbed whatever I could find in the kitchen and made a sandwich with {food1}, {food2}, and a slice of {noun1}.
    Then I added a squirt of {liquid}, a handful of {plural_noun1}, and smushed it all between two pieces of {adjective2} bread.
    When I brought it to school, my friend {person_name1} said it looked like a {animal}.
    I took one bite and immediately felt {emotion1}.
    It made a sound like a {noun2} when I chewed it, and I may have turned slightly {color}.
    I guess next time I’ll just pack a normal lunch!
    """
    print(story)

def easy_story2():
    print("\nYou've selected: Easy Story 2")

    # Collect inputs
    animal1 = input("Enter an animal: ")
    adjective1 = input("Enter an adjective: ")
    verb1_ing = input("Enter a verb ending in -ing: ")
    noun1 = input("Enter a noun: ")
    clothing_item = input("Enter a clothing item: ")
    place1 = input("Enter a place: ")
    device1 = input("Enter a device: ")
    food1 = input("Enter a food: ")
    exclamation1 = input("Enter an exclamation: ")
    nonsense_word1 = input("Enter a nonsense word: ")
    noun2 = input("Enter another noun: ")
    silly_name1 = input("Enter a silly name: ")

    story = f"""
    My pet {animal1} is the most {adjective1} creature I’ve ever met.
    Every morning, it wakes me up by {verb1_ing} on my bed and eating my {noun1} right off my desk.
    It loves to wear my {clothing_item} and parade around the {place1} like royalty.
    Last week, it even tried to use my {device1} to order {food1} online.
    Sometimes it talks in its sleep, muttering words like “{exclamation1}!” and “{nonsense_word1}!”
    I don’t know if it’s a pet or a {noun2}, but I love it anyway.
    I think I’ll name it {silly_name1}... again.
    """
    print(story)

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

def easy_story4():
    print("\nYou've selected: Easy Story 4")

    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")
    career = input("Enter a career: ")
    verb2 = input("Enter another verb: ")
    name = input("Enter a name: ")
    pronoun = input("Enter a pronoun (he/she/they): ")
    place = input("Enter a place: ")
    past_tense_verb = input("Enter a past-tense verb: ")
    noun = input("Enter a noun: ")

    story = f"""
    When I was younger, I experienced a very {adjective} event. I saw my mother {verb}!
    Though this may seem mundane to most, I couldn’t believe my eyes. See, I had never seen anyone {verb}.
    I felt {adjective2}. I decided right then that my life would change forever.
    I decided to pursue {career}. My mom asked me what was wrong, but I just told her I needed to {verb2}.
    I went to my friend {name}’s house, when I told {pronoun} that we needed to go to {place}.
    {pronoun.capitalize()} agreed, and we {past_tense_verb} to the {place}.
    Why did we go there, do you ask? Well, the answer is obvious. We needed to find {noun}. Duh!
    """
    print(story)

def easy_story5():
    print("\nYou've selected: Easy Story 5")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    plural_noun = input("Enter a plural noun: ")
    name = input("Enter a name: ")
    adjective2 = input("Enter another adjective: ")
    pronoun = input("Enter a pronoun (he/she/they): ")
    plural_noun2 = input("Enter another plural noun: ")
    plural_noun3 = input("Enter a third plural noun: ")
    name2 = input("Enter a second name: ")
    adjective3 = input("Enter a third adjective: ")

    story = f"""
    Once upon a time, a(n) {adjective} {noun} ruled the kingdom of {plural_noun}.
    {noun.capitalize()} was given a special name, {name}. {name} was a(n) {adjective2} ruler.
    {pronoun.capitalize()} quickly became ruthless, executing anyone who threatened {pronoun} rule.
    After many years, the kingdom of {plural_noun} became fed up with {name}’s cruelty, and decided to overthrow their ruler.
    The kingdom went into war, with the {plural_noun2} fighting the {plural_noun3}.
    In the end, {plural_noun2} was victorious, with the new ruler being a(n) {adjective2} person.
    This ruler was given the title of {name2}, the {adjective3}.
    The kingdom remained prosperous for years to come!
    """
    print(story)

