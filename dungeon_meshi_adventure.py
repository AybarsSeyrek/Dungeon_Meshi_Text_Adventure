# Dungeon Meshi Text-Based Adventure
# A simple choice game where the player explores a dungeon.

print("Welcome to Dungeon Meshi Adventure!")
print("You are exploring a dangerous dungeon with your party.")
print("Your goal is to survive, find food, and go deeper into the dungeon.\n")

name = input("Enter your character name: ")

print(f"\nHello, {name}!")
print("You enter the first floor of the dungeon.")
print("You see two paths ahead.")

choice1 = input("Do you go LEFT toward the cave or RIGHT toward the kitchen ruins? (left/right): ").lower()

if choice1 == "left":
    print("\nYou walk into a dark cave.")
    print("A giant slime appears!")

    choice2 = input("Do you FIGHT the slime or RUN away? (fight/run): ").lower()

    if choice2 == "fight":
        print("\nYou defeat the slime!")
        print("Senshi cooks it into slime jelly.")
        print("Your party eats and restores energy.")
        print("You win this encounter!")
    elif choice2 == "run":
        print("\nYou run away safely, but your party becomes hungry.")
        print("Marcille complains the whole time.")
    else:
        print("\nInvalid choice. While you were confused, the slime escaped.")

elif choice1 == "right":
    print("\nYou enter the kitchen ruins.")
    print("You find old cooking tools and a suspicious mushroom.")

    choice2 = input("Do you EAT the mushroom or SAVE it for later? (eat/save): ").lower()

    if choice2 == "eat":
        print("\nThe mushroom was magical!")
        print("You feel stronger, but Marcille says this was a terrible idea.")
        print("You continue deeper into the dungeon.")
    elif choice2 == "save":
        print("\nYou save the mushroom.")
        print("Later, Senshi uses it to make dungeon stew.")
        print("The party is happy and full.")
    else:
        print("\nInvalid choice. You accidentally drop the mushroom.")

else:
    print("\nInvalid choice. You stand still until a monster finds you.")

print("\nAdventure complete!")
