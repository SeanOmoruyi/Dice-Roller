import random
import time

def dice_roller():
    num_dice = int(input("Enter the number of dice to roll: "))
    results = [random,randint(1,6) for _ in range(num_dice)]
    print("Rolling the dice...")
    time.sleep(1)
    print(f"You rollled: {results}")

if __name__ == "__main__":
    dice_roller()