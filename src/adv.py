from room import Room
from player import Player
from item import Item

# Declare all items

flamethrower: Item(
    'Flamethrower', "Holy crap! A flamethrower! It has a warning: don't use unless trained.")
manual: Item('Flamethrower Training Manual',
             "Detailed instructions on how to not blow yourself up.")
spoon: Item('Vorpal Spoon', "Good against monsters made of soup ... or stew.")
shield: Item('Shield of Detritus',
             "A lovely shield made of coral. Technically, dead things.")


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'hall': Room("Grand Hall", "It is a long hallway, with exits on all sides. A pedestal is in the middle...something might be on it."),

    'billiard': Room("Billiard Room", "A massive pool table adorns this room, absent of balls. Their is an empty stick rack as well...though, something glints from one of the pockets."),

    'closet': Room("Coat Closet", "You barely fit amidst the tattered remains of some once fine coats. It smells of mothballs and kerosene."),

    'kitchen': Room("Large Kitchen", "Several hearths and rusted cauldrons fill this room. Some rotting barrels and crates are stacked haphazardly about."),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['hall']
room['hall'].e_to = room['foyer']
room['hall'].n_to = room['billiard']
room['hall'].s_to = room['closet']
room['hall'].w_to = room['kitchen']
room['billiard'].s_to = room['hall']
room['closet'].n_to = room['hall']
room['kitchen'].e_to = room['hall']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['hall'].add_item(flamethrower)
room['billiard'].add_item(spoon)
room['kitchen'].add_item(shield)
room['treasure'].add_item(manual)
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('M.Swift', room['outside'], [])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ('n', 'e', 's', 'w')
act = ('pickup', 'drop')

while True:
    room = player.current_room
    print(f'You are in the {room}...')
    location = f'(n)orth: {room.n_to}\n(e)ast: {room.e_to}\n(s)outh: {room.s_to}\n(w)est: {room.w_to}\nItem in room: {room.items}'
    print(location)
    player_in = input('What do you do?')
    player_in = player_in.split()
    print(f'Input: {player_in}')
    if len(player_in) > 1:
        print(f'Input0: {player_in[0]}, Input1: {player_in[1]}')

    if player_in[0] in directions:
        player.move_p(player_in[0])
        print(f'Room items: {player.current_room.items}')
    elif player_in[0] in act:
        act = player_in[0]
        print(f'act: {act}*')
        item = player_in[1]
        print(f'item: {item}*')
        player.item_act(act, item)
    elif player_in[0] == 'q':
        print('Good game! Thanks for participating!')
        break
    else:
        print(f' Invalid input! Please use: n, e, s, w, q / pickup, drop ')
