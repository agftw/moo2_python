"""
The game server.

It serves as a lobby for game clients.
Newly connected clients can:
    - create a game
    - join a game that has not yet started
    
    
Version 0.01
- For now simple text messages are being used to communicate between client and server
"""


import socket


class localClient():
   
    def __init__(self):
        self.__id   = 0; 



class GameServer():


    def __init__(self):
        self.__clients = [];



    def acceptClient(self):
        pass



if __name__ == "__main__":
    pass   