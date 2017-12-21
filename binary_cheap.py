""" The classic way to implement a priority queue is using
a data structure called a binary heap. A binary heap will
allow us both enqueue and dequeue items in O(logn).
"""


class BinaryHeap:

    def __init__(self, heap=None):
        self._heap = self.build_heap(heap)
        self._size = 0

    @property
    def heap(self):
        return self._heap[1:]

    @property
    def size(self):
        return len(self._heap[1:])

    @property
    def is_empty(self):
        return not bool(self._heap[1:])

    def build_heap(self, heap):
        if heap:
            return [None] + heap
        else:
            return [None]

    def insert(self, value):
        self._heap.append(value)
        self._move_up(child_pos=self.size)

    def find_min(self):
        pass

    def del_min(self):
        if self.is_empty:
            return
        self._heap[1] = self._heap.pop(-1)
        self._move_down(1)

    def _move_up(self, child_pos):
        parent_pos = child_pos // 2
        if parent_pos < 1:
            return
        child = self._heap[child_pos]
        parent = self._heap[parent_pos]
        if parent > child:
            self._heap[parent_pos] = child
            self._heap[child_pos] = parent
            self._move_up(parent_pos)

    def _min_childs(self, pos):
        childs_pos = (pos * 2, pos * 2 + 1)
        childs = {i: self._heap[i] for i in childs_pos if i < self.size}
        if childs:
            return min(childs.items(), key=lambda x: x[1])
        return None

    def _move_down(self, parent_pos):
        parent_value = self._heap[parent_pos]
        min_child = self._min_childs(parent_pos)
        if min_child[1] < parent_value:
            self._heap[parent_pos] = min_child[1]
            self._heap[min_child[0]] = parent_value
            self._move_up(min_child[0])


def test_binary_heap_insert():

    heap = BinaryHeap(heap=[1, 2, 7, 4, 5, 6])
    heap.insert(value=3)
    assert heap.heap == [1, 2, 3, 4, 5, 6, 7]

    heap = BinaryHeap(heap=[2, 1, 7, 4, 5, 6])
    heap.insert(value=0)
    assert heap.heap == [0, 1, 2, 4, 5, 6, 7]

def test_binary_heap_del_min():

    heap = BinaryHeap(heap=[1, 2, 3, 3])
    heap.del_min()
    assert heap.heap == [2, 3, 3]
