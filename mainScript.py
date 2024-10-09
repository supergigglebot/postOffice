# Room Dictionary
rooms = {
    "Your Office": {"North": "Cookie Mobster", "South": "Penny's Pens", "East": "Secretary's Office",
                    "West": "Cassette's Tapes"},
    "Cookie Mobster": {"East": "Post Office", "South": "Your Office"},
    "Penny's Pens": {"North": "Your Office", "East": "Storage Unit"},
    "Storage Unit": {"West": "Penny's Pens"},
    "Secretary's Office": {"North": "First Second Third Bank", "West": "Your Office"},
    "First Second Third Bank": {"South": "Secretary's Office"},
    "Cassette's Tapes": {"East": "Your Office"},
    "Post Office": {"West": "Cookie Mobster"}
}

# Items in rooms, except the starting room and Post Office
items_in_rooms = {
    "Cookie Mobster": "Cookies",
    "Cassette's Tapes": "Tape",
    "Penny's Pens": "Pen",
    "Storage Unit": "Rubber Duckies",
    "First Second Third Bank": "Money",
    "Secretary's Office": "Address Book"
}


# Function to run the game and its internal logic
def start_game():
    current_room = "Your Office"  # Starting room
    inventory = []  # Player's collected items

    print("Welcome to the Game!")
    print("Collect all 6 items and reach The Post Office to win.")
    print("You can move between rooms by typing 'Go North', 'Go South', 'Go East', and 'Go West'.")
    print("Type 'Exit' in The Post Office with all 6 items to win!")
    print("But beware, if you enter unprepared, surely you will meet a terrible fate.")

    # Gameplay loop
    while True:
        print(f"\nYou are in the {current_room}.")

        # Display the surrounding rooms and possible directions
        print("From here, you can move in the following directions:")
        for direction, room in rooms[current_room].items():
            print(f"  {direction}: {room}")

        # Check if there's an item in the current room and collect it if not already done
        if current_room in items_in_rooms and items_in_rooms[current_room] not in inventory:
            item = items_in_rooms[current_room]
            print(f"You found a {item}!")
            collect = input("Would you like to collect it? (yes/no): ").strip().lower()
            if collect == "yes":
                inventory.append(item)
                print(f"{item} has been added to your inventory.")

        # Display inventory
        print(f"Inventory: {inventory}")

        # Get player input
        command = input("Enter your move: ").strip().lower()

        if command == "exit":
            # Check if the player is in the Dragon Room and has all 6 items
            if current_room == 'Post Office':
                if len(inventory) == 6:
                    print("You have all the items and successfully defeated Dragana! You win!")
                    break
                else:
                    print("You don't have all 6 items. Dragana has defeated you! You lose.")
                    break
            else:
                print("You can only use 'exit' in The Post Office.")
                continue

        # Parse the move command
        command_parts = command.split()
        if len(command_parts) == 2 and command_parts[0] == "go":
            direction = command_parts[1].capitalize()

            # Check if the direction is valid in the current room
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print(f"Invalid move! You can't go {direction} from the {current_room}.")
        else:
            print("Invalid command! Please use 'Go North', 'Go South', 'Go East', 'Go West', or 'Exit'.")

        # End the game if the player is in the 'exit' room (Dragon Room with or without all items)
        if current_room == 'exit':
            print("You have reached the exit room. You Win!")
            break

start_game()