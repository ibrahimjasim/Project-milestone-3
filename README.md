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
-  

![Screenshot 2024-01-20 114455](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/4d9ac5eb-7a04-40b4-9cc7-8d1f1cbf6a93)


## Features

-  **Grid-Based Gameplay:** The game is played on two 8x8 grids - one for the player and one for the computer. Each grid represents the ocean where ships are hidden.
-  **Ship Placement:** At the start of the game, ships are randomly placed on both the player's and computer's grids. The placement is hidden from the opponent.
-  **Turn-Based Guessing:** Players take turns guessing the location of the opponent's ships by specifying a row and a column (e.g., 1A, 3D).
-  **Hit and Miss Feedback:** After each guess, the game provides immediate feedback. A "hit" indicates a ship is located at the guessed spot, and a "miss" indicates an empty ocean square.
-  **Tracking Shots:** The game keeps track of each player's guesses, marking hits and misses on the grid so players can see their shot history and strategy.
-  ***Winning Condition:*** The objective is to sink all of the opponent's ships. The game ends when either the player or the computer sinks all of the other's ships.
-  **Randomized AI Behavior:** The computer's guesses are randomized, providing an unpredictable opponent.


![Screenshot 2024-01-20 110858](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/7c601e85-4802-44a9-a9cd-2f765ab415b7)


## Wireframe 
![Blank diagram](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/2b597f57-ba47-4ba7-936d-f9276c38dfb7)



## Error Testing

| Verified |  Tested Variables | Description of output |
| ----------- | ----------- |----------- |
| - [x] | Input random charachters/ space **once** instetad of accepted input data | Program replies with consistent *"Please enter a valid row"* |
| - [x] | Input random charachters/ space **twice** instetad of accepted input data | Program reples with consistent *"Please enter a valid row"* |
| - [x] | Input random charachters/ space **multiple times** instetad of accepted input data | Program replies with consistent *"Please enter a valid row"* |
| - [x] | Correct cell is selected | Selecting **8-C** results in the selected cell to be hit. |
| - [x] | Guessing same target twice | Selecting **8-C**  twice results in reply: *"You already guessed that"* |
| - [x] | Guessing outside grid | Selecting **9-M** results in reply: *"Please enter a valid row"* |
| - [x] | Computer waits for its turn | After finishing the 10 rounds as a player, the compiter had played 9 rounds. Game tied. |



## Validator testing
- No errors detected from PEP8online.com
![CI Python Linter - Google Chrome 2024-01-19 20_27_54](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/ad7809b2-9943-45c9-a4d9-c87c6a11025c)


## Perfomance Testing

![Screenshot 2024-01-19 205445](https://github.com/ibrahimjasim/Project-milestone-3/assets/127301769/726a7962-f85e-4277-b3d8-4747b6f330de)


## Deployment steps 
* Pushed the final project to GitHub
* Created a new Heroku app
* Set the buildpacks to `Python` and `NodeJS` in that order 
* Connect GitHub as my Deployment method
* Then scroll down to Manual deploy then pressed the Deploy Bransh button 


## Bugs
* hitting enter for the first two inputs causes it to break - entering in two letters also causes it to crash - same with entering in two numbers - entering in a lower case is not acepted a second time round if the first column entry was     invalid
* game increments one of my turns when the computer plays

## Remaining Bugs
* No bugs remaining



## Credits
- CI material for the given project.
- Wikipedia for rules and logic behind the game.
- Used "copyassignment" as inspiration for functctions.
- 
