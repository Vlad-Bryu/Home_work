def string_definition(string1, string2):
    if type(string1 and string2) == str:
        if string1 == string2:
            return 1
        elif string2 == 'learn':
            return 3
        elif len(string1) > len (string2):
            return 2
    else:
        return 0


print(string_definition("LearnPython", ["Learn", "Python"]))





