def get_bags(filename):
    bags = {}
    with open(filename) as f:
        for line in f:
            parts = line.split(" contain ")
            bag_name = parts[0]
            bags[bag_name] = {}
            contain = parts[1].split(", ")
            
            for elt in contain:
                elt = elt.replace(".\n", "")
                if elt != "no other bags":
                    number_bags = elt[0]
                    bag_type = elt[2:]
                    if number_bags == "1":
                        bag_type += "s"
                    bags[bag_name][bag_type] = (int) (number_bags)

    return bags

def get_number_of_shiny_gold_bags(bags):
    nb_bags_containing_shiny_gold_bags = 0
    for current_bags in bags:
        check_current_bags = check_bags(bags, current_bags)
        if check_current_bags:
            nb_bags_containing_shiny_gold_bags += 1
    
    return nb_bags_containing_shiny_gold_bags

def check_bags(bags, current_bags):
    if bags[current_bags] == {}:
        return False
    else:
        if "shiny gold bags" in bags[current_bags]:
            return True
        else:
            base = False
            for new_current_bags in bags[current_bags]:
                base = base or check_bags(bags, new_current_bags)
            return base

def get_number_of_bags_in_shiny_gold_bags(bags):
    return get_number_of_bags(bags, "shiny gold bags") - 1
    
def get_number_of_bags(bags, current_bags):
    if len(bags[current_bags]) == 0:
        return 1
    else: 
        base = 1
        for new_current_bags in bags[current_bags]:
            base += bags[current_bags][new_current_bags] * get_number_of_bags(bags, new_current_bags)
        return base


def main():
    print("---___---")
    bags = get_bags("input.txt")
    print("---\-/---")
    print("Number of shiny gold bags in all bags :", get_number_of_shiny_gold_bags(bags))
    print("---\-/---")
    print("Number of bags in a shiny gold bag :", get_number_of_bags_in_shiny_gold_bags(bags))

if __name__ == "__main__":
    main()