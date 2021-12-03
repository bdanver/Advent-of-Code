import sys
horizontal = 0
depth = 0 
with open('input.txt') as f:
    for line in f:
        command = line.split()
        direction = command[0]
        x_units = int(command[1])
        if(direction.startswith('f')):
            horizontal += x_units
        elif(direction.startswith('d')):
            depth += x_units
        else:
            depth -= x_units
   
f.close()
print('h',horizontal)
print('d',depth)
print('total',horizontal*depth)