ORIGIN_X = 0
ORIGIN_Y = 0

def getGrid(filename):
    grid = []

    with open(filename) as f:
        for line in f:
            gridline = []
            for charac in line:
                if charac in [".", "#"]:
                    gridline += [charac]
            grid += [gridline]
    
    return grid

def getNumberOfTrees(grid, slope_right, slope_down):
    gridHeight = len(grid)

    x = ORIGIN_X
    y = ORIGIN_Y

    totalGrid = []

    for line in grid:
        totalGrid += [line.copy()]

    numberOfTrees = 0

    while y < gridHeight:
        if x != ORIGIN_X and y != ORIGIN_Y:
            if x >= len(totalGrid[0]):
                for line in totalGrid:
                    line += line

            if totalGrid[y][x] == "#":
                totalGrid[y][x] = "X"
                numberOfTrees += 1
            else: 
                totalGrid[y][x] = "O"
        x += slope_right
        y += slope_down

    return numberOfTrees

def printGrid(grid):
    res = ""
    for line in grid:
        for charac in line:
            res += charac
        res += "\n"
    print(res)

def main():
    grid = getGrid("input.txt")

    numberOfTrees_1_1 = getNumberOfTrees(grid, 1, 1)
    numberOfTrees_3_1 = getNumberOfTrees(grid, 3, 1)
    numberOfTrees_5_1 = getNumberOfTrees(grid, 5, 1)
    numberOfTrees_7_1 = getNumberOfTrees(grid, 7, 1)
    numberOfTrees_1_2 = getNumberOfTrees(grid, 1, 2)

    print(numberOfTrees_1_1)
    print(numberOfTrees_3_1)
    
    print(numberOfTrees_5_1)
    print(numberOfTrees_7_1)
    print(numberOfTrees_1_2)

    print(
        numberOfTrees_1_1 * 
        numberOfTrees_3_1 * 
        numberOfTrees_5_1 *
        numberOfTrees_7_1 *
        numberOfTrees_1_2
    )

if __name__ == "__main__":
    main()