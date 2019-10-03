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
            print(
                f'\n=============\n {self.current_room.name}.\n{self.current_room.description} \n=============')
            print(
                f'\n-------------\n Backpack: {self.backpack} \n-------------')
        else:
            print(f"\n#############\n Can't go that way! \n#############")

    def item_act(self, act, item):
        print(type(self.current_room.items))
        print(type(item))
        if act == 'pickup':
            pickup_item, pickup_idx = None, None
            for idx, i in enumerate(self.current_room.items):
                if i.name.lower() == item.lower():
                    pickup_idx = idx
                    pickup_item = i
                    break
            if not pickup_item:
                print(
                    f"\n#############\n Uhm, you can't do that... \n#############")
            else:
                self.backpack.append(self.current_room.items.pop(pickup_idx))
                print(
                    f'\n#############\n You picked up the {item}! \n#############')

        elif act == 'drop':
            self.backpack.remove(item)
            self.current_room.items.append(item)
            print(
                f'\n#############\n You dropped the {item}... \n#############')
