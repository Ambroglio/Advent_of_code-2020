VALUES = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def check_dict(dict_line):
    searched_length = len(VALUES)
    current_length = 0
    for value in VALUES:
        if value in dict_line:
            current_length += 1

    if current_length != searched_length:
        return False

    #print("---")
    #print("byr")
    byr = (int) (dict_line["byr"])
    if byr < 1920 or byr > 2002:
        return False

    #print("iyr")
    iyr = (int) (dict_line["iyr"])
    if iyr < 2010 or iyr > 2020:
        return False
    
    #print("eyr")
    eyr = (int) (dict_line["eyr"])
    if eyr < 2020 or eyr > 2030:
        return False

    #print("hgt")
    hgt = dict_line["hgt"]
    if "cm" in hgt:
        hgt_measure = (int) (hgt.split("cm")[0])
        if hgt_measure < 150 or hgt_measure > 193:
            return False
    else:
        hgt_measure = (int) (hgt.split("in")[0])
        if hgt_measure < 59 or hgt_measure > 76:
            return False

    #print("hcl")
    if "#" not in dict_line["hcl"]:
        return False
    hcl = dict_line["hcl"].split("#")[1]
    if len(hcl) != 6 or not (hcl.isdigit() or (hcl.islower())):
        return False

    #print("ecl")
    ecl = dict_line["ecl"]
    if ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return False

    #print("pid")
    pid = dict_line["pid"]
    if len(pid) != 9 or not pid.isdigit():
        return False

    return True

def get_number_of_passwords(file_name):
    number_of_passwords = 0
    with open(file_name) as file:
        dict_line = {}
        for line in file:
            if line != "\n":
                separated_values = line.replace("\n", "").split(" ")
                for separated_value in separated_values:
                    key_value = separated_value.split(":")
                    dict_line[key_value[0]] = key_value[1]
            else:
                if check_dict(dict_line):
                    number_of_passwords += 1
                dict_line = {}
    return number_of_passwords
            

def main():
    number_of_passwords = get_number_of_passwords("input.txt")
    print(number_of_passwords)

if __name__ == "__main__":
    main()