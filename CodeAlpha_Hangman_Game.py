import random

# List of predefined words
words = ["hyderabad", "python", "hangman", "mountains", "peach"]

# Randomly select a word
word_to_guess = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(word_to_guess))

# Game loop
while attempts_left > 0:
    guess = input("\nEnter a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You've already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Correct guess
    if guess in word_to_guess:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        attempts_left -= 1

    # Display current progress
    display_word=""
    for letter in guessed_letters:
        if letter in guessed_letters:
            display_word +=letter +" "
        else:
            display +="_ "
    print("Word: " + " ".join(display_word))
    print("Attempts left:", attempts_left)

    # Check if word is completely guessed
    if "_" not in display_word:
        print("You guessed the word:", word_to_guess)
        break

# If attempts run out
if attempts_left == 0:
    print("\n Game Over! The word was:", word_to_guess)
