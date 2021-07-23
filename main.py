#Chatbot by Camellia
import random

def introduce(): # Introduces the chatbot
    print('\nI am a chatbot. Ask me whatever you want! Type \'exit\' to exit.\nSay \'knock knock\' if you want to tell a knock knock joke to me.\n(If you want me to do something, check out the \'Menu\'!)')


def poem(): # Prints a poem
    print('\nOutside, there is an approaching storm\nA storm so large that\nIt’s different from the norm\n\nThe people are the least informed\nOf the tornado that is approaching\nOutside, there is an approaching storm\n\nNobody will escape the swarm\nOf locusts to come\nIt’s different from the norm.\n\nThe houses shall be adorned\nWith ashes raining from the sky\nOutside, there is an approaching storm.\n\nPieces of cloth that are torn\nFloat about in the wind\nIt’s different from the norm.\n\nMuch of our world will be waterborne\nAnd all life forms will be gone\nOutside, there is an approaching storm\nIt’s different from the norm.\n')


def play_rps(): # Plays Rock Paper Scissors
    player = input('\n>>> Rock, Paper, Scissors? ').lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    if player == computer:
        print('Tie!')
    elif player == 'rock':
        if computer == 'paper':
            print('>>> You lose!', computer, 'covers', player)
        else:
            print('>>> You win!', player, 'smashes', computer)
    elif player == 'paper':
        if computer == 'scissors':
            print('>>> You lose!', computer, 'cut', player)
        else:
            print('>>> You win!', player, 'covers', computer)
    elif player == 'scissors':
        if computer == 'rock':
            print('>>> You lose...', computer, 'smashes', player)
        else:
            print('>>> You win!', player, 'cut', computer)
    else:
        print('>>> That\'s not a valid play.')

def ascii_art(): # Prints Ascii art
    print("  __   ____   ___  __  __  \n / _\ / ___) / __)(  )(  ) \n/    \\___ \ ( (__  )(  )(  \n\_/\_/(____/ \___)(__)(__) ")
    

def hangman(): # Plays a round of hangman
    # Randomly generate a word
    words_list = ['SIGNIFICANT', 'ONOMATOPOEIA', 'PROGRAMMING', 'PARAPHERNALIA', 'AMATEUR', 'COMPUTER', 'ROBOTS', 'PYTHON', 'CODING', 'ARDUINO', 'PSEUDOCODE', 'CONDITIONALS']
    # Word that will be printed at the end
    display_word = random.choice(words_list)
    # Separates word into a list so that the elements can be changed later
    word = list(display_word)


    # List of underscores that is the length of the word
    underscores = []
    for letter in word:
        underscores.append('_')

    print('\nWelcome to the Guessing Game! A word will be generated, and you will need to guess the word based on the number of underscores displayed.')

    lives = 6
    guessed_letters = []
    guess = ''
    while lives > 0:
        # Display the lives
        print('\nLives: %d' % lives)

        # Display _ underscores depending on how long the word is
        print('Word: ', end = '')
        for char in underscores:
            print(char, end = ' ')
        print('')

        # Display letters that have been guessed
        guessed_letters.append(guess)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Guessed letters: ', end = '')

        for char in guessed_letters:
            print(char, end = ' ')

        print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

        # Checks to see if the word has been guessed fully (win condition)
        if '_' not in underscores:
            break

        # Allow user to enter a letter
        guess = input('\nGuess a letter: ').upper()

        # Replace the underscores with correct letters
        if guess in word:
            print('___________________________________________________________________________________')
            for letter in word:
                if guess == letter:
                    underscores[word.index(guess)] = guess
                    # Allows for the next index of the guess can be reached
                    word[word.index(letter)] = '*'


        elif guess not in word:
            print('___________________________________________________________________________________')
            print('Try again.')
            # Decrease amount of lives if wrong guess
            lives -= 1

    # Displays if all lives have been lost.
    if lives == 0:
        print('\nYou lose! The word was %s.' % display_word)

    else:
        print('\nYou win! The word was %s.' % display_word)


def show_menu(): # Allows user to interact with the menu
    test = False
    while test != True:
        print('To access any of the following, type the name with the correct spelling:')
        print('>> Poem')
        print('>> RockPaperScissors')
        print('>> ASCII Art')
        print('>> Hangman')
        print('>> Go Back')

        answer = input('What would you like to do? ')
        if answer.lower() == 'poem':
            poem()
        elif answer.lower() == 'rockpaperscissors':
            play_rps()
        elif answer.lower() == 'ascii art':
            ascii_art()
        elif answer.lower() == 'hangman':
            hangman()
        elif answer.lower() == 'go back':
            print('', end = '')
        else:
            print()
            continue
        test = True


def knock_knock():
    answer = input('Who\'s there?\n> ')
    answer = input('%s who?\n> ' % answer)
    print('Haha!!')

def process_input(input): # Processes any input from the user
    input_possibilities = [
    ['hi', 'hello', 'hola'],
    ['sad', 'dead', 'tired', 'dying', 'unhappy', 'scared'],
    ['no', 'stupid', 'dumb', 'dummy'],
    ['bye', 'goodbye', 'so long', 'bye bye'],
    ['']
    ]

    output_possibilites = [
    ['Hi! How are you?', 'Welcome! What would you like to ask?', 'Hi.', 'Hello.', 'How are you doing?', 'Hello. Welcome to the game.', 'Hey.'],
    ['Sorry to hear that :(', 'Hope that you\'ll feel better soon!', 'Are you ok?'],
    ['Alright then. Hope you come back later I guess?', 'Be nicer :(', 'You\'re not very nice.', 'No, you.', 'Go away.'],
    ['Bye! Have a nice day.', 'Goodbye.', 'Bye.', 'Have a great day!', 'Have fun.'],
    ['That\'s cool!', 'Nice!', 'That\'s really cool!', 'Woah!', 'Wow!']
    ]

    if input.lower() == 'menu':
        print()
        show_menu()
    elif input.lower() == 'knock knock':
        knock_knock()
        print()
    else:
        for i in range(len(input_possibilities)):
            for elem in input_possibilities[i]:
                if elem in input.lower():
                    print(random.choice(output_possibilites[i]))
                    return ''


def main():
    print("Created by Camellia @ GWC Summer Immersion Program")
    introduce()
    while True:
        answer = input('> ')
        if answer == 'exit':
            exit(0)
        else:
            process_input(answer)
        print()


if __name__ == '__main__':
    main()
