def medium_story2():
    print("\nYou've selected: Medium Story 2")

    school_name1 = input("Enter a school name: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    plural_noun1 = input("Enter a plural noun: ")
    electronic_device1 = input("Enter an electronic device: ")
    person_name1 = input("Enter a person's name: ")
    color1 = input("Enter a color: ")
    food1 = input("Enter a type of food: ")
    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    drink1 = input("Enter a type of drink: ")
    verb3_past = input("Enter a past-tense verb: ")
    teacher_name1 = input("Enter a teacher's name: ")
    verb4_past = input("Enter another past-tense verb: ")
    adjective2 = input("Enter a second adjective: ")
    animal1 = input("Enter an animal: ")
    substance1 = input("Enter a substance: ")
    noun2 = input("Enter another noun: ")
    dessert1 = input("Enter a dessert: ")
    vehicle1 = input("Enter a type of vehicle: ")

    story = f"""
    This year’s science fair at {school_name1} was the weirdest one yet.
    I built a robot that could {verb1} and {verb2} using just {plural_noun1} and an old {electronic_device1} I found in my garage.
    My best friend {person_name1} made slime that turned {color1} and made fart noises when stretched.
    Another student used {food1} to create a functioning {noun1}, which exploded halfway through judging.
    The judges looked {adjective1}, and one of them nearly spilled their {drink1} in shock.

    When my turn came, I got so nervous I {verb3_past} and dropped my robot on {teacher_name1}’s shoes.
    Everyone gasped, but then she {verb4_past} and said it was the most {adjective2} thing she’d ever seen.
    To top it off, a group of students did a live demo with {animal1}s and a makeshift volcano powered by {substance1}.
    I ended up winning third place and a trophy shaped like a {noun2}.
    We all celebrated with {dessert1}, and I promised myself I’d go even bigger next year — maybe with lasers and a flying {vehicle1}.
    """
    print(story)