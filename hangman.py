import random
import string

# Hangman stages
hangman_stages = [
    """ 
        +---+
        |   |
            |
            |
            |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
            |
            |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
        |   |
            |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
       /|   |
            |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
      =========
    """,
    """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
      =========
    """
]

# Words categorized by difficulty levels
words = {
    'easy': ['cat', 'dog', 'sun', 'fish', 'bird'],
    'medium': ['elephant', 'giraffe', 'turtle', 'rabbit', 'monkey'],
    'hard': ['python', 'javascript', 'hangman', 'computer', 'keyboard']
}

# Function to get a valid guess from the player
def get_guess(used_letters):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess not in string.ascii_lowercase:
            print("Please enter a letter.")
        elif guess in used_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

# Function to play Hangman
def hangman():
    print("Welcome to Hangman!")
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty not in words:
        print("Invalid difficulty level. Defaulting to easy.")
        difficulty = 'easy'
    
    word = random.choice(words[difficulty])
    word_letters = set(word)
    guessed_letters = set()
    incorrect_guesses = 0
    max_attempts = len(hangman_stages) - 1

    print(f"Category: {difficulty.capitalize()}")
    board = ["_"] * len(word)

    while incorrect_guesses < max_attempts:
        print("\n" + hangman_stages[incorrect_guesses])
        print(" ".join(board))
        print(f"Guessed letters: {' '.join(guessed_letters)}")

        guess = get_guess(guessed_letters)

        if guess in word_letters:
            guessed_letters.add(guess)
            for i, letter in enumerate(word):
                if letter == guess:
                    board[i] = guess
            if set(board) == word_letters:
                print(f"Congratulations! You guessed the word '{word}' correctly!")
                break
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1

    else:
        print("\n" + hangman_stages[incorrect_guesses])
        print(f"Sorry, you lost! The word was '{word}'.")

# Run the game
hangman()
