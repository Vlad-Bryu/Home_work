school_marks = [
    {'school_class': '10a', 'scores': [3, 5, 5, 4, 3, 3, 3, 4, 5, 5]},
    {'school_class': '10b', 'scores': [4, 5, 3, 4, 5, 5]},
    {'school_class': '11a', 'scores': [3, 3, 5, 5, 4, 4, 4, 5]}
]


def average_marks_for_school():
    scores = []
    number_of_marks = []
    for n in school_marks:
        a = sum(n["scores"])
        b = len(n["scores"])
        scores.append(a)
        number_of_marks.append(b)
    print('Средний балл для всей школы: {}'.format(sum(scores)/sum(number_of_marks)))


def average_marks_for_class():
    for n in school_marks:
        a = sum(n["scores"])
        b = len(n["scores"])
        print('Средний балл {} для {}'.format(a/b, n["school_class"]))


average_marks_for_school()
average_marks_for_class()

