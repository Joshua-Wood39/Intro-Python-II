# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, start_room, backpack=[]):
        self.name = name
        self.current_room = start_room
        self.backpack = backpack

    def move_p(self, direction):
        if getattr(self.current_room, f'{direction}_to') is not None:
            self.current_room = getattr(self.current_room, f'{direction}_to')
            print(f'{self.current_room.name}.\n{self.current_room.description}')
            print(f'Backpack: {self.backpack}')
        else:
            print(f"\n#############\n Can't go that way! \n#############")

    def item_act(self, act, item):
        if act == 'pickup':
            if item in self.current_room.items:
                self.backpack.append(item)
                print(f'You picked up the {item}!')
            else:
                print(f"Uhm, you can't do that...")
        elif act == 'drop':
            self.backpack.remove(item)
            self.current_room.items.append(item)
            print(f'You dropped the {item}...')
