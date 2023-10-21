import random

def choose_word():
    word_list = ["python", "javascript", "java", "programming", "computer", "algorithm", "hangman"]
    return random.choice(word_list)

def hangman():
    word_to_guess = choose_word()
    word_length = len(word_to_guess)
    guessed_letters = []
    attempts = 6  # Number of attempts allowed
    incorrect_guesses = 0

    print("Welcome to Hangman!")
    
    while True:
        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"
        
        print(f"Word to guess: {display_word}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
        
        if display_word == word_to_guess:
            print(f"Congratulations! You've guessed the word: {word_to_guess}")
            break
        
        if attempts == 0:
            print("You've run out of attempts. The word was:", word_to_guess)
            break
        
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word_to_guess:
            print("Good guess!")
            guessed_letters.append(guess)
        else:
            print("Incorrect guess.")
            guessed_letters.append(guess)
            incorrect_guesses += 1
            attempts -= 1
            draw_hangman(incorrect_guesses)

def draw_hangman(incorrect_guesses):
    hangman_pics = [
        """
        +---+
        |   |
            |
            |
            |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
            |
            |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
        |   |
            |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
       /|   |
            |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
            |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       /    |
            |
        =======
        """,
        """
        +---+
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        =======
        """
    ]
    print(hangman_pics[incorrect_guesses])

if __name__ == "__main__":
    hangman()
