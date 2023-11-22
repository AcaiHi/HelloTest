# Chapter.6
# 03. Line Numbers

def read():
    file = input('Enter a file name with its extension: ')
    object_file = open(file, 'r')
    line = object_file.readline()
    line = line.rstrip('\n')
    line_number = 1
    while line != '':
        print(line_number, ':', line, sep='')
        line = object_file.readline()
        line = line.rstrip('\n')
        line_number += 1
    object_file.close()
read()

# Chapter.6
# 06. Average of Numbers

def read():
    object_file = open('numbers.txt', 'r')
    count = 0
    total = 0
    for i in object_file:
        total += int(i)
        count += 1
    print(total / count)
    object_file.close()
read()

# Chapter.6
# 07. Random Number File Writer

import random

def write():
    object_file = open('random_numbers.txt', 'w')
    how_many = int(input('Enter a number as a integer how many random number'
                          'the file will hold: '))
    for i in range(how_many):
        number = random.randrange(1, 501)
        number = str(number)
        object_file.write(number)
        object_file.write('\n')
    print("---end 07----")
    object_file.close()
write()

# Chapter.6
# 08. Random Number File Reader

def read():
    object_file = open('random_numbers.txt', 'r')
    total = 0
    count = 0
    for i in object_file: 
        i = i.rstrip('\n')
        i = int(i)
        print(i)
        total += i
        count += 1
    print("---08----")
    print(total)
    print(count)
    object_file.close()
read()