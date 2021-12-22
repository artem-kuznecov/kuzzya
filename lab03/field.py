def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for item in items:
            if args[0] in item and item[args[0]] is not None:
                yield item[args[0]]

    else:
        for item in items:
            dictionary = {}
            for value in args:
                if value in item and item[value] is not None:
                    dictionary[value] = item[value]
            if len(dictionary) != 0:
                yield dictionary


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    a = field(goods, 'title')
    print(next(a))
    print(next(a))


if __name__ == "__main__":
    main()
