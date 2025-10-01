"""251001"""


## FT: Simulation
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    emptyBottles = 0  # 空瓶
    numDrink = 0  # 已經喝掉的瓶數

    # 當總瓶數大於能換的數量
    while numBottles + emptyBottles >= numExchange:
        # Drink: 把水瓶喝掉，變成空瓶
        emptyBottles += numBottles
        numDrink += numBottles
        numBottles = 0

        # Exchange: 把所有空瓶換成水瓶
        getBottles = emptyBottles // numExchange
        numBottles += getBottles
        emptyBottles -= getBottles * numExchange

    # Drink: 剩下不夠換的水瓶也要記得喝掉
    emptyBottles += numBottles
    numDrink += numBottles
    numBottles = 0

    return numDrink


# Approach 1: Simulation
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drunk_bottles = 0

    while numBottles >= numExchange:
        # Drunk numExchange full bottles
        drunk_bottles += numExchange
        numBottles -= numExchange

        # Exchange one full bottle
        numBottles += 1

    # Drunk the remaining numBottles (less than numExchange)
    return drunk_bottles + numBottles


# Approach 2: Optimized Simulation
def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    drunk_bottles = 0

    while numBottles >= numExchange:
        # Maximum number of times we can exchange
        max_drunk = numBottles // numExchange

        drunk_bottles += numExchange * max_drunk
        numBottles -= numExchange * max_drunk

        numBottles += max_drunk

    return drunk_bottles + numBottles
