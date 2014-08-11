Code Golf Challenges
====================

My attempts to implement simple algorithms in Python with as few statements as possible.

# Conway's Game of Life #

See [Wikipedia](http://en.wikipedia.org/wiki/Conway's_Game_of_Life) for the rules. To try it:

    python life.py

To stop it press Ctrl+C. To change the size of the board, modify the value of the boardSize variable. To change the initial board configuration, replace `[[random.random() < 0.5 for i in range(boardSize[0])] for j in range(boardSize[1])]` with your desired board.
