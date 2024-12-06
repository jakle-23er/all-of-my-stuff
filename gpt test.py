#this is chat gpt's take on this I claim no credit it is chat gpt's work
import random
import time
import os

# Function to display the dice faces
def print_dice(face):
    dice_faces = {
        1: '''
  -----
 |     |
 |  *  |
 |     |
  -----
        ''',
        2: '''
  -----
 | *   |
 |     |
 |   * |
  -----
        ''',
        3: '''
  -----
 | *   |
 |  *  |
 |   * |
  -----
        ''',
        4: '''
  -----
 | * * |
 |     |
 | * * |
  -----
        ''',
        5: '''
  -----
 | * * |
 |  *  |
 | * * |
  -----
        ''',
        6: '''
  -----
 | * * |
 | * * |
 | * * |
  -----
        '''
    }
    print(dice_faces[face])

# Function to simulate the rolling animation
def roll_dice():
    for _ in range(10):  # Roll the dice animation for 10 cycles
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for Windows or Unix
        face = random.randint(1, 6)  # Random dice face
        print_dice(face)  # Print the dice face
        time.sleep(0.2)  # Wait for 200ms before showing the next roll

    # Final roll to display the result
    os.system('cls' if os.name == 'nt' else 'clear')
    result = random.randint(1, 6)
    print(f"Final roll: {result}")
    print_dice(result)

# Run the dice rolling animation
if __name__ == "__main__":
    roll_dice()