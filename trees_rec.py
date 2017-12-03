class BinaryTree:

    def __init__(self, root_obj=None):
        self._key = root_obj
        self._left_child = None
        self._right_child = None
        self._root = None

    @property
    def key(self):
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
        if isinstance(child, BinaryTree):
            child.root = self

    @property
    def right_child(self):
        if self._right_child:
            return self._right_child

    @right_child.setter
    def right_child(self, child):
        self._right_child = child
        if isinstance(child, BinaryTree):
            child.root = self

    @property
    def root(self):
        if self._root:
            return self._root

    @root.setter
    def root(self, value):
        self._root = value

    @property
    def print_exp(self):
        exp = '('
        if isinstance(self.left_child, float):
            exp += str(self.left_child)
        else:
            exp += self.left_child.print_exp
        exp += self.key
        if isinstance(self.right_child, float):
            exp += str(self.right_child)
        else:
            exp += self.right_child.print_exp
        exp += ')'
        return exp


def prepare_expression(exp):
    prepared = []
    for i in exp.split(' '):
        try:
            prepared.append(float(i))
        except ValueError:
            prepared.append(i)
    return prepared


def parse_math_expression_recursively(exp):

    root = BinaryTree()

    def run(exp, root):
        if isinstance(exp[0], float) and isinstance(exp[-1], float):
            root.left_child = exp[0]
            root.key = exp[1]
            root.right_child = exp[-1]
        elif isinstance(exp[0], float):
            root.left_child = exp[0]
            root.key = exp[1]
            root.right_child = run(exp[3:-1], BinaryTree())
        elif isinstance(exp[-1], float):
            root.left_child = run(exp[1:-3], BinaryTree())
            root.key = exp[-2]
            root.right_child = exp[-1]
        else:
            count = 1
            pos = 0
            while count != 0:
                pos += 1
                if exp[pos] == ')':
                    count -= 1
                elif exp[pos] == '(':
                    count += 1
            root.left_child = run(exp[1:pos], BinaryTree())
            root.key = exp[pos+1]
            root.right_child = run(exp[pos+3:-1], BinaryTree())
        return root

    return run(exp, root)


sample_expressions = [
    '2 * ( 2 + ( 1 + 1 ) )',
    '2 * ( 2 + 2 )',
    '( ( 1 + 2 ) + 3 ) * 4',
]

exp = prepare_expression(sample_expressions[2])
exp_tree = parse_math_expression_recursively(exp)
print('')

print(exp_tree.print_exp)
print(eval(exp_tree.print_exp))
