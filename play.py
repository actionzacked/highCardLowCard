import os
import time
import random

def play_round(playerName):
    # Init
    letsPlay = True
    winningScore = 5
    currentRound = 1
    computerScore = 0
    playerScore = 0

    # Play Game
    while letsPlay:
        # Clear Screen
        os.system('clear')

        # Scoreboard
        print("=== SCORE BOARD ===")
        print(f"Round: {str(currentRound)}")
        print(f"{playerName}: {str(playerScore)}")
        print(f"Computer: {str(computerScore)}")
        print("===================")

        # Card Deck
        cardDeck = [1,2,3,4,5,6,7,8,9]

        # Draw a card from the deck and present it to the player
        print("\nPicking a card from the deck...")
        time.sleep(random.choice(range(1,5)))

        firstCard = random.choice(range(2,9))
        print(f"I picked the {firstCard} card!")

        # Remove the chosen card from the cardDeck
        cardDeck.remove(firstCard)

        # Ask the player if the next card is going to be higher or lower than the first card
        print("")
        print(f"Deck: {cardDeck}")
        playerChoice = input(f"Will the next card be higher (H) or lower (L) than {firstCard}? ").lower().strip()
        time.sleep(random.choice(range(1,3)))
        if playerChoice == "l":
            playerChoice = 0 
        if playerChoice == "h":
            playerChoice = 1

        # Pick the next card, but it cannot match the firstCard
        print("Drawing the next card...")
        time.sleep(random.choice(range(1,3)))

        secondCard = random.choice(cardDeck)

        # Is it higher or lower?
        if firstCard > secondCard:
            answer = 0
            fullAnswer = "LOWER"
        if secondCard > firstCard:
            answer = 1
            fullAnswer = "HIGHER"

        # Tell the player
        time.sleep(random.choice(range(1,3)))
        print(f"\nThe card is {secondCard}! Which is {fullAnswer}!")

        # Determine winner
        if playerChoice == answer:
            print(f"\nYou win! Congratulations, {playerName}!")
            playerScore += 1
        else:
            print(f"\nYou lose. Better luck next time, {playerName}!")
            computerScore += 1

        # Update Game
        currentRound += 1
        if playerScore == winningScore:
            # Display Text
            print(f"You won the GAME!!! Great job, {playerName}!!!")
            letsPlay = False
            nextRound = False
        
        if computerScore == winningScore:
            # Clear Screen
            os.system('clear')

            # Display Text
            print(f"You lost the game :( Go cry about it...")
            letsPlay = False
            nextRound = False
        if nextRound:
            # Display Text
            print("Get ready for the next round!")
            time.sleep(5)

    # Leave Game
    return

def play_game():
    # Clear Screen
    os.system('clear')

    # Init
    playAnotherGame = True

    # Get Player Name
    playerName = input("What is your name? ")
    print(f"\nHello, {playerName}, let's play!\n")

    while playAnotherGame:
        play_round(playerName)
        time.sleep(5)

        # Clear Screen
        os.system('clear')

        # Keep playing?
        keepPlaying = input(f"Would you like to keep playing, {playerName}? [y/n] ").lower().strip()
        if keepPlaying == "y":
            print("Great! Let's play!")
        else:
            print(f"K..fine... Bye.")
            playAnotherGame = False
    
    # Leave Game
    return

if __name__ == "__main__":
    play_game()