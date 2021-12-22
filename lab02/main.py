from rectangle import Rectangle
from circle import Circle
from square import Square


def main():
    r = Rectangle("синего", 3, 2)
    c = Circle("зеленого", 5)
    s = Square("красного", 5)
    print(r)
    print(c)
    print(s)

if __name__ == "__main__":
    main()
