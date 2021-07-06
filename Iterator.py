import json


class Iterr:
    def __init__(self, file):
        self.file = file
        self.start = -1

        with open(file, encoding='utf-8') as f:
            self.js = json.load(f)
            self.stop = len(self.js)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == self.stop:
            print('\nВсе ссылки записаны в файл "wiki_countries.txt"')
            raise StopIteration

        country = self.js[self.start]['translations']['rus']['common']
        wiki_url = country + ' - ' + f'https://ru.wikipedia.org/wiki/{country.replace(" ","_")}'

        with open('wiki_countries.txt', 'a', encoding='utf-8') as result:
            result.write(wiki_url + '\n')

        return wiki_url


for url in Iterr('countries.json'):
    print(url)
