def get_grid(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            new_line = []
            for charac in line:
                if charac == "#":
                    new_line += ["#"]
                elif charac == ".":
                    new_line += ["."]
                elif charac == "L":
                    new_line += ["L"]
            grid += [new_line]
    return grid

def get_number_of_seats(grid):
    grid_to_compare = create_grid_to_compare(grid)
    while (not grids_are_equals(grid, grid_to_compare)):
        grid = grid_to_compare
        grid_to_compare = create_grid_to_compare(grid)

    return count_number_of_seats(grid_to_compare)

def get_number_of_seats_v2(grid):
    grid_to_compare = create_grid_to_compare_v2(grid)
    while (not grids_are_equals(grid, grid_to_compare)):
        grid = grid_to_compare
        grid_to_compare = create_grid_to_compare_v2(grid)

    return count_number_of_seats(grid_to_compare)

def grids_are_equals(grid, grid_to_compare):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != grid_to_compare[i][j]:
                return False 

    return True

def count_number_of_seats(grid):
    total = 0
    for line in grid:
        for charac in line:
            if charac == "#":
                total += 1

    return total

def create_grid_to_compare(grid):
    grid_to_compare = []
    for y in range(len(grid)):
        new_line = []
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                new_line += ["."]
            else:
                adjacent_numbers = 0
                
                #checking adjacent
                if y > 0 and x > 0 and is_occupied_seat(grid[y - 1][x - 1]):
                    adjacent_numbers += 1
                if y > 0 and is_occupied_seat(grid[y - 1][x]):
                    adjacent_numbers += 1
                if y > 0 and x < len(grid[y]) - 1 and is_occupied_seat(grid[y - 1][x + 1]):
                    adjacent_numbers += 1
                if x < len(grid[y]) - 1 and is_occupied_seat(grid[y][x + 1]):
                    adjacent_numbers += 1
                if y < len(grid) - 1 and x < len(grid[y]) - 1 and is_occupied_seat(grid[y + 1][x + 1]):
                    adjacent_numbers += 1
                if y < len(grid) - 1 and is_occupied_seat(grid[y + 1][x]):
                    adjacent_numbers += 1
                if x > 0 and y < len(grid) - 1 and is_occupied_seat(grid[y + 1][x - 1]):
                    adjacent_numbers += 1
                if x > 0 and is_occupied_seat(grid[y][x - 1]):
                    adjacent_numbers += 1

                if is_occupied_seat(grid[y][x]) and adjacent_numbers >= 4:
                    new_line += ["L"]
                elif not is_occupied_seat(grid[y][x]) and adjacent_numbers == 0:
                    new_line += ["#"]
                else:
                    new_line += [grid[y][x]]
        grid_to_compare += [new_line]

    return grid_to_compare

def is_occupied_seat_v2(grid, x, y, x_move, y_move):
    occupied_seat = False
    finished = False

    while (not occupied_seat and not finished):
        try:
            x = x + x_move
            y = y + y_move
            if x < 0 or y < 0 or grid[y][x] == "L":
                finished = True
            if not finished:
                occupied_seat = occupied_seat or grid[y][x] == "#"
        except IndexError:
            finished = True

    return occupied_seat

def print_grid(grid):
    txt = ""
    for line in grid:
        for charac in line:
            txt += charac
        txt += "\n"
    print(txt)

def create_grid_to_compare_v2(grid):
    grid_to_compare = []
    for y in range(len(grid)):
        new_line = []
        for x in range(len(grid[y])):
            if grid[y][x] == ".":
                new_line += ["."]
            else:
                adjacent_numbers = 0
                
                #checking adjacent
                positions = [-1, 0, 1]
                for x_move in positions:
                    for y_move in positions:
                        if (x_move != 0 or y_move != 0) and is_occupied_seat_v2(grid, x, y, x_move, y_move):
                            adjacent_numbers += 1

                if is_occupied_seat(grid[y][x]) and adjacent_numbers >= 5:
                    new_line += ["L"]
                elif not is_occupied_seat(grid[y][x]) and adjacent_numbers == 0:
                    new_line += ["#"]
                else:
                    new_line += [grid[y][x]]
        grid_to_compare += [new_line]

    return grid_to_compare

def is_occupied_seat(cell):
    return cell == "#"

def main():
    print("---___---")
    grid = get_grid("input.txt")
    print("v1")
    number_of_seats = get_number_of_seats(grid)
    print(number_of_seats)
    print("v2")
    number_of_seats = get_number_of_seats_v2(grid)
    print(number_of_seats)

if __name__ == "__main__":
    main()