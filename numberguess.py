import random

def score(attempts_list):
    if not attempts_list:
        print("Haven,t Yet attempted")
    else:
        print(f'The current score is {min(attempts_list)}')

def start_game():
    attempts = 0
    rand_num = random.randint(1,100)
    attempts_list = []

    print('Hi There, Welcome to Guesses!')
    name = input('whats your name?')
    play = input(f'Hi, {name} wanna play Guesses? (Enter Yes/No):')
    if play.lower() != 'yes':
        print('coool, Thanks!')
        exit()
    else:
        score(attempts_list)

    while play.lower() == 'yes':
        try:
            guess = int(input('pick number between 1 and 100: '))
            if guess < 1 or guess > 100:
                raise ValueError('please guess a valid number')
            attempts += 1
            if guess == rand_num:
                attempts_list.append(attempts)
                print('Nice! u got it')
                print(f'it took u {attempts}')
                play = input('wanna play again? (Enter Yes/No): ')
                if play.lower() != 'yes':
                    print('Cooool, have a good one!')
                    break
                else:
                    attempts = 0
                    rand_num = random.randint(1,100)
                    score(attempts_list)
            else:
                if guess > rand_num:
                    print('Go Lower')
                elif guess < rand_num:
                    print('Go Higher')
        except ValueError as err:
            print('ohhhhhh! that is not a valid number. Try Again...')
            print(err)

if __name__ == '__main__':
    start_game()