Day 11: Simplified Blackjack Game in Python

Welcome to **Day 11** of my **100 Days of Python Challenge**!  
Today, I developed a simplified version of the **Blackjack card game**, implementing basic gameplay mechanics.


## 📝 Project Overview

This Python program allows players to:
1. **Start a game of Blackjack**.
2. **Draw cards (Hit)** or **stop drawing (Stay)**.
3. View their **current hand** and **score** after each action.
4. **Lose** if their score exceeds 21.


## 💻 How It Works

### 1. Game Mechanics

- *Card Deck*: Contains the values '2-10', 'J', 'Q', 'K', and 'A'.
- **Initial Hand**: The player is dealt two random cards at the beginning of the game.
- **Player Actions**:
  - 'Hit (H)': Draw an additional card.
  - 'Stay (S)': Stop drawing cards and finalize the score.
- **Scoring**:
  - Number cards ('2-10') are worth their face value.
  - Face cards ('J', 'Q', 'K') are worth 10 points.
  - Aces ('A') can be worth **11 or 1**, depending on the total score.

### 2. Rules of the Game

1. The player starts by drawing two cards.
2. They can keep drawing cards (HIT) until:
   - They decide to **STAY**.
   - Their score exceeds 21 (**Bust**).
3. The game ends when the player either **Stays** or **Busts**.

---

### 3. Features

- **Dynamic Scoring**:
  - Automatically adjusts for Aces ('A') if the score exceeds 21.
  
- **Interactive Gameplay**:
  - Prompts players to decide their next move (HIT or STAY).

- **Random Card Distribution**:
  - Each card is chosen randomly from the deck using 'random.choice()'.
 
Concepts Applied

Functions:
dealCards(), hitCards(), calculateScore(), and blackjack() ensure modular and reusable code.

Conditionals:
Game logic depends on player actions (HIT or STAY) and score evaluations.

Loops:
The main game loop keeps the program running until the player chooses to quit.

Randomization:
Utilized random.choice() for card selection.

Data Structures:
Lists are used to store the player’s current hand.
