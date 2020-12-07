#Electric Literature's Post-Apocalyptic Novel Generator
#by Jess Zimmerman and Halimah Marcus
#coded by Sarah Grey for learning purposes and fun

name = input('What is your full name? ')

doomed_things = ['the West Coast',
                 'half the population',
                 'Los Angeles',
                 'the government',
                 'North America',
                 'the internet',
                 'the entire male population',
                 'Asia',
                 'the East Coast',
                 'New York City',
                 'the Midwest',
                 'the entire female population',
                 'civilization',
                 'Europe',
                 'most of humanity',
                 'human reproduction',
                 'all plant life',
                 'the ocean',
                 'most of Earth',
                 'the electrical grid',
                 'Africa',
                 'the water supply',
                 'the polar ice',
                 'the moon',
                 'all infrastructure',
                 'society']
                 
dangers = ['a flu pandemic',
           'a terrorist attack',
           'an earthquake',
           'a zombie attack',
           'nuclear war',
           'a second Ice Age',
           'a plague',
           'a tsunami',
           'radiation',
           'a robot uprising',
           'a doomsday machine',
           'global warming',
           'a mysterious virus',
           'aliens',
           'capitalism',
           'a new street drug',
           'drought',
           'an asteroid strike',
           'pollution',
           'an airborne toxic event',
           'an electromagnetic pulse',
           'Ice-nine',
           'World War III',
           'death rays',
           'rising oceans',
           'a solar flare']

adjectives = ['pregnant',
              'ragged',
              'superpowered',
              'solitary',
              'rogue',
              'mutant',
              'drug-addicted',
              'immune',
              'cybernetic',
              'time-traveling',
              'nihilistic',
              'rebellious',
              'pious',
              'sociopathic',
              'grief-stricken',
              'murderous',
              'clairvoyant',
              'half-dead',
              'cyberpunk',
              'resourceful',
              'determined',
              'wealthy',
              'demoralized',
              'resilient',
              'criminal',
              'nudist']
heroes = ['reality TV star',
          'millennial',
          'mother',
          'socialite',
          'scientist',
          'mystic',
          'band of misfits',
          'journalist',
          'teen',
          'deposed princess',
          'monk',
          'middle manager',
          'conspiracy theorist',
          'road warrior',
          'mailman',
          'grifter',
          'time traveler',
          'social worker',
          'musician',
          'Shakespeare troupe',
          'linguist',
          'boy and his dog',
          'soldier',
          'doomsday prepper',
          'family',
          'herbalist']
verb_phrases = ['finding',
                'creating',
                'scavenging from',
                'destroying',
                'escaping from',
                'tricking',
                'waging war on',
                'hunting down',
                'challenging',
                'outwitting',
                'submitting to',
                'infiltrating',
                'navigating',
                'discovering',
                'eating',
                'hiding in',
                'redecorating',
                'negotiating with',
                'genetically modifying',
                'becoming part of',
                'designing',
                'establishing',
                'restarting',
                'avenging',
                'battling',
                'learning to live with']
enemies = ['an army of clones',
           'a dystopian government',
           'a group of mutants',
           'a shadow government',
           'a death cult',
           'a futuristic prison',
           'a group of zombies',
           'the patriarchy',
           'a terrorist cell',
           'a pack of wild dogs',
           'abandoned homes',
           'a rival gang',
           'a medical facility',
           'a new religion',
           'a false prophet',
           'the other survivors',
           'a spaceship',
           'a military bunker',
           'the Svalbard seed vault',
           'a makeshift city',
           'the Alpha Zombie',
           'a ruined town',
           'genetically engineered cats',
           'flying bears',
           'an underground labyrinth',
           'their sense of morality']
choices = []

#DEFINE function to lowercase that shit
def lowercase_name(name):
    name_lc = ''
    name_lc = name.lower()
    name = name_lc
    return name

#DEFINE a function to ignore spaces and punctuation
def remove(name):
    #ignore the bad character by doubling the character next to it
    for i in range(0, len(name)):
        bad_chars = [' ', ',', '-', '.']
        if name[i] in bad_chars:
            name = name.replace(name[i], str(name[i + 1]))

    #how the heck do i indent this???
    return name

#DEFINE function to lengthen a short name
#if name is < 6 chars, repeat backward and then forward from first character
#till it's a palindrome
#how the hell do i do it? the book code doesn't do this
def lengthen_name(name):
    i = 0
    length = len(name)

    if length == 5:
        name = name + name[-2]
        return name

    elif length == 4:
        name = name + name[-2] + name[-3]
        return name

    elif length == 3:
        name = name + name[-2] + name[-3] + name[-2]
        return name

    elif length == 2:
        name = name + name[-2] + name[-1] + name[-2] + name[-1]

    else:
        name = name*6

    return name
   #if the original name or the palindrome
   #is longer than 6, keep only first 6 characters

#DEFINE function to shorten a long name 
def shorten_name(name):
    name = name[0] + name[1] + name[2] + name[3] + name[4] + name[5]
    #now we have a six-letter name [sarahg]
    return name

#DEFINE a function to
#turn the name into a series of six digits
#so we can key those to our lists
def process_name(name):
    
    #test name length
    #if too short, make longer
    if len(name) < 6:
        name = lengthen_name(name)
        
    #if too long, make shorter
    elif len(name) > 6:
        name = shorten_name(name)
    return name

        
#DEFINE function to turn that 6-letter word into 6 numbers
def get_indexes_from_name(name):
    i = 0
    for char in name:
    #take the first letter of the name
    #give it the int of the ordinal
    #minus 96 bc that's how ordinals work I guess
    #add that number to the list
    #and so forth for all six
        while i < 6:
            choices.append(ord(name[i]) - 96)
            i = i + 1
    #these character variables are local!
    #do not try to carry them into the next function
    #it will not go well
    #instead use the index from the choices list
        
    return choices

#use the choices list to pick things
#from the lists of story elements

def choose_doomed_thing(choices):
    doomed_thing = doomed_things[int(choices[0])]
    return doomed_thing

def choose_danger(choices):
    danger = dangers[int(choices[1])]
    return danger

def choose_adjective(choices):
    adj = adjectives[int(choices[2])]
    return adj

def choose_hero(choices):
    hero = heroes[int(choices[3])]
    return hero

def choose_action(choices):
    action = verb_phrases[int(choices[4])]
    return action

def choose_enemy(choices):
    enemy = enemies[int(choices[5])]
    return enemy
        
#DEFINE function to choose between a and an
def get_article(adj):
    vowels = 'aeiouAEIOU'
    exceptions = ['hour', 'hours']
    first_char = adj[0]

    if first_char in vowels or exceptions:
        article = 'an'
    else:
        article = 'a'
    return article

#SHOWTIME

#convert the first six characters to numbers
name = lowercase_name(name)
name = remove(name)
name = process_name(name)
choices = get_indexes_from_name(name)
#get adjective first so get_article can use it
adj = choose_adjective(choices)

doomed_thing = choose_doomed_thing(choices)
danger = choose_danger(choices)
hero = choose_hero(choices)
action = choose_action(choices)
enemy = choose_enemy(choices)

#roll title and credits
print("Electric Literature's Post-Apocalyptic Novel Generator")
print('by Jess Zimmerman and Halimah Marcus')
print('Original at https://electricliterature.com/discover-the-plot-of-your-post-apocalyptic-novel-with-our-handy-chart/')
print('coded by Sarah Grey for the hell of it while learning Python')

#i want a blank line
#is this the best way to get that?
print('')
print('Here is the plot of your post-apocalyptic novel: ')
print('After', doomed_thing, 'is destroyed by',
      danger + ',',
      get_article(adj), adj, hero,
      'must survive by', action,
      enemy + '.') 


