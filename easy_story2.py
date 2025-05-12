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