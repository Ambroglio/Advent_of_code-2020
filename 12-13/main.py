def get_times(filename):
    fo = open(filename)
    lines = fo.readlines()
    estimated_time = (int)(lines[0].replace("\n", ""))
    times_array = []
    times = lines[1].split(",")
    for time in times:
        if time != "\n":
            if time != "x":
                times_array += [(int) (time)]
            else:
                times_array += [0]

    return (estimated_time, times_array)

def get_good_time(global_times):
    estimated_time = global_times[0]
    times = global_times[1]

    min_time = estimated_time
    bus_id = 0

    for time in times:
        if time != 0:
            current_time = estimated_time / time
            if current_time / 1.0 == (int)(current_time):
                min_time = 0
                bus_id = time
            else:
                current_min_time = (int)(current_time + 1) * time - estimated_time
                if current_min_time < min_time:
                    min_time = current_min_time
                    bus_id = time

    return min_time * bus_id

def get_good_time_v2(global_times):
    times = global_times[1]
    good_times, index_times = get_good_times_and_index(times)

    print(good_times)
    print(index_times)

    found = False
    index, path = get_index_and_path(good_times, index_times, 100000000000000)

    print("index, path", index, path)

    while not found:
        found = check_time(good_times, index_times, index)
        if not found:
            index += path

    return good_times[0] * index

def get_good_times_and_index(times):
    good_times = []
    index_times = []

    for i in range(0, len(times)):
        time = times[i]
        if time != 0:
            good_times += [time]
            index_times += [i]

    return good_times, index_times

def get_index_and_path(times, index_times, index = 0):
    array = []
    timestamp = index_times[-1]
    i = index
    while len(array) != 2:
        if (times[0] * i + timestamp) % times[-1] == 0:
            array += [i]
        i += 1

    return (array[0], array[1] - array[0])

def check_time(times, index_times, index):
    test = True
    i = 1

    first = times[0]

    while test and i < len(times) - 1:
        test = (first * index + index_times[i]) % times[i] == 0
        i += 1

    return test
        

def main():
    print("---___---")
    global_times = get_times("input.txt")
    v1_answer = get_good_time(global_times)
    print("v1")
    print(v1_answer)
    print("-----")
    v2_answer = get_good_time_v2(global_times)
    print("v2")
    print(v2_answer)

if __name__ == "__main__":
    main()