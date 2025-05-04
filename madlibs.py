def play_madlib():
    print("Welcome to the Mad Libs game!")
    print("Please provide the following words:")

    # collecting user inputs

    adjective = input("Enter an adjective:")
    noun = input("Enter a noun:")
    verb = input("Enter a verb:")
    place = input("Enter a place:")

    # test story for input

    story = f"Once upon a time in a {adjective} land, there lived a {noun}. Every day, the {noun} would {verb} in the {place}."

    print("/nHere's your story:")
    print(story)
    print("Thank you for playing Mad Libs!")
if __name__ == "__main__":
    play_madlib()