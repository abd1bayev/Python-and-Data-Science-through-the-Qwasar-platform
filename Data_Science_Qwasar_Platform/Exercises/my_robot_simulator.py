

def my_robot_simulator(instructions):
    x, y = 0, 0
    direction = 'north'

    for instruction in instructions:
        if instruction == 'R':
            if direction == 'north':
                direction = 'east'
            elif direction == 'east':
                direction = 'south'
            elif direction == 'south':
                direction = 'west'
            elif direction == 'west':
                direction = 'north'
        elif instruction == 'L':
            if direction == 'north':
                direction = 'west'
            elif direction == 'west':
                direction = 'south'
            elif direction == 'south':
                direction = 'east'
            elif direction == 'east':
                direction = 'north'
        elif instruction == 'A':
            if direction == 'north':
                y += 1
            elif direction == 'west':
                x -= 1
            elif direction == 'south':
                y -= 1
            elif direction == 'east':
                x += 1

    return "{{x: {}, y: {}, bearing: '{}'}}".format(x, -y, direction)
