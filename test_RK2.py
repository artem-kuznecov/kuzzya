import unittest
import RK2

class RK_Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(RK2.T1(), [('Среда Visual Studio', 'C#'), ('Среда Visual Studio', 'C++'), ('Среда Visual Code', 'Python'), ('Среда Xcode', 'Swift')])
    def test2(self):    
        self.assertEqual(RK2.T2(), [('Консоль', 1949.0), ('Среда Visual Code', 1991.0), ('Среда Visual Studio', 1991.5), ('Блокнот', 1993.0), ('Среда Xcode', 2014.0)])
    def test3(self):    
        self.assertEqual(RK2.T3(), [('C#', 'Среда Visual Studio'), ('C#', 'Среда Visual Studio'), ('C++', 'Среда Visual Code'), ('C++', 'Среда Visual Code')])
if __name__ == '__main__':
    unittest.main()