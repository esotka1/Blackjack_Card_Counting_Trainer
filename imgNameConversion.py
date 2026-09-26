import os

# Folder containing the card images
folder = "images/cards"

# Suit conversion
suit_map = {
    "C": "Hearts",
    "D": "Clubs",
    "H": "Diamonds",
    "S": "Spades"
}

# Rename every file in the folder
for filename in os.listdir(folder):

    # Skip non-png files
    if not filename.endswith(".png"):
        continue

    old_path = os.path.join(folder, filename)

    # Remove extension
    name = filename[:-4]

    # Example: C2
    suit_letter = name[0]
    rank = name[1:]

    # Convert suit
    suit = suit_map[suit_letter]

    # Create new filename
    new_name = f"{rank}_{suit}.png"

    new_path = os.path.join(folder, new_name)

    # Rename file
    os.rename(old_path, new_path)

    print(f"{filename} -> {new_name}")