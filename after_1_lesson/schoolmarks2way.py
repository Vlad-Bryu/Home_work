school_marks = [
    {'school_class': '10a', 'scores': [3, 5, 5, 4, 3, 3, 3, 4, 5, 5]},
    {'school_class': '10b', 'scores': [4, 5, 3, 4, 5, 5]},
    {'school_class': '11a', 'scores': [3, 3, 5, 5, 4, 4, 4, 5]}
]


def average_marks_for_school():
    full_scores = 0
    number_of_marks = 0
    for n in school_marks:
        for scores in n["scores"]:
            full_scores = full_scores + scores
        number_of_marks = number_of_marks + len(n["scores"])
    print('Средний балл для всей школы: {}'.format(full_scores/number_of_marks))


def average_marks_for_class():
    for n in school_marks:
        full_score = 0
        for scores in n["scores"]:
            full_score = full_score + scores
        average_mark = full_score / (len(n["scores"]))
        print('Средний балл {} для {}'.format(average_mark, n["school_class"]))


average_marks_for_school()
average_marks_for_class()


