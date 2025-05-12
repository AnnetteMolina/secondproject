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