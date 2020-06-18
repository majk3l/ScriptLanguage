# Lab #02 - Defining functions

### Exercises:

### 02.1: Histogram
Define function, which takes string as input and returns its histogram (pairs: character - number of occurances). The result should be a dictionary. Example:

```python
>>> histogram("Ala ma kota")
{'t': 1, 'a': 3, 'l': 1, 'A': 1, 'k': 1, 'm': 1, 'o': 1}
```

### 02.2: Poker game

Define functions that will be needed to implement simple poker game (5-card draw poker):

**02.2.1:** ``` deck() ``` - returns a list that represents deck of cards ordered from lowest to highest ( https://en.wikipedia.org/wiki/Standard_52-card_deck ). Each card has 2 attributes, that are strings:

- rank - possible values: ``` '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A' ```
- color - possible values: 
  - ```'c'``` - &clubs; **c**lubs
  - ```'d'``` - &diams; **d**iamonds
  - ```'h'``` - &hearts; **h**earts
  - ```'s'``` - &spades; **s**pades
 
Each element (card) is a tuple in a form: (rank, color). For example *ace of spades*:
 
 # &#127137;
 
will be represented as ```('A', 's')```. List should contain 52 elements (cards of 13 ranks * 4 colors).
 
**02.2.2:** ```shuffle_deck(deck)``` - takes list of cards, and shuffles them (random permutation). Take a look at the docs: https://docs.python.org/3/library/random.html

**02.2.3:** ```deal(deck, n)``` - Takes ```deck``` of cards and number of players (```n```) as input, returns n-element list of 5-element lists with cards drawn to players. Each 5-element list of cards contains 5 tuples. Example result of drawing cards to two players:

```
[[('2', 'c'), ('2', 's'), ('8', 'h'), ('8', 's'), ('A', 'h')],
[('3', 'c'), ('3', 's'), ('9', 'h'), ('9', 's'), ('K', 'h')]]   
```

--- 


