def word_counter():
    s = input('enter the sentence')
    li = s.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)

word_counter()
