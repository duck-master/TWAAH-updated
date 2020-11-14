#all code by duck_master
#written since 13 nov 2020
#open-source; licensed under MIT license

#libraries
import json
#TODO: add GPT-2 functionality

#custom classes
class Room:
    '''Represents a room.
    Properties:
        - objects (the objects in the room)
        - actions (what characters can do by default in the room)
        - exits (what rooms characters can travel from this room to)'''
    def __init__(self, objects, actions, exits):
        '''Default initializer for Room.
        [str], [str], [str] -> Room'''
        self.objects = objects
        self.actions = actions
        self.exits = exits

class House:
    '''Represents a house.
    Properties:
        - roomdict: a dictionary of Rooms, indexed by their names.'''
    def __init__(self, roomdict):
        '''Default initializer for House.
        {str:Room} -> House'''
        self.roomdict = roomdict

    def addroom(self, roomname, room):
        '''Adds a Room to the House.
        str, Room -> self'''
        self.roomdict[roomname] = room

    def __iter__(self):
        '''Implement iter(self).
        self -> dict_itemiterator'''
        return iter(self.roomdict.items())

class Actor:
    '''Represents a character.
    Properties:
        - name (the character's name)
        - loc (which room the character is in)
        - items (the items the character is carrying)
        - _done (???)'''
    def __init__(self, name, loc, items):
        '''Default initializer for Actor.
        str, Room, [str] -> Actor'''
        self.name = name
        self.loc = loc
        self.items = items
        self._done = False
        

#runnable code
#extracts the house for the story (in housedata.txt)
with open('housedata.txt', 'r') as thehousef:
	thehousetxt = thehousef.read()

thehousejson = json.loads(thehousetxt)
thehouse = House({})
for (roomname, roomjson) in thehousejson.items():
    thehouse.addroom(roomname, Room(roomjson["objects"],
                                    roomjson["actions"],
                                    roomjson["exits"]))

#testing the house
print('Here are the items in the house:')
for (roomname, room) in thehouse:
    print(f'''The {roomname}:
    - It contains the {room.objects}.
    - In it, one can {room.actions}.
    - From it, one can reach {room.exits}.
    ''')
