school_marks = [
    {'school_class': '10a', 'scores': [3, 5, 5, 4, 3, 3, 3, 4, 5, 5]},
    {'school_class': '10b', 'scores': [4, 5, 3, 4, 5, 5]},
    {'school_class': '11a', 'scores': [3, 3, 5, 5, 4, 4, 4, 5]}
]


def average_marks_for_school():
    c = 0
    d = 0
    for n in school_marks:
        for a in n["scores"]:
            c = c + a
        d = d + len(n["scores"])
    return c/d


def average_marks_for_class():
    for n in school_marks:
        c = 0
        for a in n["scores"]:
            c = c + a
        d = c / (len(n["scores"]))
        f = n["school_class"]
        r = 'Средний балл {av_marks} для {school_class}'.format(av_marks=d, school_class=f)
        print(r)


print(average_marks_for_school())
average_marks_for_class()


