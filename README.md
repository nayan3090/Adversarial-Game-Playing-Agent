
# Build an Adversarial Game Playing Agent

![Example game of isolation on a square board](viz.gif)

## Synopsis

In this project, an agent playing knights Isolation is built using adversarial search techniques. This version of Isolation gives each agent control over a single token that moves in L-shaped movements--like a knight in chess.

### Isolation

In the game Isolation, two players each control their own single token and alternate taking turns moving the token from one cell to another on a rectangular grid.  Whenever a token occupies a cell, that cell becomes blocked for the remainder of the game.  An open cell available for a token to move into is called a "liberty".  The first player with no remaining liberties for their token loses the game, and their opponent is declared the winner.

In knights Isolation, tokens can move to any open cell that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board.  On a blank board, this means that tokens have at most eight liberties surrounding their current location.  Token movement is blocked at the edges of the board (the board does not wrap around the edges), however, tokens can "jump" blocked or occupied spaces (just like a knight in chess).

Finally, agents have a fixed time limit (150 milliseconds by default) to search for the best move and respond.  The search will be automatically cut off after the time limit expires, and the active agent will forfeit the game if it has not chosen a move.

**You can find more information (including implementation details) about the in the Isolation library readme [here](/isolation/README.md).**

## Getting Started (Local Environment)

If you would prefer to complete the exercise in your own local environment, then follow the steps below:

- Open your terminal and activate the aind conda environment (OS X or Unix/Linux users use the command shown; Windows users only run `activate aind`)
```
$ source activate aind
```

- Download a copy of the project files from GitHub and navigate to the project folder. (Note: if you've previously downloaded the repository for another project then you can skip the clone command. However, you should run `git pull` to receive any project updates since you cloned the repository.)
```
(aind) $ git clone https://github.com/nayan3090/Adversarial-Game-Playing-Agent.git
```