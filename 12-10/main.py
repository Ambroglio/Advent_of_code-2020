def get_adapters(filename):
    adapters = []
    
    with open(filename) as f:
        for line in f:
            adapters += [(int) (line.replace("\n", ""))]

    return adapters

def get_number_of_differences(adapters):
    current_adapter = 0
    number_of_differences = (0, 0)
    max_adapter = max(adapters) + 3

    while current_adapter != max_adapter:
        if current_adapter + 1 in adapters:
            current_adapter += 1
            number_of_differences = (number_of_differences[0] + 1, number_of_differences[1])
        else:
            current_adapter += 3
            number_of_differences = (number_of_differences[0], number_of_differences[1] + 1)

    return number_of_differences

def get_arrangements(adapters):
    adapters += [0, max(adapters) + 3]
    adapters.sort()
    print(adapters)
    adapters_to_be_removed = []
    adapters_range_length = 0
    first_of_range = False

    for i in range(0, len(adapters)):
        adapter = adapters[i]

        if adapter + 1 in adapters:
            if first_of_range:
                adapters_range_length += 1
            else:
                first_of_range = True
        elif adapter + 2 in adapters:
            if first_of_range:
                adapters_range_length += 1
            else:
                first_of_range = True
        elif adapter + 3 in adapters:
            if adapters_range_length != 0:
                adapters_to_be_removed += [adapters_range_length]
            adapters_range_length = 0
            first_of_range = False
    
    total = 1

    for ranges in adapters_to_be_removed:
        total = total * get_number_of_perms(ranges)

    print(total)


def get_number_of_perms(n):
    if n <=2:
        return 2**n
    else:
        #maybe not 1 but ...?
        return 2**n - (2**(n-2) - 1)

def main():
    print("---___---")
    adapters = get_adapters("input.txt")
    number_of_differences = get_number_of_differences(adapters)
    print(number_of_differences)
    print(number_of_differences[0] * number_of_differences[1])
    get_arrangements(adapters)
    #x = get_number_of_perms(3) * get_number_of_perms(3) * get_number_of_perms(2) * get_number_of_perms(1) * get_number_of_perms(3) * get_number_of_perms(3)
    #print(x)

if __name__ == "__main__":
    main()