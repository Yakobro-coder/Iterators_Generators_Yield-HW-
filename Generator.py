import hashlib


def generator(file):
    with open(file, 'r', encoding='utf-8') as f:
        count = f.readlines()
        print(count)

        start = 1
        stop = len(count) + 1

    with open(file, 'r', encoding='utf-8') as f:
        while start < stop:
            yield f'Строка {start}'
            line = hashlib.md5(f.readline().encode())
            print(line.hexdigest())
            start += 1


for numb in generator('wiki_countries.txt'):
    print(numb)
