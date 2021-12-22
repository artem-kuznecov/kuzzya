import json
from print_result import print_result
import unique
from gen_random import gen_random
from cm_timer import cm_timer_1
# Сделаем другие необходимые импорты

path = "C:\Users\parkk\Desktop\лаба 3 владос\data_light.json"

with open(path, "r", encoding='utf8') as f:
    data = json.load(f)
    args = (job["job-name"] for job in data)

@print_result
def f1(args):
    return sorted(unique.Unique(args, ignore_case=False).data)


@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith("программист") is True, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    return list(zip(arg, list(gen_random(len(arg), 100000, 200000))))


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(args))))
