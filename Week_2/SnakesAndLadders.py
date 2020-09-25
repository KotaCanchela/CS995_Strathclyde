import random


def rollDie():
    """
    Function to simulate a die roll
    """
    return random.randint(1, 6)


def playSnakesAndLadders(actions):
    """
    Returns the number of dice rolls to win a game of Snakes and Ladders
    """
    playerPos = 0
    numberOfRolls = 0

    while True:
        # Roll the die
        playerPos += rollDie()
        numberOfRolls += 1

        # The game is complete
        if playerPos >= 100:
            break

        # Check if player has landed on an action square
        if playerPos in actions.keys():
            playerPos = actions[playerPos]

    return numberOfRolls


if __name__ == "__main__":
    actions = {
        4: 14,
        9: 31,
        17: 7,
        20: 38,
        28: 84,
        40: 59,
        51: 67,
        54: 34,
        62: 19,
        64: 60,
        71: 91,
        87: 24,
        93: 73,
        95: 75,
        99: 78,
    }
    numberOfGames = 1000
    averageRolls = 0
    for i in range(numberOfGames):
        numberOfRolls = playSnakesAndLadders(actions)
        averageRolls += float(numberOfRolls) / numberOfGames

    print(f"Average number of rolls in {numberOfGames} games: {str(averageRolls)}")
