def even_ch(n):
    for i in range(n):
        if i%2 == 0:
            yield(i)

for value in even_ch(10):

    print(value)
