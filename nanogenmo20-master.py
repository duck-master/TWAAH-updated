#all code by duck_master
#written since 13 nov 2020
#open-source licensed under MIT license

#libraries
import json                     #for interpreting house files
from random import *            #for randomization
from datetime import *          #for (in-universe) timestamps
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
      :str:Room -> House'''
        self.roomdict = roomdict

    def addroom(self, roomname, room):
        '''Adds a Room to the House.
        str, Room -> self'''
        self.roomdict[roomname] = room

    def __iter__(self):
        '''Implement iter(self).
        self -> dict_itemiterator'''
        return iter(self.roomdict.items())
    
    def roomof(self, actor):
        '''Returns the room that a character is in.
        self, Actor -> Room'''
        return thehouse.roomdict[actor.loc]

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

    def leaveRoom(self, room):
        '''Represents character leaving room.
        self, Room -> None'''
        if (uniform(0, 1) < 0.6):
            self.loc = choice(room.exits)
    
    def commentObject(self, objects, otherPlayer):
        '''Function for an Actor to comment on objects in the room.
        self, [str] -> None
        prints str'''
        if(len(objects) > 0):
            newRoom(self)
            talkAboutObject(self.name, choice(objects))
            if uniform(0, 1) < 0.25:
                self.think(otherPlayer)
                
    def action(self, actions, otherPlayer):
        '''Function for an Actor to perform actions.
        self, [str] -> None
        prints str'''
        if(len(actions) > 0):
            newRoom(self)
            print(f'\n{self.name} {choice(actions)}')
            if uniform(0, 1) < 0.25:
                self.think(otherPlayer)

    def think(self, otherPlayer):
        '''Function for a Player to reflect.
        self, Actor -> None
        prints str'''
        feelings = ['loved', 'hated', 'envied', 'liked']
        possibleThoughts = [
            f'She thought about {otherPlayer.name}.',
            f'She {choice(feelings)} her so damn much.',
            f'She wanted that {choice(otherPlayer.items)}. Nothing else would do',
            f'It was almost too much to deal with',
            f'Why couldn\'t she be more like her?',
            f'Maybe if they could just be real with each other for once... ',
            f'Nobody really knew how she felt. ',
            f'Why did everyone want to be like her? ',
            f'Just thinking about it made her want to puke. ',
            f'Why did she come to this stupid house party in the first place?'
        ]
        thoughts = ''
        for pt in possibleThoughts:
            if uniform(0, 1) < 0.4:
                thoughts += pt
        #TODO: augment with GPT-2
        return thoughts
    

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
#print('Here are the items in the house:')
#for (roomname, room) in thehouse:
#	print(f'''The:roomname:
#	- It contains the:room.objects.
#	- In it, one can:room.actions.
#	- From it, one can reach:room.exits.
#	''')
#print("end")

#TODO: initializing names
with open('names.txt', mode = 'r') as f:
    nameslines = f.readlines()

names = [nameslines[2*i][1:-2] for i in range(1, len(nameslines)//2)]

#initializing characters
def makeItems(num):
  adjectives = [
    'crimson',
    'teal',
    'ostentatious',
    'fashionable',
    'aquamarine',
    'emerald',
    'amazing',
    'incredible',
    'mind-blowing'
  ]
  nouns = [
    'scarf',
    'sweater',
    'hat',
    'skirt',
    'necklace',
    'phone',
    'purse',
    'belt',
    'watch',
    'jacket',
    'shirt',
    'coat'
  ]
  return [choice(adjectives) + ' ' + choice(nouns) for i in range(num)]

players = [Actor(choice(names), "front yard", makeItems(2)) for i in range(6)]

print(', '.join([player.name for player in players]) + ' found themselves dropped off at the same house. How awkward.')

#data
looked = [
  'seemed',
  'looked',
  'appeared'
]

cross = [
  'cross',
  'angry',
  'concerned',
  'disinterested'
]

asked = [
  'asked',
  'inquired',
  'demanded',
  'asked',
  'asked'
]

flinched = [
  'recoiled',
  'beamed',
  'flinched',
  'squirmed',
  'sighed',
  'chuckled',
  'laughed',
  'yawned',
  'yelled'
]

with open('dreams.txt', mode = 'r') as f:
    dreams = list(map((lambda s: s[:-2]), f.readlines()))

#helper functions

#TODO: augment with GPT-2
def dialogue(actor1, actor2):
    '''Generates a conversation between two characters.
    Actor, Actor -> None
    prints str'''
    randno = uniform(0, 1)
    if randno < 0.5:
        pass
    elif randno < 0.71:
        print(f'{actor1.name} and {actor2.name} had a nice conversation.')
        #in karpathy: calls generate, generateBest, generateFav
        #TODO: replace with GPT-2 calls
    elif randno < 0.92:
        stare(actor1, actor2)
    else:
        dream(actor1, actor2)
        

def dream(actor1, actor2):
    '''Represents discussion about dreams.
    Actor, Actor -> None
    prints str'''
    pre = choice([
	actor2.name + ' looked directly at ' + actor1.name + '. "I had the weirdest dream," she said.',
	actor2.name + ' stiffened and began to ramble, not noticing ' + actor1.name + ', as if in a fugue state.',
	'"' + actor2.name + ', what did you dream about last night?" asked ' + actor1.name + '. ' + actor2.name + ' seemed wary, but her face softened.',
	'"Dreams," ' + actor1.name + ' said. "Tell me about your dreams." ' + actor2.name + ' almost said nothing, but thought better of it.',
	actor2.name + ' was crying. ' + actor1.name + ' acted on instinct. "Tell me all about it." she said. ' + actor2.name + ' obliged in an unbecoming outpouring.',
    ])
    encounter(actor1, actor2)
    print(pre + '\n', end = choice(dreams))

def stare(actor1, actor2):
    '''Represents two characters uncomfortably staring at one another.
    Actor, Actor -> None
    prints str'''
    print('\n');
    encounter(actor1, actor2);
    print(choice([
        actor1.name + ' stared at ' + actor2.name + ' suspiciously.',
        actor1.name + ' avoided ' + actor2.name + '.',
        actor1.name + ' eyed ' + actor2.name + '\'s ' + choice(actor2.items) + ' with envy.',
        '"Where did you get that ' + choice(actor2.items) + ', ' + actor2.name + '?" ' + actor2.name +' ignored her.',
        actor1.name + ' played nervously with her ' + choice(actor1.items) + ' in a successful bid to avoid talking to ' + actor2.name + '.'
    ]))
    if (uniform(0, 1) < 0.25):
        actor1.think(actor2)

def solo(actor):
    '''Describes a character doing stuff in a room alone.
    Actor -> None
    prints str'''
    if(uniform(0, 1) > 0.2):
        if (uniform(0, 1) < 0.45):
            actor.commentObject(thehouse.roomof(actor).objects, choice(players))
        else:
            actor.action(thehouse.roomof(actor).actions, choice(players))

def newRoom(actor):
    '''Describing a character entering a room.
    Actor -> None
    prints str'''
    print('\n' + choice([
        'After some time, ' + actor.name + ' found herself in the ' + actor.loc + '.',
        actor.name + ' entered the ' + actor.loc + '.',
        'Nobody was in the ' + actor.loc + ', so ' + actor.name + ' found herself uncharacteristically at ease.',
        '"Perfect, I\'ve got the ' + actor.loc + ' all to myself," thought ' + actor.name + '.',
        'The ' + actor.loc + ' was empty. Finally, ' + actor.name + ' thought, somewhere she could think.',
        actor.name + ' looked around the ' + actor.loc + '.',
        actor.name + ' breathed deeply and took in sights of the ' + actor.loc + '.'
      ]))

def encounter(actor1, actor2):
    '''Describes two characters encountering each other.
    Actor, Actor -> None
    prints str'''
    print(choice([
        actor1.name + ' encountered ' + actor2.name + ' in the ' + actor1.loc + '.',
        actor1.name + ' and ' + actor2.name + ' ran into each other in the ' + actor1.loc + '.',
        actor1.name + ' entered the ' + actor1.loc + '. ' + actor2.name + ' was there, as if waiting.',
        'As ' + actor1.name + ' entered the ' + actor1.loc + ', she saw ' + actor2.name + ' making trouble.',
        actor1.name + ' found ' + actor2.name + ' in the ' + actor1.loc + '.',
        actor1.name + ' entered the ' + actor1.loc + ' to find ' + actor2.name + ' standing there.',
        actor1.name + ' walked into the ' + actor1.loc + ' and saw ' + actor2.name + '. Great.',
        'The ' + actor1.loc + ' held two items of interest to ' + actor1.name + ': the ' + choice(thehouse.roomof(actor1).objects) + ' and ' + actor2.name + '.'
    ]))

#TODO: augment with GPT-2 calls
def talkAboutObject(name, obj):
    '''Describes a character talking about an object.
    str, str -> None
    prints str'''
    talks = [
	'The ' + obj + ' caught her eye. She thought it was the ugliest thing she\'d ever seen.',
	'She stared at the ' + obj + ' uncomprehendingly.',
	'"Wow, check out that ' + obj + '," she said to no one in particular.',
	'She dutifully avoided the ' + obj + ' out of some primal respect for its otherness.',
	'The ' + obj + ' reminded her of her mother. Barf.',
	'She noticed the ' + obj + '. Kinda tacky.',
	'The next thing she saw was the ' + obj + ', which left her feeling disquieted.'
    ]
    posts = [
	'Why she noticed in the first place was beyond her.',
	'She didn\'t give it a second thought.',
	'She was hoping it would distract her, if for some brief moment, from her life.',
	'Things. The house was full of things. When she got old enough to have a house, she\'d own nothing.',
	'Part of her, a larger part than she cared to admit, wanted to smash it.',
	'She wished the booze would kick in.',
	'She heard a noise from somewhere else in the house.'
    ]
    print('\n' + choice(talks) + ' ' + choice(posts))

#main code
def generateVignettes():
    '''The main function.
    None -> None
    prints str'''
    dialogues = []
    for player in players:
        player.leaveRoom(thehouse.roomof(player))

    for player in players:
        othersHere = list(filter((lambda el: el.loc == player.loc and el.name != player.name), players))
        if (len(othersHere) > 0):
          other = choice(othersHere)
          dialogue(player, other)
        else:
          solo(player)

#calling the main code
timestamp = datetime(2038, 1, 18, randrange(4, 6), randrange(60), randrange(60))
vigno = 1
for i in range(800):
    print(f'\n-------------\nREPORT {vigno}\n{timestamp} PT\n') #because karpathy likes california, I'll set the mansion in PT
    generateVignettes()
    timestamp += timedelta(seconds = randrange(50, 100))
    vigno += 1
