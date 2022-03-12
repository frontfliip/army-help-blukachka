"""
A game module
"""


class Location:
    """
    A class that represents a location
    """
    def __init__(self, name, description) -> None:
        """
        Parameters
        ----------
        name : str
           The name of the location
        description: str
            The description of the location
        """
        self.name = name
        self.description = description
        self.character = None
        self.linked_locs = []
        self.item = None

    def get_name(self) -> str:
        """
        Returns the name of location
        """
        return self.name

    def describe(self) -> str:
        """
        Describes the location
        """
        print(self.description)

    def set_character(self, character) -> None:
        """
        Adds the character to the location
        """
        self.character = character

    def get_character(self) -> object:
        """
        Returns the character of the location
        """
        return self.character

    def set_item(self, item) -> None:
        """
        Adds the item
        """
        self.item = item

    def link_loc(self, next_loc, direction) -> None:
        """
        Adds the closest locs to the list
        """
        self.linked_locs.append((next_loc, direction))

    def move(self, direction) -> object:
        """
        Changes the location
        """
        for loc in self.linked_locs:
            if direction in loc:
                return loc[0]

    def get_directions(self) -> str:
        """
        Prints all closest locations and its directions
        """
        for direction in self.linked_locs:
            print(f"The {direction[0].name} is {direction[1]}")

    def get_item(self) -> object:
        """
        Returns the item of the location
        """
        return self.item


class Item:
    """
    A class that represents the item
    """
    def __init__(self, name, description) -> None:
        """
        Parameters
        ----------
        name : str
           The name of the item
        description: str
            The description of the item
        """
        self.name = name
        self.description = description

    def get_name(self) -> str:
        """
        Returns the name of the location
        """
        return self.name

    def describe(self) -> str:
        """
        Describes the item
        """
        return (f", the {self.description}")

    def get_description(self) -> str:
        """
        Returns the description of the item
        """
        return self.description


class Character:
    """
    Parent class for all characters in the game
    """
    def __init__(self, descrption, name, conversation) -> None:
        """
        Parameters
        ----------
        conversation : str
            The replica of the character
        description : str
            The description of the character
        name : str
            The name of the character
        """
        self.description = descrption
        self.name = name
        self.conversation = conversation

    def get_name(self) -> str:
        """
        Returns the name of the character
        """
        return self.name

    def describe(self) -> str:
        """
        Describes the character
        """
        print(f"{self.name} is here!")
        print(self.description)

    def talk(self) -> str:
        """
        Prints the replica of the character
        """
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
    A class that represents the student
    """
    def __init__(self, name, descrption) -> None:
        """
        Parameters
        ----------
        description: str
            The description of the student
        name : str
            The name of the student
        """
        self.description = descrption
        self.name = name
        self.location = None
        self.direction = None
        self.conversation = None
        self.item = None
        super().__init__(descrption, name, self.conversation)

    def attach_location(self, location, direction) -> None:
        """
        Adds a secret location to the student
        """
        self.location = location
        self.direction = direction

    def set_conversation(self, replica) -> None:
        """
        Adds the replica of the student
        """
        self.conversation = replica


class Policeman(Character):
    """
    A class that represents the policeman
    """
    def __init__(self, name, descrption) -> None:
        """
        Parameters
        ----------
        description: str
            The description of the student
        name : str
            The name of the student
        """
        self.description = descrption
        self.name = name
        self.conversation = None
        self.item = None
        self.key = None
        super().__init__(descrption, name, self.conversation)

    def set_key(self, key) -> None:
        """
        Adds a key to the policeman
        """
        self.key = key

    def set_conversation(self, replica) -> None:
        """
        Adds the replica of the policeman
        """
        self.conversation = replica


class Main_volonteer(Character):
    def __init__(self, name, descrption) -> None:
        """
        Parameters
        ----------
        description: str
            The description of the student
        name : str
            The name of the student
        """
        self.description = descrption
        self.name = name
        self.conversation = None
        self.key = "volonteer_key"
        self.item = None
        super().__init__(descrption, name, self.conversation)

    def set_conversation(self, replica) -> None:
        """
        Adds the replica of the volonteer
        """
        self.conversation = replica

    def set_item(self, item) -> None:
        """
        Adds an item for the volonteer
        """
        self.item = item
