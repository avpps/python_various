class BinaryTree:

    def __init__(self, root_obj):
        self._key = root_obj
        self._left_child = None
        self._right_child = None
        self._root = None

    @property
    def key(self):
        print(self._key)
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    @property
    def left_child(self):
        if self._left_child:
            return self._left_child

    @left_child.setter
    def left_child(self, child):
        self._left_child = child
        child.root = self

    @property
    def right_child(self):
        if self._right_child:
            return self._right_child

    @right_child.setter
    def right_child(self, child):
        self._right_child = child
        child.root = self

    @property
    def root(self):
        if self._root:
            return self._root

    @root.setter
    def root(self, value):
        self._root = value


def parse_math_expression(exp):

    exp_pre = []
    for i in exp.split():
        if i in ['(', ')', '+', '-', '*', '/']:
            exp_pre.append(i)
        else:
            exp_pre.append(str(i))



exp = '2 * ( 2 + 2 )'
parse_math_expression(exp)
