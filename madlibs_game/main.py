#main.py
import random
from easy_stories import easy_story1, easy_story2, easy_story3, easy_story4, easy_story5
from medium_stories import medium_story1, medium_story2, medium_story3, medium_story4, medium_story5
from hard_stories import hard_story1, hard_story2, hard_story3, hard_story4, hard_story5

def main():
    print("Welcome to Mad Libs!")
    print("Choose a difficulty: easy, medium, or hard")

    difficulty= input("Enter your choice:"). strip().lower()
    if difficulty == "easy":
        stories = [easy_story1, easy_story2, easy_story3, easy_story4, easy_story5]
    elif difficulty == "medium":
        stories = [medium_story1, medium_story2, medium_story3, medium_story4, medium_story5]
    elif difficulty == "hard":
        stories = [hard_story1, hard_story2, hard_story3, hard_story4, hard_story5]
    else:
        print("Invalid choice. Please choose easy, medium, or hard.")
        return
    print (f"\nYou chose {difficulty}.")
    story_func = random.choice(stories)
    story_func()
if __name__ == "__main__":
    main()