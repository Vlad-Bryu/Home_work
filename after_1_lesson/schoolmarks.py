school_marks = [
    {'school_class': '10a', 'scores': [3, 5, 5, 4, 3, 3, 3, 4, 5, 5]},
    {'school_class': '10b', 'scores': [4, 5, 3, 4, 5, 5]},
    {'school_class': '11a', 'scores': [3, 3, 5, 5, 4, 4, 4, 5]}
]

scores = []
number_of_marks = []
print(school_marks[1]['scores'])
print(sum(school_marks[0]["scores"]))


def average_marks_for_school():
    for n in school_marks:
        a = sum(n["scores"])
        b = len(n["scores"])
        scores.append(a)
        number_of_marks.append(b)
    return sum(scores)/sum(number_of_marks)


def average_marks_for_class():
    for n in school_marks:
        a = sum(n["scores"])
        b = len(n["scores"])
        d = n["school_class"]
        c = 'Средний балл {av_marks} для {school_class}'.format(av_marks=a/b, school_class=d)
        print(c)


print(average_marks_for_school())

average_marks_for_class()

