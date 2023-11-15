# Chapter.5
# 11. Math Quiz

import random

number1 = random.randint(1, 1000)
number2 = random.randint(1, 1000)
total = number1 + number2
print('\t', format(number1, '4.0f'))
print('+\t', format(number2, '4.0f'))

answer = int(input('Enter the answer: '))

def check(answer, total):
    if answer == total:
        print('Congratulation!')
    else:
        print('The answer is', total)

check(answer, total)

# Chapter.5
# 20. Random Number Guessing Game

import random

y = 'y'
while y == 'y' or y == 'Y':
    r = random.randrange(1, 101)
    def guess(r):
        number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
        while r != number:
            if number > r:
                print('Too high')
                number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
            elif number < r:
                print('Too low')
                number = int(input('Enter a integer betweeen 1 to 100 to guess a number: '))
        print('Congratulatioin!!')
    guess(r)
    y = input('Do this again? If yes, enter y or Y. If no, enter other letters')

# Chapter.5
# 21. Rock, Paper, Scissors Game

import random

def set_up():
    n = random.randrange(1, 4)
    com = ''
    if n == 1:
        com = 'rock'
    elif n == 2:
        com = 'scissors'
    else:
        com = 'paper'
    choice = input('Choose and enter one among \'rock\', \'scissors\' or'
                       '\'paper\': ')
    print(com)
    return com, choice
def rule(com, choice):
    while com == choice:
        com, choice = set_up()
    else:
        if com == 'rock' and choice == 'scissors':
            print('Computer wins!')
        elif com == 'scissors' and choice == 'rock':
            print('You wins!')
        elif com == 'paper' and choice == 'scissors':
            print('You wins!')
        elif com == 'scissors' and choice == 'paper':
            print('Computer wins!')
        elif com == 'rock' and choice == 'paper':
            print('You wins!')
        elif com == 'paper' and choice == 'rock':
            print('Computer wins!')
def main():
    com, choice = set_up()
    rule(com, choice)
main()