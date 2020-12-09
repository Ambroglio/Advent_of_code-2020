def check_sum(number, predicate_numbers):
    for i in range(0, len(predicate_numbers) - 1):
        for j in range(i + 1, len(predicate_numbers)):
            if predicate_numbers[i] + predicate_numbers[j] == number:
                return True
    return False

def find_first_number_not_respecting_algorithm(numbers):
    predicate_length = 25
    predicate_numbers = numbers[:predicate_length]
    rest_of_numbers = numbers[predicate_length:]

    for i in range(0, len(rest_of_numbers)):
        if not check_sum(rest_of_numbers[i], predicate_numbers):
            return rest_of_numbers[i]
        else:
            predicate_numbers.pop(0)
            predicate_numbers += [rest_of_numbers[i]]

def get_numbers(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers += [(int) (line.replace("\n", ""))]

    return numbers

def get_set(numbers, first_number):
    for i in range(0, len(numbers) - 1):
        current_numbers = [numbers[i]]
        continue_set = True
        j = i + 1
        while continue_set and j < len(numbers):
            number = numbers[j]
            current_numbers += [number]
            if sum(current_numbers) == first_number:
                return min(current_numbers) + max(current_numbers)
            elif sum(current_numbers) < first_number:
                j += 1
            else:
                continue_set = False

def main():
    print("---___---")
    numbers = get_numbers("input.txt")
    first_number = find_first_number_not_respecting_algorithm(numbers)
    print(first_number)
    global_number = get_set(numbers, first_number)
    print(global_number)

if __name__ == "__main__":
    main()