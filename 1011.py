# Chapter.4
# 04. Distance Traveled

speed = float(input('What is the speed of the vehicle in mph? '))
hour = int(input('How many hours has it traveled? '))
distance = 0
print('Hour\t', 'Distance Traveled')
print('-' * 30)

for i in range(1, hour + 1):
    
    print(format(i, '1.0f'), '\t\t', format(i * speed, '6.1f'))
    distance += i * speed
# Chapter.4
days = int(input('Enter the number of days: '))
print('Day\t\t', 'Salary')
print('-' * 25)
total = 0
for i in range(1, days + 1):
    salary = 0.01 * 2 ** (i -1)
    print(format(i, '3.0f'), '\t\t$', format(salary, '8.2f'))
    total += salary
print('The total pay at the end of the period is $', format(total, '.2f'))

# Chapter.4
# 08. Sum of Numbers

number = float(input('Enter a positive number or enter a negative number '
                     'if you want to end: '))
total = 0
while number > 0:
    total += number
    number = float(input('Enter a positive number: '))
print('The sum is', total)