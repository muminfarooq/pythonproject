"""
Map, Filter, Reduce
Jimmy Tran
"""
import unittest
from MapFilterReduce import *


class TestMapFilterReduce(unittest.TestCase):
    def testSimpleMap(self):
        list1 = MfrList([1, 2, 3])
        # triples the value of each element in the MfrList object
        self.assertListEqual(list1.map(lambda x: x * 3), MfrList([3, 6, 9]))
        self.assertListEqual(MfrList([]).map(lambda x: x * 3), MfrList([]))

    def testSimpleReduce(self):
        list1 = MfrList([2, 3, 4])
        list2 = MfrList([])
        list3 = MfrList([5])
        # triples the value of each element in the MfrList object
        self.assertEqual(list1.reduce(lambda a, b: a + b), 9)
        self.assertEqual(list1.reduce(lambda a, b: a + b, 11), 20)
        self.assertEqual(list2.reduce(lambda a, b: a + b, 10), 10)
        self.assertEqual(list3.reduce(lambda a, b: a + b), 5)
        self.assertEqual(list3.reduce(lambda a, b: a + b, 12), 17)
        with self.assertRaises(TypeError):
            c = list2.reduce(lambda a, b: a + b)
            print(c)

    def testSimpleFilter(self):
        list1 = MfrList([2, 3, 4])
        key = 2
        self.assertEqual(list1.filter(lambda y: y == key), MfrList([2]))
        self.assertEqual(list1.filter(lambda y: y % 2 == 0), MfrList([2, 4]))
        key_new = 1868
        self.assertEqual(list1.filter(lambda y: y % 2 == key_new), MfrList([]))
        list2 = MfrList(["Go", "Bears", 1868, "Oski"])
        self.assertEqual(list2.filter(lambda y: hasattr(y, "capitalize")), MfrList(["Go", "Bears", "Oski"]))
        key_new_new = 1868
        self.assertEqual(MfrList([]).filter(lambda y: y % 2 == key_new_new), MfrList([]))

    def testSquare(self):
        inputs = [MfrList([12, 98, 53]), MfrList([0, 0, 0]), MfrList([-12, -98, -53])]
        results = [MfrList([144, 9604, 2809]), MfrList([0, 0, 0]), MfrList([144, 9604, 2809])]
        for i, j in zip(inputs, results):
            self.assertListEqual(square(i), j)

    def testOdds(self):
        inputs = [MfrList([12, 98, 53]), MfrList([-2, -2, -1]), MfrList([12, 12, 12]), MfrList([]), MfrList([99])]
        results = [MfrList([53]), MfrList([-1]), MfrList([]), MfrList([]), MfrList([99])]
        for i, j in zip(inputs, results):
            self.assertListEqual(odds(i), j)

    def testAddAll(self):
        inputs = [MfrList([1, 2, 3, 4, 5]), MfrList([1, 2, -3]), MfrList([0]), MfrList([-12, -12, -12]), MfrList([])]
        results = [15, 0, 0, -36, 0]
        for i, j in zip(inputs, results):
            self.assertEqual(add_all(i), j)

    def testSumOfSquares(self):
        inputs = [MfrList([1, 2, 3, 4, 5]), MfrList([1, 2, -3]), MfrList([0, 0]),
                  MfrList([-12, -12, -12]), MfrList([]), MfrList([25])]
        results = [55, 14, 0, 432, 0, 625]
        for i, j in zip(inputs, results):
            self.assertEqual(sum_of_squares(i), j)

    def testIsIn(self):
        inputs = [MfrList(["Stanford", "Cardinals"]), MfrList(["Stanford"]),
                  MfrList(["Potato", 0, 2.5]), MfrList([-4, -4, -4]), MfrList([])]
        keys = ["Cardinals", "Oski", 2.5, 0, "potato"]
        results = [True, False, True, False, False]
        for i, j, k in zip(inputs, keys, results):
            self.assertEqual(is_in(i, j), k)

    def testCapitalize(self):
        self.assertRaises(TypeError, lambda: capitalize(MfrList([1, 2, 3])))
        inputs = [MfrList(["stanford", "cardinals"]), MfrList(["bRuInS"]), MfrList(["Potato", "0", "2.5"]),
                  MfrList(["-4", "-4", "-4"]), MfrList([]), MfrList(["anakin", "skywalker", "dARTH", "vADER"])]
        results = [MfrList(["Stanford", "Cardinals"]), MfrList(["Bruins"]), MfrList(["Potato", "0", "2.5"]),
                   MfrList(["-4", "-4", "-4"]), MfrList([]), MfrList(["Anakin", "Skywalker", "Darth", "Vader"])]
        for i, j in zip(inputs, results):
            self.assertEqual(capitalize(i), j)

    def testBetween(self):
        inputs = [["A", "B", "C"], ["C", "C", "D"], [1, 2, 3], [4, 5, 6], [], [1], ["A"], ["Bat", "Cat", "Door"],
                  ["Car", "Caterpillar", "Cardinals"]]
        test_start = ["A", "D", 1, -40, "Alpha", 1, "A", "Z", "Ca"]
        test_end = ["C", "D", 3, -50, "Omega", 2, "A", "A", "Zed"]
        results = [["A", "B"], [], [1, 2], [], [], [1], [], [], ["Car", "Caterpillar", "Cardinals"]]
        for i, j, k, l in zip(inputs, test_start, test_end, results):
            self.assertEqual(between(MfrList(i), j, k), MfrList(l))

    def testOldest(self):
        with self.assertRaises(TypeError):
            oldest(MfrList([]))
        # Like the one above but a different way
        self.assertRaises(TypeError, lambda: oldest(MfrList([])))
        inputs = [[("John", 28), ("Mary", 30), ("Jake", 5)], [("Jonathan", 21), ("Joseph", 21)], [("Jotaro", 18)]]
        results = ["Mary", "Jonathan", "Jotaro"]
        for i, j in zip(inputs, results):
            self.assertEqual(oldest(MfrList(i)), j)

    def testJoin(self):
        inputs = [[], ["", "", ""], [" ", " ", " "], ["", "hello", "there"], [1], [2.2], ["Herro"], ["Aang", "Avatar"],
                  [1, "Dragons", 2.24]]
        sep = ["hello", "+", "+", "-", 1, 2, 3, " is the ", 2342.34]
        results = ["", "++", " + + ", "-hello-there", "1", "2.2", "Herro", "Aang is the Avatar",
                   "12342.34Dragons2342.342.24"]
        for i, j, k in zip(inputs, sep, results):
            self.assertEqual(join(MfrList(i), j), k)

    def testSame(self):
        inputs = [[], [1], [2.2], ["Herro"], ["A", "A", "B"], [-1, -1, -1], ["-1", -1, -1.0],
                  ["C", "C", "C"], [-1, -1., -1.00, -1.000000]]
        results = [True, True, True, True, False, True, False, True, True]
        for i, j in zip(inputs, results):
            self.assertEqual(same(MfrList(i)), j)

    def testAbsOfEven(self):
        inputs = [MfrList([12, -98, 53]), MfrList([-2, -2, -1]), MfrList([12, -12, 2]), MfrList([]), MfrList([99]),
                  MfrList([-24.6]), MfrList([-88.0])]
        results = [MfrList([12, 98]), MfrList([2, 2]), MfrList([12, 12, 2]), MfrList([]), MfrList([]), MfrList([]),
                   MfrList([88])]
        for i, j in zip(inputs, results):
            self.assertListEqual(abs_of_evens(i), j)

    def testCountStr(self):
        with self.assertRaises(TypeError):
            count_str(MfrList([]), "POTATO")
        inputs = [["A" for _ in range(4)], ["A" for _ in range(4)], ["A", "A", "A", "Z"], ["Herro"], ["HELLO"]]
        key = ["A", "a", "a", "herro", "herro"]
        results = [4, 4, 3, 1, 0]
        for i, j, k in zip(inputs, key, results):
            self.assertEqual(count_str(MfrList(i), j), k)

    def testPalindrome(self):
        self.assertRaises(TypeError, lambda: longest_palindrome(MfrList([])))
        self.assertRaises(TypeError, lambda: longest_palindrome(MfrList(["tom", "jerry", "kids"])))
        inputs = [["noon", "racecar", "poop"], ["noon"], ["noon", "poop", "wuuw"]]
        results = ["racecar", "noon", "noon"]
        for i, j in zip(inputs, results):
            self.assertEqual(longest_palindrome(MfrList(i)), j)


if __name__ == "__main__":
    unittest.main()
