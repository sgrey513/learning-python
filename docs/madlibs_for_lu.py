

noun1 = input('A noun: ')
noun2 = input('A noun: ')
noun3 = input('A noun: ')
noun4 = input('A noun: ')

plural_noun1= input('A plural noun: ')
plural_noun2 = input('A plural noun: ')
plural_noun3 = input('A plural noun: ')

verb1 = input('A verb: ')
verb2 = input('A verb: ')
verb3 = input('A verb: ')
verb4 = input('A verb: ')
past_tense_verb1 = input('A past-tense verb: ')
ing_verb1 = input('A verb ending in -ing: ')
ing_verb2 = input('A verb ending in -ing: ')

adj1 = input('An adjective: ')
adj2 = input('An adjective: ')
adj3 = input('An adjective: ')
adj4 = input('An adjective: ')
adj5 = input('An adjective: ')
adj6 = input('An adjective: ')

place1 = input('A place: ')
place2 = input('A place: ')

adverb1 = input('An adverb: ')
adverb2 = input('An adverb: ')
adverb3 = input('An adverb: ')

name_of_person_in_room1 = input('Name of someone in the room: ')
name_of_person_in_room2 = input('Name of someone else in the room: ')

number1 = input('A number: ')
emotion1 = input('An emotion: ')
body_part1 = input('A part of the body: ')
job1 = input('A job: ')
insult1= input('An insulting name to call someone: ')
kind_of_building1 = input('A kind of building: ')
kind_of_person1 = input('A kind of person: ')

def get_article(str):
    vowels = 'aeiouAEIOU'
    first_char = str[0]

    if first_char in vowels:
        article = 'an'
    else:
        article = 'a'
    return article

article1 = get_article(adj1)
article2 = get_article(adj3)
article3 = get_article(kind_of_building1)
article4 = get_article(job1)
   

print('One moment while I write your story!')
print('Once upon a time there was', article1, adj1, kind_of_person1,
      'named', name_of_person_in_room1 + '.',
      name_of_person_in_room1,
      'lived in', article3, kind_of_building1,
      'in', place1 +
      '. They worked very', adverb1,
      'to', verb1, plural_noun1,
      'all day, but their secret dream was to', verb2, plural_noun2,
      'in', place2,
      'and become very', adj2 + '.')
print(name_of_person_in_room2 + ', the worst', noun1,
      'in', number1, 'towns, told',
      name_of_person_in_room1,
      'they were nothing but', article2, adj3, noun2,
      'and they should be', emotion1,
      'for what they had. But', name_of_person_in_room1,
      'shook their', body_part1,
      'and kept', ing_verb1 + '.',
      'Before long, their', adj4, plural_noun3,
      'were known far and', adverb2 + '.',
      name_of_person_in_room1,
      'was', adj5 + '.')
print('One day', article4, job1, 'for the local newspaper asked',
      name_of_person_in_room1,
      'if they wanted to', verb3,
      'anything on live', noun3 + '. They',
      past_tense_verb1,
      'right at the camera', adverb3,
      'and said, "I just want', name_of_person_in_room2,
      'to', verb4, 'that they were', adj6,
      'about me. I am', ing_verb2,
      'my best', noun4,
      'and I love it! So there,', insult1 + '."')

