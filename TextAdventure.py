
# Update this text to match your story.
start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

print(start)

print("Type 'left' to go left or 'right' to go right.") # Update to match your story.
user_input = input()
if user_input == "left":
    print("You decide to go left and you come face to face with a weird ghost. The ghost asks if you trust him.")
    print("Do you trust? yes or no?") # Update to match your story.
    user_input = input()
    if user_input == "yes":
        print("The ghost smiles :) and says okay follow me") # U
    elif user_input == "no":
        print("The ghost cries :'( and runs away") # 

elif user_input == "right":
    print("You choose to go right and you find a potion") # Update to match your story.
    print("Do you drink the potion? Yes or no?") # Update to match your story.
    user_input = input()
    if user_input == "yes":
        print("YOU DIE INSTANTLY HEHE") # U
    elif user_input == "no":
        print("YOU LIVE HAPPILY EVER AFTER!") # U
