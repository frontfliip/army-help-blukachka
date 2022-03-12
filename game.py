"""
A game module
"""


class Location:
    """
    """
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description
        self.character = None
        self.linked_locs = []
        self.item = None

    def get_name(self):
        return self.name

    def describe(self):
        print(self.description)

    def set_character(self, character):
        self.character = character

    def get_character(self) -> object:
        """
        Returns the character of the room
        """
        return self.character
    
    def set_item(self, item):
        self.item = item

    def link_loc(self, next_loc, direction):
        """
        Adds the closest locs to the list
        """
        self.linked_locs.append((next_loc, direction))

    def move(self, direction) -> object:
        """
        Changes the room
        """
        for loc in self.linked_locs:
            if direction in loc:
                return loc[0]

    def get_directions(self) -> str:
        """
        Prints all closest rooms and its directions
        """
        for direction in self.linked_locs:
            print(f"The {direction[0].name} is {direction[1]}")

    def get_item(self):
        return self.item
class Item:
    """
    """
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def describe(self):
        return (f", the {self.description}")

    def get_description(self):
        return self.description

class Character:
    """
    """
    def __init__(self, descrption, name, conversation) -> None:
        self.description = descrption
        self.name = name
        self.conversation = conversation

    def get_name(self):
        return self.name

    def describe(self):
        print(f"{self.name} is here!")
        print(self.description)
        
    
    def talk(self):
        print("\n")
        print(self.conversation)

class Stranger(Character):
    """
    """
    def __init__(self, description) -> None:
        self.name = "Stranger"
        self.description = description
        self.conversation = None
        self.unknown_direction = None
        self.item = None
        super().__init__(description, self.name, self.conversation)

    def set_unknown_direction(self, direction):
        self.unknown_direction = direction

    def set_conversation(self, replica) -> None:
        self.conversation = replica

class Student(Character):
    """
    """
    def __init__(self, name, descrption) -> None:
        self.description = descrption
        self.name = name
        self.location = None
        self.direction = None
        self.conversation = None
        self.item = None
        super().__init__(descrption, name, self.conversation)


    def attach_location(self, location, direction):
        self.location = location
        self.direction = direction


    def set_conversation(self, replica) -> None:
        self.conversation = replica

class Policeman(Character):
    """
    """
    def __init__(self, name, descrption) -> None:
        self.description = descrption
        self.name = name
        self.conversation = None
        self.item = None
        self.key = None
        super().__init__(descrption, name, self.conversation)

    def set_key(self, key):
        self.key = key
    
    def set_conversation(self, replica) -> None:
        self.conversation = replica


class Main_volonteer(Character):
    def __init__(self, name, descrption) -> None:
        self.description = descrption
        self.name = name
        self.conversation = None
        self.key = "volonteer_key"
        self.item = None
        super().__init__(descrption, name, self.conversation)
    
    def set_conversation(self, replica) -> None:
        self.conversation = replica
    
    def set_item(self, item):
        self.item = item
    
