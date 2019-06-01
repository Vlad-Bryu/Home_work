def number_of_symb_in_line():
    with open('referat.txt', 'r', encoding='utf-8') as r:
        i = 0
        for str in r:
            i += 1
            str = str.replace("\n", "")
            print("Количество символов в {} строке: ".format(i), len(str))


def number_of_symb_in_text():
    with open('referat.txt', 'r', encoding='utf-8') as r:
        content = r.read().replace("\n", "")
        print("Количество символо всего текста: ", len(content))


def number_of_words_in_text():
    with open('referat.txt', 'r', encoding='utf-8') as r:
        content = r.read().replace("\n", "").split()
        print("Количество слов в тексте: ", len(content))


def create_new_file():
    with open('referat.txt', 'r', encoding='utf-8') as r:
        content = r.read().replace(".", "!")

    with open('referat2.txt', 'w', encoding='utf-8') as w:
        w.write(content)
        print("Создан новый файл referat2.txt, где вместо запятых стоит воскл.знак")


number_of_symb_in_line()
number_of_symb_in_text()
number_of_words_in_text()
create_new_file()











