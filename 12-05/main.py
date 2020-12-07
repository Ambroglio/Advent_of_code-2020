def get_ids(file_name):
    ids = []

    with open(file_name) as f:
        for line in f:
            line = line.replace("\n", "")
            first_part = line[0:7]
            second_part = line[7:]

            print(first_part)
            f_p_a = 0
            f_p_b = 127
            for char in first_part:
                if char == "F":
                    f_p_b = (int) ((f_p_a + f_p_b) / 2)
                else:
                    f_p_a = (int) ((f_p_a + f_p_b + 1) / 2)
            print(f_p_a, f_p_b)

            print(second_part)
            s_p_a = 0
            s_p_b = 7
            for char in second_part:
                if char == "L":
                    s_p_b = (int) ((s_p_a + s_p_b) / 2)
                else:
                    s_p_a = (int) ((s_p_a + s_p_b + 1) / 2)
            print(s_p_a, s_p_b)

            id = f_p_a * 8 + s_p_a
            print(id)

            ids += [id]

    return ids

def find_my_seat(ids):
    ids.sort()
    
    current_id = ids[0]
    for id in ids:
        if current_id == id:
            current_id += 1

    return current_id

def main():
    ids = get_ids("input.txt")
    print("---")
    print("max id")
    print(max(ids))
    print("---")
    print("my id")
    print(find_my_seat(ids))

if __name__ == "__main__":
    main()