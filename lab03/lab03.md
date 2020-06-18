# Lab #03 - Coding functions: practice

### Exercises:

### 03.1:

Implement function ```hand_rank(hand)```, which will take as input list of 5 tuples (representing player hand - refer to lab02) and return an ```int``` in range from 10 to 1 that will represent player hand strength in 5 card draw poker game (https://en.wikipedia.org/wiki/List_of_poker_hands), where 10 - royal flush, 9 - straight flush , 8 - four of a kind etc.

Use ```poker.py``` (from this repo) as a template. Add your implementation of ```histogram()``` function from previous lab.

Each hand falls into a hand-ranking category determined by the patterns formed by its cards. There are some rules to check:

- five cards are in one suit,
- five cards of sequential rank,
- some ranks occur more then once.

Use ```histogram()``` from previous lab to check if some ranks occur more then once. If we create list of cards' ranks, we can check it for some pairs, three of a kind and four of a kind. For example, if we have list:

```[('A','h'), ('A','c'), ('A','s'), ('9','c'), ('8','s')]```

Which is a following hand:

 # &#127153; &#127185; &#127137; &#127193; &#127144;

we can create list of the ranks:

```['A', 'A', 'A', '9', '8']```

using ```histogram()``` on that list we can get dictionary:

```{'8': 1, '9': 1, 'A': 3}```

when we check the values, we will know if there is more than one occurence of some rank (In this case it was Ace).
