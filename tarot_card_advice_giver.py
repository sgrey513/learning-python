import random
my_advice = ''

#major and minor arcana work differently, so we'll have to determine which one we have before we go further.
card_types = ['Major Arcana', 'Minor Arcana']

#here are the majors, which get a one-part name
major_arcana = ['The Fool',
                'The Magician',
                'The High Priestess',
                'The Empress',
                'The Emperor',
                'The Hierophant',
                'The Lovers',
                'The Chariot',
                'Justice',
                'The Hermit',
                'Wheel of Fortune',
                'Strength',
                'The Hanged Man',
                'Death',
                'Temperance',
                'The Devil',
                'The Tower',
                'The Star',
                'The Moon',
                'The Sun',
                'Judgement',
                'The World']


#here's what i think you should consider:
major_advice = ["that you have absolutely no idea what you're in for. But by all means, move to New York and see how it goes.",
                      "setting down the freeze ray and maybe not taking over the world tonight, Brain.",
                      "watching and waiting for now. You can spill the tea later.",
                      "moving to Long Island and having a baby.",
                      "doing what you do every night: try to take over the world.",
                      "graduate school.",
                      "allowing yourself to fall in love again.",
                      "raising your rates, applying for that job, or otherwise channeling the confidence of a mediocre white man.",
                      "organizing a series of direct actions.",
                      "staying in and reading tonight. Maybe learn to code or something.",
                      "buying a vowel.",
                      "some self-care. You do a lot for others. You deserve some rest.",
                      "settling in for a while, because this isn't over.",
                      "letting go and closing this chapter in your life.",
                      "drinking less. Not judging, I'm just saying, would a dry January be so bad?",
                      "a twelve-step program.",
                      "moving immediately to the lowest windowless point in your home. This is not a drill. TAKE SHELTER NOW. Shit is about to go down.",
                      "taking a hot bath and lots of deep breaths. The things you've seen lately... But you're safe now.",
                      "getting to know them a little better before you make any big commitments.",
                      "spending the afternoon in the park. It's a gorgeous day- don't waste it inside!",
                      "making better decisions. Not that I'm judging you. But.",
                      "yourself lucky. This is about as good as it's gonna get."]
                

#for the minors we'll have to break it down by suit and rank
suits = ['Cups', 'Wands', 'Swords', 'Pentacles', 'None']
ranks = ['Ace',
        'Two',
        'Three',
        'Four',
        'Five',
        'Six',
        'Seven',
        'Eight',
        'Nine',
        'Ten',
        'Page',
        'Knight',
        'King',
        'Queen']

    
#Do I have to list them all individually?
#index by suit and then rank? so we have to pull up the suit list and then the rank advice

#let's list the advice for all the suits
cups_advice = ["double-checking the effectiveness of your birth control. I'm just saying: accidents happen.",
               "carefully, because the romantic decisions you make right now could change your life.",
               "spending some quality time with your besties, even if it has to be remotely.",
               "therapy, and maybe look into some medication options if you have insurance. If you can't make your own serotonin, store-bought is fine!",
               "a support group. Grief and loss take time to heal.",
               "reconnecting with your roots. What parts of the past do you want to keep and which can you let go?",
               "not trusting anyone easily. Lots of cons out there. Be careful.",
               "walking away. You've done all you could here.",
               "yourself lucky, and share generously.",
               "roasting chestnuts or something cozy like that: you're safe and with the people who love you most.",
               "keeping a dream diary. Your subconscious is hatching some good stuff right now.",
               "scheduling a hot date with that cutie.",
               "how to keep toxic masculinity out of your head. Honor your emotions.",
               "whether all that emotional labor you do so well is going toward the right things."]
swords_advice = ["writing those ideas down.",
               "making a damn decision already. Stop putting it off.",
               "stocking up on chocolate ice cream, which is the best known medicine for heartbreak.",
               "taking a few days off and just catching up on sleep, if you can.",
               "dumping them. Aren't you tired of fighting?",
               "going no-contact for a while so you can move on with your life.",
               "dumping them. They're cheating on you.",
               "opening your eyes and getting out of denial. You can solve this, but only if you face reality.",
               "some breathing exercises to help with your anxiety.",
               "dumping him.",
               "going to law school.",
               "thinking before you speak.",
               "leading your affinity group into battle against the police and fascists.",
                 "being slightly less ruthless with your sharp tongue and wit every now and then."]
wands_advice = ["doing that thing you've always wanted to do.",
                "bullet journaling, or maybe a fancy planner. Put some thought into your planning.",
                "the details of how you'll implement your grand plan.",
                "celebrating: you've been blessed.",
                "watching your back. People are cutthroat in this biz.",
                "what kind of ticker-tape parade will mark your glorious homecoming.",
                "how to defend what you've accomplished, because you'll need to.",
                "taking action as quickly as possible. That thing you're preparing to do? Do it now.",
                "taking a deep breath; you're almost done with this long-haul effort. You're going to make it.",
                "dialing down the drama just a bit. You feel defeated and that sucks, but keep walking.",
                "pursuing that weird but awesome idea. It might turn into something much bigger.",
                "leaving the Shire and going on an adventure.",
               "doing more leadership work. You're good at it.",
                "going for that job/promotion. You are not an impostor! You're perfectly qualified."]
pentacles_advice = ["a career in piracy (or, failing that, a startup venture).",
               "striving for work/life balance. If you figure out how to do that in a pandemic, please let me know.",
                    "participating in a team project, organized sports, or perhaps a well-organized high-level bank heist.",
                    "finding a different job. Capitalism is trying its hardest to squeeze you.",
                    "asking for help. You don't have to deal with all this alone.",
                    "sharing the wealth-- or redistributing it.",
                    "taking on a few extra projects this year. It'll be hard work, but you'll be glad later.",
                    "taking your skills to the next level and honing your craft.",
                    "putting a hot tub next to your infinity pool-- might as well enjoy what you've got.",
                    "hosting more dinner parties-- you have such a warm and inviting home.",
                    "starting a retirement account now, while you've got time to build it up. And don't forget your savings account.",
                    "spicing up the whole office's week with 'Hawaiian Shirt Fridays'. Then no one will call you boring.",
                    "expanding your media empire with some lucrative branding opportunities, like projecting your face onto the moon.",
                    "becoming a counselor, given all the good life advice you've dispensed to other women over cups of tea in your sunny kitchen."]

#let's set up our variables
i = 0
your_card_rank = ''
your_card_suit = ''
your_card_major = ''
your_card_minor = ''
your_card_suit_number = 0
rank_numbers = []
suit_numbers = []
your_card_rank_number = 0
your_card_major_number = 0
number_of_suits = 0
number_of_ranks = 0
my_advice = ''
magic_number = 0

#is it a major arcana or minor?
#pick a number from 0 to 77
magic_number = random.randint(0, 77)

#under 22 is major. if it's major, pull up the advice for that card
if magic_number < 22:
    your_card_suit_number = 4 
    your_card_major = major_arcana[magic_number]
    your_card_major_number = magic_number
        
    #print the card name
    print('You have drawn', your_card_major)

    #generate advice
    index = major_arcana.index(your_card_major)
    my_advice = major_advice[your_card_major_number]
    print('You should really consider', my_advice)

#if it's not major, it's minor
elif magic_number >= 22:
    #assign rank

    number_of_ranks = len(ranks)
    rank_numbers = list(range(number_of_ranks))
    your_card_rank_number = random.choice(rank_numbers)
    your_card_rank = ranks[your_card_rank_number]

    #assign suit
    number_of_suits = len(suits)
    suit_numbers = list(range(number_of_suits))                    
    your_card_suit_number = random.choice(suit_numbers)
    your_card_suit = suits[your_card_suit_number]

        #find advice
    if your_card_suit_number == 0:
        my_advice = cups_advice[your_card_rank_number]
    elif your_card_suit_number == 1:
        my_advice = wands_advice[your_card_rank_number]
    elif your_card_suit_number == 2:
        my_advice = swords_advice[your_card_rank_number]
    elif your_card_suit_number == 3:
        my_advice = pentacles_advice[your_card_rank_number]




    #print card name
    print('You have drawn the', your_card_rank, 'of', your_card_suit)
    #print advice
    print('You should really consider', my_advice)

