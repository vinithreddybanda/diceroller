import random
import time

# ASCII frames for a simple rolling animation
dice_faces = [
    "[     ]",
    "[  o  ]",
    "[ o o ]",
    "[o o o]",
    "[ ooo ]",
    "[ooooo]"
]

def roll_animation():
    print("Rolling the die...", end="\r")
    for i in range(10):
        print(f"{random.choice(dice_faces)}", end="\r")
        time.sleep(0.1)
    print(" " * 20, end="\r")  # Clear the line

def main():
    print("Welcome to the Dice Roller!")
    while True:
        input("Press Enter to roll the die (or Ctrl+C to quit)...")
        roll_animation()
        result = random.randint(1, 6)
        print(f"You rolled a {result}!\n")

if __name__ == "__main__":
    main()
