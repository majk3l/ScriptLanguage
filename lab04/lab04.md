# Lab #04 - Classes and OOP

Now we will introduce our own classes to the poker project, making the code little more object oriented. The ```poker.py``` contain some basic code that defines classes and methods, and must be completed, so the planned functionality is implemented properly. From now on, the script that will be executed is ```main.py``` and our classes are imported from a module (```poker.py```). 

### Exercises:

### 04.1: Class implementation

Complete all **TODO** tasks  from ```poker.py``` file, to achieve following functionality:

- ```Card``` - a class that represents a single card (we used generic tuple in lab02 and lab03). It should have two fields (rank and color) for the data. For backward compatibility, we need a method (```get_value()```) which will return a tuple representing the card (as before). We also need a method ```__str__``` which will return nice, human readable string that can be printed out to the console by calling ```print```.

- ```Deck``` - a class that represents a deck of cards. It should have one field - a list that will contain all the ```Card``` objects. We also need methods for shuffling and dealing the cards, and ```__str__``` for printing.

- ```Player``` -  a class that represents a poker player. Most of its functionality is already provided.

The ```poker.py``` file should contain also the functions from last lab: ```get_player_hand_rank``` and ```histogram```. 

Please notice, that in current concept, the ```get_player_hand_rank``` will take a tuple of ```Card``` objects, not a list of generic tuples as before. The function should be slightly modified (thats why we need this ```get_value()``` method in ```Card```).

Here are some example results of running the ```main.py``` script assuming complete implementation of above mentioned features:

```
New deck:
2♣ 2♦ 2♥ 2♠ 3♣ 3♦ 3♥ 3♠ 4♣ 4♦ 4♥ 4♠ 5♣ 5♦ 5♥ 5♠ 6♣ 6♦ 6♥ 6♠ 7♣ 7♦ 7♥ 7♠ 8♣ 8♦ 8♥ 8♠ 9♣ 9♦ 9♥ 9♠ 10♣ 10♦ 10♥ 10♠ J♣ J♦ J♥ J♠ D♣ D♦ D♥ D♠ K♣ K♦ K♥ K♠ A♣ A♦ A♥ A♠ 
Shuffled deck:
4♥ 9♣ 6♦ 6♣ 2♦ 8♥ 5♥ 7♠ D♦ 4♣ D♣ 5♣ 2♣ D♠ K♥ J♠ 3♣ A♦ K♣ 2♥ 8♣ A♣ J♣ 4♦ 10♦ 6♠ 3♠ 10♠ 7♦ 4♠ 10♥ 5♦ 9♥ 7♥ 7♣ 3♥ 5♠ K♠ 3♦ J♦ 10♣ 2♠ 8♠ A♠ J♥ A♥ K♦ 6♥ 9♦ 8♦ D♥ 9♠ 
Cards dealt to players:
9♠ 8♦ 6♥ A♥ A♠  : 1
D♥ 9♦ K♦ J♥ 8♠  : 0
```

```
New deck:
2♣ 2♦ 2♥ 2♠ 3♣ 3♦ 3♥ 3♠ 4♣ 4♦ 4♥ 4♠ 5♣ 5♦ 5♥ 5♠ 6♣ 6♦ 6♥ 6♠ 7♣ 7♦ 7♥ 7♠ 8♣ 8♦ 8♥ 8♠ 9♣ 9♦ 9♥ 9♠ 10♣ 10♦ 10♥ 10♠ J♣ J♦ J♥ J♠ D♣ D♦ D♥ D♠ K♣ K♦ K♥ K♠ A♣ A♦ A♥ A♠ 
Shuffled deck:
7♦ 8♣ D♠ 5♠ K♣ 7♣ 4♦ 2♦ 6♦ K♠ A♠ 9♣ 3♠ 2♣ A♥ K♥ 5♣ J♠ D♦ A♦ 4♠ 5♥ 3♣ 5♦ 10♣ J♣ J♦ 2♠ 8♠ 4♣ 9♠ A♣ 4♥ 10♦ 2♥ D♣ 10♠ D♥ J♥ 8♥ 9♥ K♦ 6♥ 7♥ 3♦ 10♥ 6♣ 3♥ 6♠ 8♦ 9♦ 7♠ 
Cards dealt to players:
7♠ 8♦ 3♥ 10♥ 7♥  : 1
9♦ 6♠ 6♣ 3♦ 6♥  : 3
```
