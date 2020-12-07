import re

def main():
    count = 0

    with open("input.txt") as f:
        for line in f:
            numberRange = re.split("-", re.findall(r'\d+-\d+', line)[0])
            searchedLetter = re.split(r': \D*', re.split(r'\d+-\d+ ', line)[1])[0]
            word = re.split(r'\d+-\d+ \D: ', line)[1]
        
            """
            numberOfChars = word.count(searchedLetter)
            
            if numberOfChars >= (int) (numberRange[0]) and numberOfChars <= (int) (numberRange[1]):
                count += 1 
            """

            listOfIndexes = [m.start() + 1 for m in re.finditer(searchedLetter, word)]
        
            if ((int)(numberRange[0]) in listOfIndexes and (int)(numberRange[1]) not in listOfIndexes) or ((int)(numberRange[0]) not in listOfIndexes and (int)(numberRange[1]) in listOfIndexes):
                count += 1

    print(count)

if __name__ == "__main__":
    main()