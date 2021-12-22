import functools
#декораторы

def print_result(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        print(func.__name__)
        if type(result) is list:
            print(*result, sep='\n')
        elif type(result) is dict:
            for k, v in result.items():
                print('{} = {}'.format(k, v))
        else:
            print(result)
        return result

    return wrapped


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('--------')
    test_1()
    test_2()
    test_3()
    test_4()
