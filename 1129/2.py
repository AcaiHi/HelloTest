# Chapter.6
# 10. Golf Scores

def init():
    member = int(input('Enter the number of member: '))
    object_file = open('golf.txt', 'w')
    for i in range(member):
        name = input('Enter a player\'s name: ')
        score = input('Enter his or her score: ')
        object_file.write(name + '\n')
        object_file.write(score + '\n')
    object_file.close()
    return object_file
def read():
  object_file = open('golf.txt', 'r')
  for i in object_file:
    i = i.rstrip('\n')
    print(i)

def delete():
  name = input('Enter a player\'s name: ')
  with open('golf.txt', 'r') as file:
    lines = file.readlines()
  with open('golf.txt', 'w') as file:
    i = 0
    while i < len(lines):
      if lines[i].strip() == name:
        i += 2  # Skip the name and score lines
      else:
        file.write(lines[i])
        file.write(lines[i+1])
        i += 2

def search():
  name = input('Enter a player\'s name: ')
  with open('golf.txt', 'r') as file:
    lines = file.readlines()
  found = False
  for i in range(0, len(lines), 2):
    if lines[i].strip() == name:
      print(lines[i].strip())
      print(lines[i+1].strip())
      found = True
      break
  if not found:
    print('Not found')

def modify():
  name = input('Enter a player\'s name: ')
  with open('golf.txt', 'r') as file:
    lines = file.readlines()
  found = False
  for i in range(0, len(lines), 2):
    if lines[i].strip() == name:
      print(lines[i].strip())
      print(lines[i+1].strip())
      found = True
      break
  if not found:
    print('Not found')
  else:
    new_score = input('Enter a new score: ')
    lines[i+1] = new_score + '\n'
    with open('golf.txt', 'w') as file:
      for line in lines:
        file.write(line)

object_file = init()
modify()
search()
delete()
read()