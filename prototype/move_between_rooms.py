"""Module Six Milestone starter file for the simplified movement prototype."""

# A dictionary for the simplified dragon text game.
# The dictionary links a room to other rooms.
rooms = {
    "Great Hall": {"south": "Bedroom"},
    "Bedroom": {"north": "Great Hall", "east": "Cellar"},
    "Cellar": {"west": "Bedroom"},
}


# TODO: Set the player's starting room for the simplified prototype.

# TODO: Create the gameplay loop required by the milestone.
# Within the loop, complete the required behavior in small steps:
#   1. Display the current room.
#   2. Prompt the player for a movement command or "exit".
#   3. Use decision branching to handle a valid move, exit, or invalid input.
#   4. Update the current room only when the command should move the player.
#   5. End the loop when the required exit condition is reached.

# TODO: Run and debug the program using the cases listed in prototype/README.md.
