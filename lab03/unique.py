from gen_random import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.data = items
        self.ignore_case = False
        if len(kwargs) > 0:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        it = iter(self.data)
        while True:
            try:
                cur = next(it)
            except StopIteration:
                raise StopIteration
            else:
                if self.ignore_case is True and isinstance(cur, str):
                    cur = cur.lower()
                if cur not in self.used_elements:
                    self.used_elements.add(cur)
                    return cur

    def __iter__(self):
        return self


def main():
    data = gen_random(2, 1, 3)
    iter = Unique(data, ignore_case=True)
    for i in iter:
        print(i)
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    iter = Unique(data, ignore_case=False)
    for i in iter:
        print(i)


if __name__ == "__main__":
    main()
