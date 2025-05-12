
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