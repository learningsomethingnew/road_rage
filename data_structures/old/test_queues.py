#from data_structures.queue import Queue

#from data_structures.custom_exceptions import MaxSizeLimit
from data_structures import Queue
from nose import *


def test_queue_exists():
    q = Queue(10, [1, 2, 3, 4])
    a_list = [1, 2, 3, 4]
    assert a_list == q.get_queue()


def test_clear_queue():
    q = Queue(10, [1, 2, 3, 4])
    a_list = []
    q.set_clear_queue()
    assert a_list == q.get_queue()


def test_get_left():
    q = Queue(10, [1, 2, 3, 4])
    a_list = [1, 2, 3, 4]
    assert a_list[0] == q.pop()


def test_append_right():
    q = Queue(10, [1, 2, 3, 4])
    a_list = [1, 2, 3, 4, 5]
    assert a_list == q.set_append(5)


def test_set_append_fail():
    q = Queue(4, [1, 2, 3, 4])
    try:
        q.set_append(5)
        assert False
    except MaxSizeLimit:
        assert True

    ######################################################################################
    # Old Code
    ######################################################################################
    #
    # q = Queue(10, [1,2,3,4])
    # x = q.get_queue()
    # print(len(x))
    # print(q.get_left())
    # print(q.get_queue())
    # print(q.set_append(10))
    # print(q.get_queue())
    # print(q.get_num_items_infront(3))
    # print(q.get_queue_len())
