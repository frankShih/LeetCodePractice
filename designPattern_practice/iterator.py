'''
Traverses and accesses a container's elements.

主要精神：提供公開存取介面，有一致的方式來逐一取得物件內部的資料


'''

from collections import Iterable, Iterator


class NumberGenerator:  # iterable
    class Iterator:
        def __init__(self, length):
            self.length = length
            self.number = -1

        def __next__(self):
            self.number = self.number + 1
            if self.number == self.length:
                raise StopIteration
            return self.number

    def __init__(self, length):
        self.length = length

    def __iter__(self):
        return NumberGenerator.Iterator(self.length)


g = NumberGenerator(10)
print(type(g))
print(isinstance(g, Iterable))
print(isinstance(g, Iterator))
for n in g:
    print(n)

print("===================================")


def count_to(count):
    """Counts by word numbers, up to a maximum of five"""
    numbers = ["one", "two", "three", "four", "five"]
    # save in memory
    for number in numbers[:count]:
        yield number


def count_to_num(count):
    curr = 0    # lazy evaluation, save MEM
    while curr < count:
        yield curr
        curr += 1


def count_to_two(): return count_to(2)


def count_to_five(): return count_to(5)


def main():
    print('Counting to two...')
    for number in count_to_two():
        print(number, end=' ')

    print('\nCounting to five...')
    for number in count_to_five():
        print(number, end=' ')

    print('\nCounting to five...')
    for number in count_to_num(5):
        print(number)


if __name__ == "__main__":
    main()
