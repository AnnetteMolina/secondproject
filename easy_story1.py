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
