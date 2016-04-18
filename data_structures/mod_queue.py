from collections import deque

from data_structures.custom_exceptions import *


class ModQueue:
    def __init__(self, maxsize=0, a_list=[]):
        self.a_queue = deque(maxlen=maxsize)
        if a_list != []:
            self.a_queue.extend(a_list)

    """Returns contents of queue as a list"""
    def get_queue(self):
        return list(self.a_queue)

    """Returns type"""
    def get_type(self):
        return (type(self.a_queue))

    """Clears all of the data_structures contents"""
    def set_clear_queue(self):
        self.a_queue.clear()

    """Returns int of len of queue"""
    def get_len_queue(self):
        return len(self.a_queue)

    """Returns and removes index[0] from queue"""
    def pop(self):
        if len(self.a_queue) > 0:
            return self.a_queue.popleft()
        else:
            raise NoMoreElementsInQueue('Ran out of elements')

    """Appends to the queue from the right"""
    def append_right(self, a_value):
        if len(self.a_queue) < self.a_queue.maxlen:
            self.a_queue.append(a_value)
        else:
            raise MaxSizeLimit('Queue is at max size')

    """Returns left most value but does not remove"""
    def peek_left(self):
        return self.a_queue[0]

    def peek_right(self):
        temp = len(self.a_queue)
        return self.a_queue[temp-1]

    """Returns int. Counts the number of deque elements equal to x"""
    def get_num_items_in_front(self, a_value):
        return self.a_queue.count(a_value)

    """Takes in a list and appends it to the queue"""
    def append_list(self, a_list):
        temp_diff = self.get_max_size()-len(self.a_queue)
        if len(a_list) <= temp_diff:
            self.a_queue.extend(a_list)
        else:
            raise MaxSizeLimit("List coming in to large")

    """Returns Int of Max Size of Queue"""
    def get_max_size(self):
        return self.a_queue.maxlen

if __name__ == '__main__':
    f = ModQueue(8, [1,2,3,4])
    print(f.get_queue())
    #Test for failure
    f.append_right(5)
    print(f.get_max_size())
    print(f.pop())
    f.append_right(f.pop())
    print(f.get_queue())
    f.append_list([6,7,8])
    print(f.get_queue())
    print(f.peek_right())
    # fails the test
    # f.append_list([6, 7, 8])



