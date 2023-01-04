![logo_transparent_background](https://user-images.githubusercontent.com/58174581/168226295-816431ce-7ce7-4fe3-ab78-40ba228242bd.png)

This was a group project conducted as part of Code First Girls Nanodegree spring 2022

# **Project Description**
A simple 2D snake game which will log player scores and generate a leader board.

We have developed a two-dimensional snake game that will bring the nostalgia of the popular 1970s versions into the present day. The snake game is engaging and requires strategic thinking and patience to play. With our users in mind, we will create our game in such a way that players with varying degrees of gaming expertise, those short on time, or those looking to pick up a new interest, may play at any time. Our game will track user scores and build a leader board, fostering casual competitiveness and pushing players. The leader board and other game data such as a player's high score and game history, is all available via our 'Snake Data Service' API.

# **Technologies used**
🔹 Python 3 
🔹 MySQL 
🔹 HTML 
🔹 CSS 

# **Future feature development**
🔹 User to play a 3D game <br />
🔹 User to play against others in mulit-player mode <br />
🔹 User to play the game on an app <br />
🔹 User to play different levels and rooms <br />
🔹 User to choose the design the snake <br />

# **Demo**
https://user-images.githubusercontent.com/58174581/168898981-23166d9f-acbc-40eb-bbe4-9bfde674e1b2.mp4










# **Table of contents**
1. [How to get started?](#howtogetstarted)
    1. [Clone the repo](#clonetherepo)
    2. [Prerequisites](#prerequisites)
    3. [Configuration of database & running API](#config)
    4. [Run the code](#runthecode)
    5. [Start playing](#Startplaying)
    6. [How to access game data](#viewdata)
2. [How to use the project](#howtousetheproject)
3. [Authors](#authors)
4. [Code contributers](#acodecontributers)
     
        
         

# **How to get started?**

## i. Clone the repo <br />
Use this [link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for steps on cloning a repo.

## ii. Prerequisites
   Using the command <br />
   
    $ pip install
    
   Import the following libraries in the terminal: <br />
    
   python 3 <br />
   pygame <br />
   flask <br />
   requests <br />
   
   Execute the Snake_DB.sql script in MySQL Workbench to set up the 'snake' database.

## iii. Configuration of database and running API
Edit the config.py file by replacing "password" with your own MySQL password. <br />
Execute the API code by running app.py (this must be run before running main.py). <br />

## iv. Run code 
   In the snake-game directory, run the command below: 
   
   ```
   $ python main.py 
   ```
   
## v. Start playing 

# **How to play the game?**
🔹 Move the snake using the keyboard arrow keys to collect as many “good” food as possible to increase the length of the snake.  <br />
🔹 The snake will continue to move in one direction if not guided to the required place on the board.  The longer the snake’s tail grows, the higher your score. <br />
🔹 If the snake catches its tail or the wall, it is game over <br />

# **How to access game data?**
🔹 The url for the Snake Data Service is http://127.0.0.1:5001 <br />
🔹 To view the leader board go to: http://127.0.0.1:5001/leaderboard <br />
🔹 To view a player's highest score go to http://127.0.0.1:5001/top_score/<player name\>   <br />
🔹 To view a player's game history go to http://127.0.0.1:5001/history/<player name\>   <br />



# **How to use the project?**
The code could be used simply to play the game, or as a base to develop apps, websites, or run it on the cloud. <br />
The code outlines a basic 2D game, it can be built ppon for a more complex game with additional features. <br />


# **Authors:**
[Esther Arumainayagam](https://github.com/esther-ar) <br />
[Jenna Scotcher](https://github.com/Scotchbum) <br />
[Jessie Kinganga](https://github.com/KingJessie) <br />
[Irina Shestova](https://github.com/Rujik2) <br />
[Serena-Louise Nowbath-Nelson](https://github.com/Renalouise) 

# License and copyright 
© CFG Snakee

