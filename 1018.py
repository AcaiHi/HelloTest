# Chapter.4
# 05. Average Rainfall

years = int(input('Please enter the number of years: '))
month_rainfall = 0
for i in range(1,  years + 1):
    for m in range(1, 5):
        rainfall_inch = float(input('Enter the inches of rainfall for this season: '))
        month_rainfall += rainfall_inch
months = years * 4
print('The number of months is', months, '\nThe total inches of rainfall is',
      month_rainfall, '\nThe average rainfall per month for the entire period is',
      format(month_rainfall / months, '.2f'))

# Chapter.4
# 12. Population

starting_number = int(input('Enter the starting number of organisms: '))
daily_increase = int(input('Enter the average daily population increase (as a percentage): '))
days = int(input('Enter the number of days to multiply: '))

print('Day Approximate\t', 'Population')
for i in range(1, days + 1):
    print(i, '\t', starting_number)
    starting_number += starting_number * daily_increase / 100

# Chapter.4
# 13. Write a program that uses nested loops to draw this pattern

base_size = 8
for r in range(base_size, 1, -1):
    for c in range(r - 1):
        print('*', end='')
    print()
'''
for i in range(7, 0, -1):
    print('*' * i)
'''

# Chapter.4
# 14. Write a program that uses nested loops to draw this pattern

steps = 6
for r in range(steps):
    print('#', end='')
    for c in range(r):
        print(' ', end='')
    print('#')
    
