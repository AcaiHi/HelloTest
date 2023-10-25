# Chapter.5
# 01. Kilometer Converter

km = float(input('Enter a distance in kilometers: '))
def convert(km):
    miles = km * 0.6214
    print(format(miles, '.2f'), 'miles')
    
convert(km)

# Chapter.5
# 03. How Much Insureance?

cost = float(input('Enter the replacement cost of a building: $'))
def calculate(cost):
    insurance = cost * 0.8
    print('The minimum amount of insurance you should buy for the property is $', format(insurance, '.2f'))

calculate(cost)

# Chapter.5
# 06. Calories from Fat and Carbohydrates

fat_grams = float(input('Enter the number of fat grams: '))
carb_grams = float(input('Enter the number of carbohydrate grams: '))

def calculate(fat_grams, carb_grams):
    print('The calories from fat is', format(fat_grams * 9, '.2f'), 'calories')
    print('The calories from carbohydrate is', format(carb_grams * 4, '.2f'), 'calories')

calculate(fat_grams, carb_grams)