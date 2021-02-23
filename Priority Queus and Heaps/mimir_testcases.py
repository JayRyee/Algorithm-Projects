import unittest
from PriorityHeap import PriorityHeap, Node, heap_sort, current_medians


class MimirTests(unittest.TestCase):



    def test_empty(self):
        min_heap = PriorityHeap()
        max_heap = PriorityHeap(False)

        min_heap.push(5, 'c')
        min_heap.push(4, 'y')
        min_heap.push(3, 'n')
        min_heap.push(2, 'd')
        min_heap.push(5, 'y')
        print(min_heap)

        assert min_heap.pop() == Node(2, 'd')
        print(min_heap)
        #assert min_heap.pop() == Node(3, 'n')
        #print(min_heap)

        max_heap.push(5, 'c')
        max_heap.push(4, 'y')
        max_heap.push(3, 'n')
        max_heap.push(2, 'd')
        max_heap.push(5, 'y')

        print(max_heap)
        assert max_heap.pop() == Node(5, 'y')
        assert max_heap.pop() == Node(5, 'c')

        print(max_heap)




    def test_push(self):
        min_heap = PriorityHeap()
        min_heap.push(5, 'c')
        min_heap.push(4, 'y')
        min_heap.push(3, 'n')
        min_heap.push(2, 'd')
        min_heap.push(5, 'y')

        assert len(min_heap._data) == 5
        assert min(min_heap._data[:5]) == min_heap._data[0]
        assert min_heap._data[1] < min_heap._data[3]
        assert min_heap._data[1] < min_heap._data[4]
        min_heap.push(6, 'y')
        assert min_heap._data[2] < min_heap._data[5]
        #print(min_heap)


        max_heap = PriorityHeap(False)
        max_heap.push(5, 'c')

        max_heap.push(4, 'y')

        max_heap.push(3, 'n')

        max_heap.push(2, 'd')
        print(max_heap)

        max_heap.push(5, 'y')

        assert len(max_heap._data) == 5
        assert max(max_heap._data[:5]) == max_heap._data[0]
        assert max_heap._data[1] > max_heap._data[3]
        assert max_heap._data[1] > max_heap._data[4]
        print(max_heap)

        max_heap.push(6, 'y')
        assert max_heap._data[2] > max_heap._data[5]

        #print(min_heap)
        print(max_heap)


    def test_pop(self):
        # test 1: tests pop returns the root
        min_heap = PriorityHeap()
        max_heap = PriorityHeap(False)

        min_heap.push(5, 'c')
        min_heap.push(4, 'y')
        min_heap.push(3, 'n')
        min_heap.push(2, 'd')
        min_heap.push(5, 'y')

        max_heap.push(5, 'c')
        max_heap.push(4, 'y')
        max_heap.push(3, 'n')
        max_heap.push(2, 'd')
        max_heap.push(5, 'y')

        assert min_heap.pop() == Node(2, 'd')
        assert max_heap.pop() == Node(5, 'y')

        # test 2: checks for length and not empty
        min_heap = PriorityHeap()
        max_heap = PriorityHeap(False)
        min_heap.push(4, 'y')
        min_heap.push(3, 'n')
        max_heap.push(4, 'y')
        max_heap.push(3, 'n')

        assert len(min_heap._data) == 2
        assert len(max_heap._data) == 2
        assert min_heap.pop().value == 'n'
        assert max_heap.pop().value == 'y'
        assert not min_heap.empty()
        assert not max_heap.empty()


    def test_min_child(self):
        from string import ascii_lowercase
        def check_min(pheap, idx, lhs=None, rhs=None):
            '''
            function helper for validating the min method
            '''
            min_child = lhs if pheap._data[lhs] < pheap._data[rhs] else rhs
            assert min_child == pheap.min_child(idx)

        heap = PriorityHeap()
        for child in ascii_lowercase:
            heap.push(ord(child), child)
        assert len(heap._data) == 26

        check_min(heap, 0, 1, 2)
        check_min(heap, 2, 5, 6)
        check_min(heap, 3, 7, 8)



    def test_max_child(self):
        from string import ascii_lowercase
        def check_max(pheap, idx, lhs=None, rhs=None):
            '''
            function helper for validating the max method
            '''
            max_child = lhs if pheap._data[lhs] > pheap._data[rhs] else rhs
            assert max_child == pheap.max_child(idx)

        heap = PriorityHeap(False)
        for child in ascii_lowercase:
            heap.push(ord(child), child)
        assert len(heap._data) == 26

        check_max(heap, 0, 1, 2)
        check_max(heap, 2, 5, 6)
        check_max(heap, 3, 7, 8)

        max_heap = PriorityHeap(False)

        max_heap.push(5, 'c')
        max_heap.push(4, 'y')
        max_heap.push(3, 'n')
        max_heap.push(4, 'd')
       # max_heap.push(3, 'n')


        #print(max_heap)
        #print(max_heap.max_child(3))


    def test_heap_sort(self):
        array = [5, 4, 3, 2, 1]
        array2 = [1, 2, 3, 4, 5]
        heap = heap_sort(array2)
        #heap = heap_sort(array)
        #assert heap == [1, 2, 3, 4, 5]
        
    def test_current_medians(self):
        data_list = [2, 4, 6, 8, 10]
        assert current_medians(data_list) == [2, 3, 4, 5, 6]



if __name__ == '__main__':
    unittest.main()
