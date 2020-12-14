Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> marbles = [10, 13, 39, 14, 41, 9, 3]
>>> sum(marbles)
129
>>> print("The total is", sum(marbles))
The total is 129
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /random/marble sums.py
The total is 129
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /random/recursive_marbles.py
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /random/recursive_marbles.py
The total is 129
>>> firstmarbles = [10, 13, 39, 14, 41, 9, 3]
>>> rest
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    rest
NameError: name 'rest' is not defined
>>> marbles
[10, 13, 39, 14, 41, 9, 3]
>>> sum
129
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: ravens
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: ravens
Traceback (most recent call last):
  File "/Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py", line 9, in <module>
    palindrome_check(word)
TypeError: palindrome_check() takes 0 positional arguments but 1 was given
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: bytts
odd
>>> sarah
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    sarah
NameError: name 'sarah' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: sarah
odd
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: even steven
odd
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/odds_evens.py
Please enter a word: evensteven
even
>>> word = roland
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    word = roland
NameError: name 'roland' is not defined
>>> word = 'roland'
>>>     if len(word)%2 == 0:
        if i in word < (len(word)/2) 
            first_half.append()
            print(first_half)
            
SyntaxError: unexpected indent
>>> 
>>> if len(word)%2 == 0:

	if i in word < (len(word)/2) 
            first_half.append()
            print(first_half)
            
SyntaxError: invalid syntax
>>> if len(word)%2 == 0:
    if i in word < (len(word)/2) 
        first_half.append()
        print(first_half)

SyntaxError: invalid syntax
>>> if len(word)%2 == 0:
    if i in word < (len(word)/2):
        first_half.append()
        print(first_half)

        
Traceback (most recent call last):
  File "<pyshell#15>", line 2, in <module>
    if i in word < (len(word)/2):
NameError: name 'i' is not defined
>>> if len(word)%2 == 0:
    first_half = word[0:(len(word)/2)-1]
    back_half = word[(len(word):-1)]

SyntaxError: invalid syntax
>>> if len(word)%2 == 0:
    first_half = word[0:(len(word)/2)-1]
    back_half = word[(len(word)):-1]

    
Traceback (most recent call last):
  File "<pyshell#18>", line 2, in <module>
    first_half = word[0:(len(word)/2)-1]
TypeError: slice indices must be integers or None or have an __index__ method
>>> if len(word)%2 == 0:
    first_half = word[0:int(len(word)/2)-1]
    back_half = word[int(len(word)):-1]

    
>>> word = "roland"
>>> if len(word)%2 == 0:
    first_half = word[0:int(len(word)/2)-1]
    back_half = word[int(len(word)):-1]
    print(first_half, "and", back_half)

    
ro and 
>>> if len(word)%2 == 0:
    first_half = word[0:int(len(word)/2)]
    back_half = word[int(len(word)):-1]

    
>>> if len(word)%2 == 0:
    first_half = word[0:int(len(word)/2)]
    back_half = word[int(len(word)):-1]
    print(first_half, "plus", back_half)

    
rol plus 
>>> first_half
'rol'
>>> back_half
''
>>> word
'roland'
>>> if len(word)%2 == 0:
    i = len(word)/2
    first_half = word[0:(i-1))]
    back_half = word[i:]
    print(first_half, "plus", back_half)
    
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
>>> if len(word)%2 == 0:
    i = len(word)/2
    first_half = word[0:(i-1)]
    back_half = word[i:]
    print(first_half, "plus", back_half)

    
Traceback (most recent call last):
  File "<pyshell#34>", line 3, in <module>
    first_half = word[0:(i-1)]
TypeError: slice indices must be integers or None or have an __index__ method
>>> word
'roland'
>>> len(word)
6
>>> len(word)/2
3.0
>>> if len(word)%2 == 0:
    i = int(len(word)/2)
    first_half = word[0:(i-1)]
    back_half = word[i:]
    print(first_half, "plus", back_half)

    
ro plus and
>>> if len(word)%2 == 0:
    i = int(len(word)/2)
    first_half = word[0:i]
    back_half = word[i:]
    print(first_half, "plus", back_half)

    
rol plus and
>>> center = word[i]
>>> print(center)
a
>>> word = raven
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    word = raven
NameError: name 'raven' is not defined
>>> word = "raven"
>>> word
'raven'
>>> center
'a'
>>> center = word[i+1]
>>> center
'n'
>>> i
3
>>> i = int(len(word)/2)
>>> i
2
>>> len(word)
5
>>>     i = int((len(word)-1)/2)
    
SyntaxError: unexpected indent
>>> i = int((len(word)-1)/2)
>>> i
2
>>> len(word)
5
>>> len(word)-1
4
>>> (len(word)-1)/2
2.0
>>> int(len(word)-1)/2
2.0
>>> int((len(word)-1)/2)
2
>>> i = int((len(word)-1)/2)
>>> i
2
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
ra plus ven
odd number of letters
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
ra plus e plus en
odd number of letters
>>> center
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    center
NameError: name 'center' is not defined
>>>         i = int((len(word)-1)/2)
        center = word[i+1]
        first_half = word[0:i]
        back_half = word[i+1:]
        print(first_half, "plus", center, "plus", back_half)
        print("odd number of letters")
        
SyntaxError: unexpected indent
>>>     i = int((len(word)-1)/2)
        center = word[i+1]
        first_half = word[0:i]
        back_half = word[i+1:]
        print(first_half, "plus", center, "plus", back_half)
        print("odd number of letters")
        
SyntaxError: unexpected indent
>>> i = int((len(word)-1)/2)
        center = word[i+1]
        first_half = word[0:i]
        back_half = word[i+1:]
        print(first_half, "plus", center, "plus", back_half)
        print("odd number of letters")
        
SyntaxError: multiple statements found while compiling a single statement
>>> i = int((len(word)-1)/2)
center = word[i+1]
first_half = word[0:i]
back_half = word[i+1:]
print(first_half, "plus", center, "plus", back_half)
print("odd number of letters")

SyntaxError: multiple statements found while compiling a single statement
>>> i = -((len(word)+1)/2)
>>> word
'raven'
>>> i
-3.0
>>> i = -(int((len(word)+1)/2))
>>> i
-3
>>> word[i]
'v'
>>> i = -(int((len(word)+1)/2))
center = word[i]
first_half = word[0:i-1]
back_half = word[i+1:]
print(first_half, "plus", center, "plus", back_half)
print("odd number of letters")

SyntaxError: multiple statements found while compiling a single statement
>>> length = int(len(word))
center_slot = (length + 1)/2
i = -(center_slot)
center = word[i]
first_half = word[0:i-1]
back_half = word[i+1:]
print(first_half, "plus", center, "plus", back_half)
print("odd number of letters")
SyntaxError: multiple statements found while compiling a single statement
>>> length = int
length = len(word)
SyntaxError: multiple statements found while compiling a single statement
>>> length = int(len(word))

>>> length
5
>>> center_slot = (length + 1)/2

>>> 
>>> center_slot
3.0
>>> center_slot = int((length + 1)/2)
>>> center_slot
3
>>> center
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    center
NameError: name 'center' is not defined
>>> word = lucia
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    word = lucia
NameError: name 'lucia' is not defined
>>> word = "lucia"
>>> length
5
>>> center_slot
3
>>> i
-3
>>> word[i]
'c'
>>> first_half = word[0:i-1]

>>> first_half
'l'
>>> first_half = word[0:i]
>>> first_half
'lu'
>>> back_half = word[i+1:]
>>> back_half
'ia'
>>> print(first_half, "plus", center, "plus", back_half)

Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    print(first_half, "plus", center, "plus", back_half)
NameError: name 'center' is not defined
>>> center = word[i]
>>> print(first_half, "plus", center, "plus", back_half)

lu plus c plus ia
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: joseph
jos plus eph
even number of letters
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: saraj
sa plus r plus aj
odd number of letters
>>> word.reverse
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    word.reverse
AttributeError: 'str' object has no attribute 'reverse'
>>> backward = str.reverse(back_half)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    backward = str.reverse(back_half)
AttributeError: type object 'str' has no attribute 'reverse'
>>> help(split)
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    help(split)
NameError: name 'split' is not defined
>>> help(text.split)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    help(text.split)
NameError: name 'text' is not defined
>>> help(str.split)
Help on method_descriptor:

split(self, /, sep=None, maxsplit=-1)
    Return a list of the words in the string, using sep as the delimiter string.
    
    sep
      The delimiter according which to split the string.
      None (the default value) means split according to any whitespace,
      and discard empty strings from the result.
    maxsplit
      Maximum number of splits to do.
      -1 (the default value) means no limit.

>>> back_half
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    back_half
NameError: name 'back_half' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: roland
rol plus and
even number of letters
>>> back_half
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    back_half
NameError: name 'back_half' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
ra plus v plus en
odd number of letters
>>> back_half
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    back_half
NameError: name 'back_half' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
>>> turned
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    turned
NameError: name 'turned' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
Traceback (most recent call last):
  File "/Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py", line 45, in <module>
    turned = back_half.reverse()
NameError: name 'back_half' is not defined
>>> word
'redder'
>>> split(word)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    split(word)
NameError: name 'split' is not defined
>>> text.split(word)
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    text.split(word)
NameError: name 'text' is not defined
>>> word.split
<built-in method split of str object at 0x7f9f7c754fb0>
>>> word.split(word)
['', '']
>>> word
'redder'
>>> type(word)
<class 'str'>
>>> letters = word.split[]
SyntaxError: invalid syntax
>>> letters = word.split(word)
>>> letters
['', '']
>>> word
'redder'
>>> letters = word.split()
>>> letters
['redder']
>>> len(letters)
1
>>> def analyze_word(str):

    #odd or even?
    if len(word)%2 == 0:

        #even numbers: split in 2 halves
        even = True
        i = int(len(word)/2)
        first_half = word[0:i]
        back_half = word[i:]
        print(first_half, "plus", back_half)
        print("even number of letters")
        return first_half
        return back_half
    
    else:
        #odd numbers: pull out the center character
        #then the strings before and after it
        even = False
        length = int(len(word))
        center_slot = int((length + 1)/2)
        i = -(center_slot)
        center = word[i]
        first_half = word[0:i]
        back_half = word[i+1:]
        print(first_half, "plus", center, "plus", back_half)
        print("odd number of letters")

        return first_half
        return back_half
        return center

>>> word = redder
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    word = redder
NameError: name 'redder' is not defined
>>> word = "redder"
>>> analyze_word(word)
red plus der
even number of letters
'red'
>>> letters = list()
>>> print(list(word))
['r', 'e', 'd', 'd', 'e', 'r']
>>> letters = list(word)
>>> print(letters)
['r', 'e', 'd', 'd', 'e', 'r']
>>> first_half
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    first_half
NameError: name 'first_half' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
Traceback (most recent call last):
  File "/Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py", line 2, in <module>
    turned = back_letters.reverse()
NameError: name 'back_letters' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
Traceback (most recent call last):
  File "/Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py", line 51, in <module>
    print("The word starts with", first_half, "and ends with", back_half)
NameError: name 'first_half' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
The word starts with ['r', 'e', 'd'] and ends with ['d', 'e', 'r']
Traceback (most recent call last):
  File "/Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py", line 52, in <module>
    if center:
NameError: name 'center' is not defined
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
The word starts with ['r', 'e', 'd'] and ends with ['d', 'e', 'r']
This word is not a palindrome.
>>> turned
>>> print(turned)
None
>>> first_letters
['r', 'e', 'd']
>>> back_letters
['d', 'e', 'r']
>>> back_letters.reverse()
>>> print(back_letters)
['r', 'e', 'd']
>>> turned
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
The word starts with ['r', 'e', 'd'] and ends with ['d', 'e', 'r']
This word is not a palindrome.
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: redder
red plus der
even number of letters
The word starts with ['r', 'e', 'd'] and ends with ['d', 'e', 'r']
This word is a palindrome.
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: raven
ra plus v plus en
odd number of letters
The word starts with ['r', 'a'] and ends with ['e', 'n']
This word is not a palindrome.
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: tacocat
tac plus o plus cat
odd number of letters
The word starts with ['t', 'a', 'c'] and ends with ['c', 'a', 't']
This word is a palindrome.
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: rainbow
rai plus n plus bow
odd number of letters
The word starts with ['r', 'a', 'i'] and ends with ['b', 'o', 'w']
This word is not a palindrome.
>>> 
= RESTART: /Users/sgrey/Documents/Head First Learn to Code /headfirstlearntocode-master/ch8/mine/palindrome_checker.py
Please enter a word: amanaplanacanalpanama
amanaplana plus c plus analpanama
odd number of letters
The word starts with ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a'] and ends with ['a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']
This word is a palindrome.
>>> 