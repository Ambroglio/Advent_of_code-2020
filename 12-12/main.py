import math

def get_instructions(filename):
    instructions = []

    with open(filename) as f:
        for line in f:
            line = line.replace("\n", "")
            letter = line[0]
            move = (int) (line[1:])
            instructions += [{letter: move}]

    return instructions

def navigate(instructions, v2 = False):
    directions = ["N", "E", "S", "W"]
    direction = "E"
    position = (0, 0)
    if v2:
        waypoint_position = (10, 1)

    for instruction in instructions:
        for letter in instruction:
            move = instruction[letter]
            if (letter == "F"):
                current_move = move_ship(direction, move)
                if not v2:
                    position = (position[0] + current_move[0], position[1] + current_move[1])
                else:
                    position = (position[0] + move * waypoint_position[0], position[1] + move * waypoint_position[1])
            elif (letter in directions):
                current_move = move_ship(letter, move)
                if not v2:
                    position = (position[0] + current_move[0], position[1] + current_move[1])
                else:
                    waypoint_position = (waypoint_position[0] + current_move[0], waypoint_position[1] + current_move[1])
            else:
                if not v2:
                    change_direction = 0
                    if letter == "L":
                        change_direction = directions.index(direction) * 90 - move
                    else:
                        change_direction = directions.index(direction) * 90 + move
                    direction = directions[(int)(change_direction / 90) % 4]
                else:
                    if letter == "L":
                       waypoint_degree = -move
                    else:
                        waypoint_degree = move

                    waypoint_position = (
                        waypoint_position[0] * (int)(math.cos(math.radians(waypoint_degree))) + waypoint_position[1] * (int)(math.sin(math.radians(waypoint_degree))),
                        -waypoint_position[0] * (int)(math.sin(math.radians(waypoint_degree))) + waypoint_position[1] * (int)(math.cos(math.radians(waypoint_degree)))
                    )
    
    return abs(position[0]) + abs(position[1])
             
def move_ship(direction, move):
    if direction == "N":
        return (0, move)
    elif direction == "E":
        return (move, 0)
    elif direction == "S":
        return (0, -move)
    else:
        return (-move, 0)

def main():
    print("---___---")
    instructions = get_instructions("input.txt")
    print("v1")
    value = navigate(instructions)
    print(value)
    print("v2")
    value = navigate(instructions, v2=True)
    print(value)

if __name__ == "__main__":
    main()