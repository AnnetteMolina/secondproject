def medium_story5():
    name = input("Enter a name: ")
    city_name = input("Enter a city name: ")
    name2 = input("Enter another name: ")
    animal = input("Enter an animal: ")
    time = input("Enter a time: ")
    food = input("Enter a food: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    animal2 = input("Enter another animal: ")
    verb2 = input("Enter another verb: ")

    story = f"""
It all started when my friend, {name} suggested we go to {city_name}. Thinking it could be fun, I agreed. Big mistake! 
On the plane, we met a funny looking guy, who introduced himself by the name of {name2}. He sat in between us, and he smelled like a(n) {animal}. 
When we finally landed, we scurried off to our hotel. The lady at the front desk told us that she could not find our reservation. 
Though she could get us a room, we would have to wait until {time}. Sighing, we left our luggage and decided to go visit a museum.

At the museum, we were surprised to find that almost nobody was around. Getting some {food} at the cafe, we sat down and decided to eat. 
After finishing, my friend decided to {verb} up the stairs, and I followed. Looking around at a room full of delicate material, I became {adjective}. 
My friend was such a clumsy guy, and I was too {adjective2} to behave normally.

Looking at a nearby painting, I was shocked to see a depiction of a person with the head of a(n) {animal2}. 
I was making a joke to my friend, when, all of a sudden, the painting started to speak! The creature swore revenge on us for making fun of it. 
We decided we were just seeing things because we were tired. However, on the street next to the hotel, we ran into a person dressed like the creature from the painting! 
Looking at each other, we decided to {verb2} in the opposite direction. Seeking refuge in a nearby store, we were greeted with a rack of postcards. 
I looked through them, some depicting the nearby city of {city_name}. To my surprise, I found a postcard with another depiction of the creature! 
Long story short, I have been seeing this creature everywhere ever since. A piece of advice: never make fun of art, ever.
"""
    print(story)