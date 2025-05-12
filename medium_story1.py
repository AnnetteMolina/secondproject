def medium_story1():
    print("\nYou've selected: Medium Story 1")

    place1 = input("Enter a place: ")
    smell1 = input("Enter a smell: ")
    plural_noun1 = input("Enter a plural noun: ")
    food1 = input("Enter a type of food: ")
    noun1 = input("Enter a noun: ")
    plural_noun2 = input("Enter another plural noun: ")
    exclamation1 = input("Enter an exclamation: ")
    adjective1 = input("Enter an adjective: ")
    plural_noun3 = input("Enter a third plural noun: ")
    adjective2 = input("Enter a second adjective: ")
    person_name1 = input("Enter a person's name: ")
    animal1 = input("Enter an animal: ")
    sound1 = input("Enter a sound: ")
    structure1 = input("Enter a structure (e.g. cabin, tent): ")
    liquid1 = input("Enter a type of liquid: ")
    clothing_item = input("Enter a clothing item: ")
    adjective3 = input("Enter a third adjective: ")
    insect1 = input("Enter an insect: ")

    story = f"""
    I was excited for camp at {place1}, but everything went wrong the second we arrived. My tent was full of holes and smelled like {smell1}.
    During the first night, I found {plural_noun1} crawling all over my sleeping bag, and a raccoon stole my {food1}.
    On the hike the next morning, I tripped on a {noun1}, fell into a bush of {plural_noun2}, and had to wear a leaf as a bandage.
    "{exclamation1}!" I yelled, sliding down a muddy hill straight into the lake. Everyone laughed, but at least the water washed off the {adjective1} goo from my legs.

    Later that evening, we roasted {plural_noun3} over the campfire and told scary stories.
    One was about a {adjective2} ghost named {person_name1} who haunted abandoned cabins and screamed like a {animal1}.
    Just as the story ended, we heard a {sound1} in the woods. Everyone panicked and ran into the {structure1} at once, knocking over a pot of {liquid1}.
    I accidentally put on someone else's {clothing_item} and wore it backwards all night.
    Camp was definitely {adjective3}, but I made new friends — and a lasting fear of {insect1}.
    """
    print(story)