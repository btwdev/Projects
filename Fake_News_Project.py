import random
Subject = [
    "Sharuk Khan",
    "Amitabh Bachchan",
    "Salman Khan",
    "Akshay Kumar",
    "Ranveer Singh",
    "Deepika Padukone",
    "narendra Modi",
    "Rahul Gandhi",
    "Sonia Gandhi"
]

Action = [
    "caught in a scandal",
    "wins an award",
    "involved in a controversy",
    "launches a new initiative",
    "makes a surprising announcement",
    "faces legal issues",
    "joins a new political party",
    "reiding on a tiger",
    "adopts a child",
    "Decleres war on "

]

Object_place = [
    "in Mumbai",
    "at a political rally",
    "during a film shoot",
    "at an award ceremony",
    "while vacationing abroad",
    "at a charity event",
    "during a press conference",
    "in a secret meeting",
    "while attending a wedding",
    "at a sports event"
]
def generate_headline():    
    return random.choice(Subject) + " " + random.choice(Action) + " " + random.choice(Object_place)
print(generate_headline())

while True:
    
    
    user_input = input("\nYou want to another headline (Yes/No):").strip().lower()

    if user_input == "yes":
        print(f"Breaking News: {generate_headline()}")
        continue
    elif user_input == "no":
        print("Thanks For Using My Program")
        break
    else:
        print("Please enter 'Yes' or 'No' Only")
        
    