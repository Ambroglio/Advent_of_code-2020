def get_sum_from_questions(questions):
    sum_questions = 0
    for types_questions in questions:
        sum_questions += len(types_questions)

    return sum_questions

def get_answered_questions(filename):
    questions = []
    with open(filename) as f:
        question = []
        for line in f:
            if line != "\n":
                for charac in line:
                    if charac != "\n" and charac not in question:
                        question += [charac]
            else:
                questions += [question]
                question = []

        questions += [question]

    return questions

def get_answered_questions_v2(filename):
    questions = []
    with open(filename) as f:
        question = {}
        nb_voters = 0
        for line in f:
            if line != "\n":
                nb_voters += 1
                for charac in line:
                    if charac != "\n":
                        if charac not in question:
                            question[charac] = 1
                        else:
                            question[charac] += 1
            else:
                question["nb_voters"] = nb_voters
                questions += [question]
                question = {}
                nb_voters = 0

        question["nb_voters"] = nb_voters
        questions += [question]

    return questions

def get_sum_from_questions_v2(questions):
    nb_questions_answered = 0
    for question in questions:
        nb_voters = question["nb_voters"]
        for elt in question:
            if elt != "nb_voters" and question[elt] == nb_voters:
                nb_questions_answered += 1

    return nb_questions_answered
    

def main():
    questions = get_answered_questions("input.txt")
    questions_v2 = get_answered_questions_v2("input.txt")
    sum_questions = get_sum_from_questions(questions)
    sum_questions_v2 = get_sum_from_questions_v2(questions_v2)
    print(sum_questions)
    print(sum_questions_v2)

if __name__ == "__main__":
    main()