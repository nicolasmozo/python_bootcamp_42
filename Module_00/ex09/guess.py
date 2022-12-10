from random import randint

number = randint(1, 99)

print('This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType \'exit\' to end the game.\nGood luck!')

counter = 0
while True:
    guess = input('What\'s your guess between 1 and 99?\n')
    if guess == 'exit':
        print('Goodbye!')
        break
    if not guess.isnumeric():
        print('That\'s not a number.')
        continue
    guess = int(guess)
    if guess < number:
        print('Too low!')
    elif guess > number:
        print('Too high')
    else:
        counter += 1
        if number == 42:
            print(
                'The answer to the ultimate question of life, the universe and everything is 42.')
        if counter == 1:
            print("Congratulations! You got it on your first try!")
            break
        print(
            f'Congratulations, you\'ve got it!\nYou won in {counter} attemps!')
        break
    counter += 1