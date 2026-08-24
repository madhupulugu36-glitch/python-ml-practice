import random

words = ["python", "java", "computer", "developer", "programming"]

secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

lives = 5

stages = [
      """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,

    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

while "_" in display_word and lives > 0:

    guess = input("Guess a letter:").lower()

    for position in range(len(secret_word)):
        if secret_word[position] == guess:
            display_word[position] = guess

    if guess not in secret_word:
        lives -= 1
        print("worng guess!")
        print("Liver remaining:", lives)
    print(stages[5 - lives])
    print(display_word)

if "_" not in display_word:
    print("Congratulations!:", secret_word)
else:
    print("Game Over!")
    print("The word was:", secret_word) 

