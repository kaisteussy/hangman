import random

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

word = random.choice(words)
count = 0
HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']

# Create the blanks to fill in with guesses
letters = ['_' for letter in range(len(word))]
game_is_done = False


def display_status(current_count, letters_status):
    print(HANGMAN_PICS[current_count])
    print()
    print(''.join(letters_status))


def play_again():
    answer = input('Would you like to play again? y/n: ')
    return answer.lower().startswith('y')


print('Welcome to hangman. Please have your wits about you, as this is a game of life and death.')
print('Let us begin.\n')

while True:
    display_status(count, ''.join(letters))
    guess = input('Enter your guess: ')
    while len(guess) > 1:
        print('Please enter only 1 character. No cheating.')
        guess = input('Enter your guess: ')
    print()
    if guess in word:
        print("Your life continues...")
        letters[word.find(guess)] = guess
    else:
        print('Your life shortens...')
        count += 1
        if count == 6:
            print('You\'re dead. Game over.')
            game_is_done = True

    if ''.join(letters) == word:
        print('Congratulations, you cheated death.')
        game_is_done = True

    # Check if game is done
    if game_is_done:
        # Prompt user to play again
        if play_again():
            # Get new word and reset gameplay variables
            word = random.choice(words)
            letters = ['_' for letter in range(len(word))]
            count = 0
            game_is_done = False
        else:
            break
