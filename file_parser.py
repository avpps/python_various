import time
import redis
import json
from pprint import pprint
from copy import deepcopy


def timer(fnc):

    def wrapper():
        start = time.time()
        fnc()
        end = time.time()
        print('time: ', end - start)

    return wrapper


class FileStream:

    def __init__(self, file_path):
        self.file_path = file_path

    def __iter__(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                yield line


class LineParser:

    _lines = None

    def __init__(self):
        self.lines = []

    def add_new_line(self, line):
        self._lines.append(line)

    @property
    def lines_json(self):
        return json.dumps(self._lines)

    @property
    def lines(self):
        return self._lines

    @lines.setter
    def lines(self, value):
        self._lines = value

    @lines.deleter
    def lines(self):
        self._lines = []


class RedisDB:

    def __init__(self):
        self.db = redis.Redis()

    def __setitem__(self, key, value):
        self.db.set(key, value)

    def __getitem__(self, item):
        return self.db.get(item)

    def __delitem__(self, item):
        self.db.delete(item)


@timer
def main():

    file = FileStream('sample.txt')
    parser = LineParser()
    db = RedisDB()

    split_size = 200000
    counter = 0
    page_no = 0
    for line in file:
        counter += 1
        if counter == split_size:
            db['aaa_{}'.format(page_no)] = parser.lines_json
            print('Saved page no ', page_no)
            del parser.lines
            counter = 0
            page_no += 1
        parser.add_new_line(line)
    db['aaa_{}'.format(page_no)] = parser.lines_json
    print('Saved page no ', page_no)
    del parser.lines
    page_no += 1

    for page_no in range(page_no):
        key = 'aaa_{}'.format(page_no)
        aaa = json.loads(db[key])
        print(key, len(aaa))
        del db[key]



main()
