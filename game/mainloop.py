



"""
    The games mainloop.
    
    - It begins after the game has been initialized.
    - The loops execution is blocked until every player has made his turn
    - The changes eaxh player has made in his turn are applied to the current game status
    - Special events are launched, depending on the current situtiation
    - The next loops starts

    - The loop exits when a player has won the game or the when ended by the admin 
"""


def mainloop():

    while 1:
        
        #   Wait for players
        break