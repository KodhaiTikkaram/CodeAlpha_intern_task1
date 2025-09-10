import random

# Predefined list of words
words = ["python", "coding", "school", "hangman", "simple"]

# Randomly choose a word
word = random.choice(words)
word_letters = list(word)  # letters in the word
guessed = ["_"] * len(word)  # display blanks
attempts = 6  # maximum wrong guesses
used_letters = []  # track guessed letters

print("🎮 Welcome to Hangman Game!")
print("You have 6 chances to guess the word.")
print(" ".join(guessed))

# Game loop
while attempts > 0 and "_" in guessed:
    guess = input("\nGuess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter a single valid letter.")
        continue

    if guess in used_letters:
        print("⚠️ You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word_letters:
        print("✅ Good guess!")
        for i, letter in enumerate(word_letters):
            if letter == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! {attempts} attempts left.")

    print("Word: ", " ".join(guessed))
    print("Used letters:", ", ".join(used_letters))

# Result
if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
