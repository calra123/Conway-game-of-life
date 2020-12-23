# Conway-game-of-life
### Introduction
Game of Life was devloped by mathematician John Conway. It is a zero player game which simulates life. Populations expand, contract, form clusters and follow periodicity in erratic manner, all in all its beautiful.

The game has been made in Python using Pygame, it is just a bunch of functions clubbed together to make it run.
### Ambitions
I originally wanted to do it the Object Oriented way, but in the end I just couldn't figure it out.
I also wanted to make it multiplayer and real-time, but when I searched online, I was disheartened as someone had already done it, I still think it would be a good project for OOPS, sockets programming and lot of other interesting concepts.

# Steps for Windows
1) Open cmd or powershell
2) Enter `pip install pygame` and run this command. Further instructions
https://www.pygame.org/wiki/GettingStarted#Windows%20installation
3) Type `pip install pygame-menu` and hit Enter.
4) Run `python trial_game3.py` on the cmd.

# How to Play the Game
1) Add consecutives/adjacent cubes anywhere.
2) Press Spacebar for the next generation. (again and again)

Caution: For starters, play in the middle. Try glider or a vertical of 3 cubes. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

Note: Press Spacebar for next generation.
# Known Issues
1) The board is finite here, when the blocks reach towards the edges they don't follow the conway rules.
2) The Play button doesn't resumes the game anymore, its similar to Reset button.
3) To reset the game, hit Spacebar, after clicking Reset. (as told in the Instructions)
