# Chapter.7
# 01. Total Sales

def calculate():
    sales = []
    total = 0
    for i in range(7):
        sale = input('Enter a store\'s sales for today: ')
        sales.append(sale)
        total += float(sale)
    print(sales)
    print(total)
calculate()

# Chapter.7
# 02. Lottery Number Generator

import random

def generate():
    lottery_list = []
    for i in range(7):
        lottery_list.append(random.randrange(0 ,10))
    print(lottery_list)
    return lottery_list
def display(lottery_list):
    for i in lottery_list:
        print(i)
lottery_list = generate()
display(lottery_list)

# Chapter.7
# 04. Number Analysis Program

numbers = []
total = 0
for i in range(5):
    number = int(input('Enter a number as a integer: '))
    numbers.append(number)
    total += number
print('The lowest number in the list is', min(numbers))
print('The highest number in the list is', max(numbers))
print('The total in the list is', total)
print('The average in the list is', total / 20)

# Chapter.7
# 06. Larger Than n


def compare(numbers_list, number):
    for i in numbers_list:
        if i > number:
            print(i)

compare(numbers, 3)





    