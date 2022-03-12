"""
The main file
"""
import game


stryi_park = game.Location("Stryi park", "A huge park in Lviv")
ucu = game.Location("UCU", "A great university that is always ready to help")
volonteer_centre = game.Location("Volonteer centre", "A place where all volonteers come together")
rinok_squere = game.Location("Rinok Squere", "The centre of Lviv")
blockpost = game.Location("Blockpost", "Here policemen have to check your documents and permissions")
destenation = game.Location("Destenation", "Place where help is needed")

stryi_park.link_loc(rinok_squere, "south")
stryi_park.link_loc(volonteer_centre, "west")
ucu.link_loc(stryi_park, "south")
volonteer_centre.link_loc(rinok_squere, "west")
volonteer_centre.link_loc(stryi_park, "east")
rinok_squere.link_loc(volonteer_centre, "east")
rinok_squere.link_loc(stryi_park, "north")
blockpost.link_loc(volonteer_centre, "west")
volonteer_centre.link_loc(destenation, "north")


volonteer_key = game.Item("volonteer key", "key that allows to go to the volonteer centre")
helmet = game.Item("helmet", "new military helmet")
body_armor = game.Item("body armor", "new military body armor")
apple = game.Item("apple", "fresh food which will certanly be useful")


ucu.set_item(body_armor)
rinok_squere.set_item(apple)
volonteer_centre.set_item(helmet)


student = game.Student("Ivan", "A young UCU student that is always ready to help")
student.attach_location(ucu, "south")
student.set_conversation(f"[{student.get_name()}]: Hi, I can help you. You can visit UCU and get some help. You can go there from the Stryi park")

stranger = game.Stranger("An old unkown man. You can ask him a direction")
stranger.set_conversation(f"[{stranger.get_name()}]: Good day! I can tell you the direction if you need")
stranger.set_unknown_direction("north")

policeman = game.Policeman("Policeman", "A kind policeman")
policeman.set_conversation(":)")
policeman.set_key(volonteer_key)

volonteer = game.Main_volonteer("Volonteer", "A guy who is ready to help you")
volonteer.set_item(volonteer_key)
volonteer.set_conversation(f"[{volonteer.get_name()}]: Hi there! If you need a key I can give it to you")


stryi_park.set_character(stranger)
blockpost.set_character(policeman)
rinok_squere.set_character(student)
volonteer_centre.set_character(volonteer)

current_location = rinok_squere
play = True
backpack = []
check_student = 0
check_stranger = 0
print("\n")
print("Hi, your mission is to find three important items(apple, helmet, body armor) and bring them to destenation. All found items will be in your backpack")
print("U're able to talk with characters, take their items or take items on different locations. And also move through locations")
print("Good luck!")
while play:
    print("\n")
    print(current_location.name)
    current_location.describe()
    print("-"*20)
    current_location.get_directions()

    inhabitant = current_location.get_character()
    item = current_location.get_item()

    if item is not None:
        print("\n")
        print(f"There is a(an) {item.name} here{item.describe()}. You can take it")

    if inhabitant is not None:
            print("\n")
            inhabitant.describe()
            if inhabitant.item is not None:
                print("\n")
                print(f"He has a {inhabitant.item.get_name()}{inhabitant.item.describe()}")

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        # Move in the given direction
        back = current_location
        current_location = current_location.move(command)
        if current_location == destenation:
            if helmet.get_name() not in backpack or apple.get_name() not in backpack or body_armor.get_name() not in backpack:
                print("\n")
                print("Are you sure you've found all necesary things?")
                print("You have to find them all frist")
                current_location = back
                continue
            current_location = blockpost
    elif command == "talk":
        # Talk to the inhabitant

            if inhabitant is not None:
                if type(inhabitant).__name__ == "Student" and check_student == 0:
                    stryi_park.link_loc(ucu, "???")
                    check_student = 1
                if type(inhabitant).__name__ == "Stranger" and check_stranger == 0 and check_student == 1:
                    for loc in current_location.linked_locs:
                        if ucu in loc:
                            current_location.linked_locs.remove(loc)
                            stryi_park.link_loc(ucu, inhabitant.unknown_direction)
                    check_stranger = 1
                if type(inhabitant).__name__ == "Policeman":
                    print("\n")
                    print(f"[{inhabitant.get_name()}]: You need a permission to leave the city")
                    if volonteer_key.get_name() in backpack:
                        print(f"[You]: Yes")
                        print(f"[{inhabitant.get_name()}]: Okey, have a nice trip!")
                        print("\n")
                        print("You have finished your mission!")
                        play = False
                    else:
                        print(f"[You]: No")
                        print(f"[{inhabitant.get_name()}]: Oh, you have to ask a volonteer for it. See you later")
                inhabitant.talk()
            else:
                print("\n")
                print("There is no one to talk with")
    elif command == "take":
        if item is not None:
            print("\n")
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_location.set_item(None)
        else:
            print("\n")
            print("There is nothing to take")
    elif command == "backpack":
        print("\n")
        print("In your backpack are:")
        for elem in backpack:
            print(elem)
    elif command == "take from friend":
        if inhabitant is not None:
            if inhabitant.item is not None:
                print("\n")
                print("You put the " + inhabitant.item.get_name() + " in your backpack")
                backpack.append(inhabitant.item.get_name())
                inhabitant.item = None
            else:
                print("\n")
                print("There is nothing to take")
        else:
            print("\n")
            print("There is no one in here or there is nothing to take")
    else:
        print("\n")
        print("I don't know how to " + command)
