# Battleship game
![Screenshot 2024-01-19 205615](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/a906c11f-eeaf-4d1f-b72d-6e27cd498a4b)


The game Battleship is a Python terminal game that revolves around two players trying to strategically guess and locate the positions of the opponent's ships while keeping the positions of ones own ships hidden. The game is typically played on a grid-based board in which each battleship occupies one cell on the grid. First player to sink all of the opponent's ships is declared winner of the game round. 

## Why playing the game 
 **Skill Development:**
-  It's a great way to practice strategic thinking and decision-making skills. Players need to guess the locations of ships, which requires logical reasoning and sometimes even pattern recognition.

**Learning Experience:** 
-  For those interested in programming, playing a game developed in Python can be inspiring. It demonstrates how coding skills can be used to create enjoyable, interactive experiences.

**Nostalgia and Fun:** 
-  Battleship has been a popular board game for generations. Playing a digital version can be a nostalgic experience for many, bringing back memories of playing the physical game.

**Convenience:** 
-  Unlike the traditional board game, this digital version doesn't require physical set-up or another person present to play. It's easily accessible and can be played anytime on a computer.

**Educational Tool:**  
-  For educators or parents, this game can be used as a fun way to introduce children to basic programming concepts and logic.

## How to play

**Gameplay:**

-  The game will prompt you to enter coordinates for your guesses. This typically involves specifying a row *(1-8)* and a column *(A-H)*.
-  Enter the coordinates where you think the computer's ships are located. For example, you might enter 1 for the row and A for the column.
-  The terminal will update you on whether your guess was a hit or a miss and display the game boards showing your guesses and the computer's guesses.
-  The game will also handle the computer's turn, making guesses against your ships.

## Features

-  **Grid-Based Gameplay:** The game is played on two 8x8 grids - one for the player and one for the computer. Each grid represents the ocean where ships are hidden.
-  **Ship Placement:** At the start of the game, ships are randomly placed on both the player's and computer's grids. The placement is hidden from the opponent.
-  **Turn-Based Guessing:** Players take turns guessing the location of the opponent's ships by specifying a row and a column (e.g., 1A, 3D).
-  **Hit and Miss Feedback:** After each guess, the game provides immediate feedback. A "hit" indicates a ship is located at the guessed spot, and a "miss" indicates an empty ocean square.
-  **Tracking Shots:** The game keeps track of each player's guesses, marking hits and misses on the grid so players can see their shot history and strategy.
-  ***Winning Condition:*** The objective is to sink all of the opponent's ships. The game ends when either the player or the computer sinks all of the other's ships.
-  **Randomized AI Behavior:** The computer's guesses are randomized, providing an unpredictable opponent.


![snip2](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/6be9427b-3c0c-4342-9650-72d4570dcb45)




-  Input validation and error checking: 
-  Only coordinates corresponding to cells within the range of (1-8 and A-H) result in a succesful guess.
-  Each guess is only concidered valid once.


## Error Testing

| Verified |  Tested Variables | Description of output |
| ----------- | ----------- |----------- |
| - [x] | Header | Title |
| - [x] | Paragraph | Text |
| - [x] | Paragraph | Text |
| - [x] | Paragraph | Text |
| - [x] | Paragraph | Text |


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
