def getListOfNumbers(file):
    numberList = []

    with open(file) as f:
        for number in f:
            number = number.replace('\n', '')
            try:
                numberList += [int(number)]
            except ValueError:
                print("Error")

    return numberList

def checkAlgorithmWithTwo(a, b):
    return a + b == 2020

def checkAlgorithmWithThree(a, b, c):
    return a + b + c == 2020

def checkNumbersWithTwo(numberList):
    for i in range(0, len(numberList) - 1):
        a = numberList[i]
        for j in range(i + 1, len(numberList)):
            b = numberList[j]
            if checkAlgorithmWithTwo(a, b):
                print(str(a) + " + " + str(b) + " = 2020")
                print(str(a) + " x " + str(b) + " = " + str(a * b))

def checkNumbersWithThree(numberList):
    for i in range(0, len(numberList) - 2):
        a = numberList[i]
        for j in range(i + 1, len(numberList) - 1):
            b = numberList[j]
            for k in range(j + 1, len(numberList)):
                c = numberList[k]
                if checkAlgorithmWithThree(a, b, c):
                    print(str(a) + " + " + str(b) + " + " + str(c) + " = 2020")
                    print(str(a) + " x " + str(b) + " x " + str(c) + " = " + str(a * b * c))


def main():
    print("AVENT OF CODE EPISODE 1")
    numberList = getListOfNumbers("input.txt")
    checkNumbersWithTwo(numberList)
    checkNumbersWithThree(numberList)

if __name__ == "__main__":
    main()