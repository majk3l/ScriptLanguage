# Lab #05 - Simple communication using sockets and object serialization

Let's assume we want to make our poker project a multi-player. Besides the code that handles game logic and data-types we need some mechanism to send the data through network, to achieve multi-player playability on more than one machine.

The simplest way to communicate by network is to use sockets. Sockets provide OS-based software abstraction for all the low level operations that are needed to send data by network. The most common type of socket applications are client-server applications, where one side waits for connections from one or more clients. We will be using INET (i.e. IPv4) sockets (they are great majority of sockets in use) and TCP protocol. 

The simplest client will look something like that:

```python
# create INET socket object
sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to a server at port 80
sockt.connect(("www.python.org", 80))
```

When the connect completes, the socket can be used to send in a request.

Creating a server involves using more methods:

```python
# create INET socket object
servsockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind socket to a particular port
servsockt.bind((socket.gethostname(), 80))
# listen for incoming connection, the function parameter indicates how many connections can be queued
servsockt.listen(5)
```
When sockets are created, communication can take place by invoking ```send()``` and ```recv()``` methods. General scheme of the communication looks like this:


```python
         *client*                       *server*
       
                                         socket
                                           |    
                                          bind
                                           |
                                         listen
                                           |
          socket                         accept
            |                              | 
         connect - - - - - - - - - - - - ->|
            |                              |
        -->send - - - - - - - - - - - - ->recv<--
       |    |                              |     |
        --recv<- - - - - - - - - - - - -  send --
            |                              |
          close - - - - - - - - - - - - ->recv
                                           |
                                          close
```

We need to send byte streams, but we have (after lab #04) few objects that are instances of ```Card```, ```Deck``` and ```Player```. Fortunately, we have the serialization technique, moreover, it's provided by Python Standard Library. According to Wikipidia, serialization is a process of translating data structures or object state into a format that can be stored (for example, in a file or memory buffer) or transmitted (for example, across a network connection link) and reconstructed later. Python has handy module for that called [pickle](https://docs.python.org/3/library/pickle.html). That is everything we need to know for now, let's move on to the exercises.


### Exercises:

### 05.1: Server

Use following piece of code to create a server script (save it as ```server.py``` file). Fill the blanks.

```python
import socket
from poker import *
import pickle

### TODO: create a socket, bind and listen. Use 'localhost' as address

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    if buf == b'play': # 'magic' word, if client 'says' it, deal the cards
        
        # TODO: create deck 
        # TODO: shuffle deck
        
        [SC,CC] = deck.deal(2) # SC - server's cards, send CC to client
        data_for_client = pickle.dumps(CC, -1) # serialization
        
        # TODO: use connection to send data_for_client
        
        print(SC) # print server's cards

```

### 05.2 Client

Use following piece of code to create a client script (save it as ```client.py``` file). Fill the blanks.

```python
import socket
import pickle
from poker import *

# TODO: create client socket. Name the variable: csocket

# TODO: Connect. Use 'localhost' as address and the same port that server uses.

csocket.send(bytes('play', 'UTF-8')) # send the 'magic' word to get the cards
buf = csocket.recv(4096)

CC = # TODO: unserialize 'buf' contents here

print(CC)
```

### 05.3 Testing

Test your scripts. Remember that server should be run first, to succeed with the connection. 


