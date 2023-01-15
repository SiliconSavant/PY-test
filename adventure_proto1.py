
print("Welcome to the adventure game!")
print("You are lost in a forest, and you must find your way out.")

direction = ""
while direction != "exit":
    direction = input("Which direction would you like to go? (north, south, east, west, exit): ")

    if direction == "north":
        print("You come across a river. You can either try to swim across or follow the river.")
    elif direction == "south":
        print("You find a cave. You can either go inside or stay outside.")
    elif direction == "east":
        print("You stumble upon a clearing. You see a small cabin. You can either knock on the door or ignore it.")
    elif direction == "west":
        print("You find a dense thicket. You can either try to push through or go back.")
    elif direction == "exit":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please enter north, south, east, west, or exit.")
