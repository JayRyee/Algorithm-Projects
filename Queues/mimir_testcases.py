import unittest
from circularqueue import CircularQueue, QStack, digit_swap

class TestProject1(unittest.TestCase):

    def test_accessors(self):
        queue = CircularQueue()

        # manually set queue variables to test accessors
        queue.data = [5, 10, 15, None]
        queue.head = 0
        queue.tail = 3
        queue.size = 3

        assert queue.is_empty() == False
        assert len(queue) == 3
        assert queue.head_element() == 5

    def test_q(self):
        queue = CircularQueue()
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        print(queue.head_element())
        print(queue.tail_element())

        queue.dequeue()
        print()
        print(queue.data[0])
        print(queue.data[1])
        print(queue.data[2])
        print(queue.data[3])

        queue.dequeue()
       # queue.enqueue(60)

        print()
        print(queue.head_element())
        print(queue.tail_element())

       # queue.grow()

        #print(queue.head_element())
        #print(queue.tail_element())

      #  queue.dequeue()
       # queue.dequeue()


        print(queue.capacity)


    def test_grow(self):
        queue = CircularQueue(5)
        queue.data = [0, 1, 2, 3, 4]
        #ueue.enqueue(5)
        queue.head = 0
        queue.tail = 0
        queue.size = 5

        queue.grow()

        #print(queue.tail_element())
        assert queue.data == [0, 1, 2, 3, 4, None, None, None, None, None]
        queue.head == 0
        queue.tail == 0
        queue.size == 5
        queue.capacity == 10

    def test_shrink(self):
        queue = CircularQueue(8)
        queue.data = [0, 1, 2, 3, None, None, None, None]
        queue.size = 4
        queue.head = 0
        queue.tail = 4

        print(queue.head)
        print(queue.tail)
        print()

        queue.dequeue()

        print(queue.head)
        print(queue.tail)
        print(queue)

        print()

        queue.dequeue()

        print(queue.head)
        print(queue.tail)
        print(queue.data)

        #queue.shrink()

        print()
        print(queue.data)
        print(queue.tail)

        #queue.shrink()
      #  print(queue.capacity)
        assert queue.data == [2, 3, None, None]
        assert queue.size == 2
        assert queue.capacity == 4
        assert queue.head == 0
        assert queue.tail == 2

    def test_enqueue(self):
        queue = CircularQueue()

        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        assert queue.data == [10, 20, 30, None]
        assert queue.size == 3
        assert queue.head == 0
        assert queue.tail == 3
        assert queue.capacity == 4

    def test_dequeue(self):
        queue = CircularQueue(6)

        for i in range(0, 5):
            queue.enqueue(i * 5)

        assert queue.data == [0, 5, 10, 15, 20, None]
        assert queue.size == 5
        assert queue.capacity == 6
        assert queue.head == 0
        assert queue.tail == 5

    def test_qstack_top(self):
        stack = QStack()

        #manually enqueue to test top accessor function
        stack.cq.enqueue(10)
        stack.cq.enqueue(20)
        stack.cq.enqueue(30)

        stack.size = 3

        assert stack.top() == 30

    def test_qstack_push(self):
        stack = QStack()
        stack.push(10)


        print(stack)

        assert stack.top() == 10
        assert stack.size == 1

        stack.push(20)

        print(stack)

        assert stack.top() == 20
        assert stack.size == 2

    def test_qstack_pop(self):
        stack = QStack()

        stack.push(1)
        print(stack)
        stack.push(2)
        print(stack)
        stack.push(3)

        print(stack)
        print(stack.top())

       # print(stack.pop())
        print(stack.top())

        assert stack.pop() == 3
        assert stack.top() == 2
        assert stack.size == 2

    def test_digit_swap(self):
        nums = "5858"
        replacements = 2
        assert digit_swap(nums, replacements) == 4  # example input 1

        nums = "56787776646"
        replacements = 1
        assert digit_swap(nums, replacements) == 5  # example input 2

        nums = "9191919191"
        replacements = 5
        assert digit_swap(nums,replacements) == 10

        nums = ""
        replacements = 0
        #print(digit_swap(nums, replacements))
        assert digit_swap(nums, replacements) == 0

        nums = ""
        replacements = 1
        assert digit_swap(nums,replacements) == 0

        nums = "0"
        replacements = 0
        assert digit_swap(nums, replacements) == 1

        nums = "00"
        replacements = 1
        assert digit_swap(nums,replacements) == 2

        nums = "1112"
        replacements = 0
        #print(digit_swap(nums, replacements))
        assert digit_swap(nums, replacements) == 3

        nums = "2111"
        replacements = 0
        assert digit_swap(nums, replacements) == 3

        nums = "2111"
        replacements = 1
        assert digit_swap(nums, replacements) == 4

        nums = "21112"
        replacements = 0
        assert digit_swap(nums, replacements) == 3

        nums = "21112"
        replacements = 1
        assert digit_swap(nums, replacements) == 4

        nums = "21112"
        replacements = 3
        assert digit_swap(nums, replacements) == 5

        nums = "111"
        replacements = 3
        assert digit_swap(nums, replacements) == 3

        nums = "113"
        replacements = None
        assert digit_swap(nums,replacements) == 2


    def test_zero_replacements(self):

        nums = None
        replacements = None
        assert digit_swap(nums,replacements) == 0

        nums = ""
        replacements = None
        assert digit_swap(nums, replacements) == 0

        nums = "1"
        replacements = None
        assert digit_swap(nums, replacements) == 1

        nums = "11"
        replacements = None
        assert digit_swap(nums, replacements) == 2

        nums = "111"
        replacements = 0
        assert digit_swap(nums, replacements) == 3

        nums = "11211"
        replacements = 0
        assert digit_swap(nums, replacements) == 4

        nums = "111221112222"
        replacements = 0
        assert digit_swap(nums, replacements) == 6






if __name__ == '__main__':
    unittest.main()