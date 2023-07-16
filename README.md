# Battleship game
![snip 1](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/be0cba73-ad66-4913-a206-2916085620fb)

The game Battleship is a Python terminal game that revolves around two players trying to strategically guess and locate the positions of the opponent's ships while keeping the positions of ones own ships hidden. The game is typically played on a grid-based board in which each battleship occupies one square on the grid. 

## How to play

Each player has their own grid board. The board in this version is an 8x8 grid and each player's ships are positioned in random squares on the grid. The size and number of ships can vary in the traditional game, however, in this project 5 ships were placed on each player's board.
Taking turns, each players attempts to locate and sink their opponent's ships. The player selects a cell on their opponent's board using coordinates (e.g., "B-5" or "F-9"). The selected position is either a hit (marked: X) or a miss (marked:-).

The game continues for 10 rounds with the winner being the player who successfully manages to sink the highest number of ships on the oppnont's board. 


## Features

- Random board generation: 
  -    The ships are randomly placed on the board.
  -    The ships are hidden.
  -    The only option available is playing against the computer.
  -    The inputs are limited to (1-8) and (A-H), with each coordinate representing a cell on the grid.
  -    The previous guesses are visible on a grid.

![snip2](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/6be9427b-3c0c-4342-9650-72d4570dcb45)


-  Input validation and error checking: 
-  Only coordinates corresponding to cells within the range of (1-8 and A-H) result in a succesful guess.
-  Each guess is only concidered valid once.


## Testing

- I have manually tested the project by following these steps:
  -  Code successfully passed through a PEP8 linter.
  -  Deliberatly guessing invalid inputs for:
      - Positions outside the grid.
        
     ![snip4](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/27b5e214-4e92-4494-ab1f-1e88068c42e8)

      - Repeating the same guess.
        
     ![snip3](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/0fe0e8ea-f026-457b-937b-e129d051d915)

-  Used CI's Heroku terminal for testing.
  
  ![snip5](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/a310a1a2-4b65-4f37-9596-6fca1eb1bbd1)



## Bugs
- No known bugs.


# Validator testing
- No errors detected from PEP8online.com


## Credits
- CI material for the given project.
- Wikipedia for rules and logic behind the game.
- Used "copyassignment" as inspiration for functctions.
