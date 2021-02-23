import unittest
import random
from HybridSort import *


class TestProject3(unittest.TestCase):
    def test_get_pivot(self):
        ex = [13,51,49,35,7,48,55,23,15,3,28,37,32,17]
        pivot = find_pivot(ex,0,len(ex)-1)
        print(pivot)
        assert pivot == 17

    def test_quick(self):
        empty = []
        res = quick_sort(empty, 0, 0, len(empty)-1, True)
        print(empty)

        single = [1]
        res1 = quick_sort(single, 0, 0, len(empty)-1, True)
        print(single)

        double = [1, 2]
        res2 = quick_sort(double, 0, 0, len(double)-1, True)
        print(double)

        trip = [1, 2, 3]
        quick_sort(trip, 0, 0, len(trip)-1)
        print(trip)
        quick_sort(trip, 0, 0, len(trip)-1, True)
        print(trip)

        trip2 = [2, 2, 3, 2, 4]
        quick_sort(trip2, 0, 0, len(trip2)-1)
        print(trip2)
        quick_sort(trip2, 0, 0, len(trip2)-1, True)
        print(trip2)

    def test_quick_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        quick_sort(ex, 0, 0, len(ex)-1)
        print(ex)
        assert ex == [7, 13, 35, 42, 48, 49, 51]

        #ex = [7, 13, 35, 42, 48, 49, 51]
        #quick_sort(ex, 0, 1, len(ex) - 1, True)
        #print("Reverse: ", ex)
        #assert ex == [51,49,48,42,35,13,7]

    def test_insertion_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        insertion_sort(ex, 4, len(ex) - 1, False)
        print(ex)
        assert ex == [7, 13, 35, 42, 48, 49, 51]
        insertion_sort(ex, 0, len(ex) - 1, True)
        print("Reverse: ",ex)
        assert ex == [51,49,48,42,35,13,7]

    def test_hybrid_sort(self):
        ex = [13, 51, 49, 35, 7, 48, 42]
        quick_sort(ex,4,0,len(ex) - 1)
        print(ex)
        assert ex == [7, 13, 35, 42, 48, 49, 51]
        quick_sort(ex, 2, 0, len(ex) - 1, True)
        print(ex)
        assert ex == [51,49,48,42,35,13,7]

    def test_max_diff(self):
        #ex = [13, 21, 18]
        #diff = largest_sequential_difference(ex)
        #print(diff)
        #assert diff == None

        lst = []
        for i in range(1, 100000):
            lst.append(random.randint(1, 200000))

        print(lst)
        df = largest_sequential_difference(lst)
        print(df)

    def test_subdivide(self):
        #ex = [5, 7, 13, 51, 15, 49, 49, 35]
        #sub = subdivide(ex, 0, len(ex)-1, False)
        #print()
        #print(sub)

        #ex1 = [1, 2, 3, 7, 5, 4]
      #  ex2 = [60, 3, 30, 6, 10]
        #ex2 = ex1

        ex3 = [15, 20, 37, 71, 5]



        #sub1 = subdivide(ex1, 0, len(ex1)-1, False)
        #print()
        #sub2 = subdivide(ex2, 0, len(ex2)-1, True)

        #print()
        #sub3 = subdivide(ex3, 0, len(ex3)-1, False)
        #print()
        #sub3 = subdivide(ex3, 0, len(ex3)-1, True)
        #print()

       # ex4 = [4, 5, 7, 3, 2, 1]
        #ex5 = [4, 9, 7, 10, 15, 1]
        #sub4 = subdivide(ex4, 0, len(ex4)-1, True)
        #sub4 = subdivide(ex5, 0, len(ex5)-1, False)

       # exx = [13, 51, 49, 35, 7, 48, 42]
        exx = [35, 51, 35, 13, 48, 42, 36]
        s = subdivide(exx, 0, len(exx)-1, False)
        print(exx)
        print(s)

        #exx1 = [3, 2, 1, 2, 2]
        exx1 = [35, 51, 35, 13, 48, 42, 36]
        s1 = subdivide(exx1, 0, len(exx1)-1, True)
        print(exx1)
        print(s1)

        #ex = [7, 13, 35, 42, 48, 49, 51]
        #sub4 = subdivide(ex, 0, len(ex)-1, True)
        #print(sub4)




if __name__ == "__main__":
    unittest.main()