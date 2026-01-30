import random

def display_hangman(tries):
    """Display the hangman based on number of incorrect tries."""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      
           |
           |
           |
           -
        """
    ]
    return stages[tries]

def get_word():
    """Return a random word from the word list."""
    word_list = ['python', 'hangman', 'programming', 'computer', 'keyboard', 
                 'developer', 'algorithm', 'function', 'variable', 'database',
                 'software', 'internet', 'network', 'security', 'application']
    return random.choice(word_list).upper()

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display.strip()

def play_hangman():
    """Main game function."""
    print("=" * 50)
    print("Welcome to HANGMAN!")
    print("=" * 50)
    
    word = get_word()
    guessed_letters = set()
    incorrect_guesses = set()
    tries = 6
    
    while tries > 0:
        print("\n" + display_hangman(tries))
        print("\nWord: " + display_word(word, guessed_letters))
        print(f"Incorrect guesses: {', '.join(sorted(incorrect_guesses)) if incorrect_guesses else 'None'}")
        print(f"Tries remaining: {tries}")
        
        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("\n" + "=" * 50)
            print(f"🎉 Congratulations! You won! The word was: {word}")
            print("=" * 50)
            return
        
        # Get player's guess
        guess = input("\nGuess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single letter.")
            continue
        
        if guess in guessed_letters or guess in incorrect_guesses:
            print("⚠️  You already guessed that letter.")
            continue
        
        # Check if guess is correct
        if guess in word:
            guessed_letters.add(guess)
            print(f"✓ Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses.add(guess)
            tries -= 1
            print(f"✗ Sorry, '{guess}' is not in the word.")
    
    # Player lost
    print("\n" + display_hangman(0))
    print("\n" + "=" * 50)
    print(f"💀 Game Over! The word was: {word}")
    print("=" * 50)

def main():
    """Main program loop."""
    while True:
        play_hangman()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break

if __name__ == "__main__":
    main()