class Base:

    def __init__(self, name, value=None):
        self.name = name
        self.value = value


class Tree(Base):

    def __init__(self, name, value):
        Base.__init__(self, name, value)
        self._root = None

    def set_root(self, root):
        self._root = root

    def get_root(self):
        return self._root

    def height(self):
        if self._root:
            return None
        else:
            return None


class Node(Base):

    def __init__(self, name, value):
        Base.__init__(self, name, value)
        self._childs_edges = {}

    def set_child_edge(self, child_edge):
        self._childs_edges[len(self._childs_edges)] = child_edge

    def get_child_edges(self):
        return self._childs_edges

    def print_childs_names(self):

        def childs_names(childs_edges, path):
            if not childs_edges:
                print(path)
            else:
                for i, edge in childs_edges.items():
                    child = edge.get_child()
                    curr_path = path + '/%s' % child.name
                    childs_names(child.get_child_edges(), curr_path)

        childs_names(self.get_child_edges(), self.name)


class Edge(Base):

    def __init__(self, name, value=1):
        Base.__init__(self, name, value)
        self._child_end = None

    def set_child_end(self, child):
        self._child_end = child

    def get_child(self):
        return self._child_end


tree_1 = Tree('tree_1', 10)
start_point = Node('start_point', 10)
mid_point_1 = Node('mid_point_1', 9)
mid_point_2 = Node('mid_point_2', 8)
mid_point_3 = Node('mid_point_3', 7)
mid_point_4 = Node('mid_point_4', 6)
mid_point_5 = Node('mid_point_5', 5)

tree_1.set_root(start_point)
conn_1 = Edge('conn_1')
start_point.set_child_edge(conn_1)
conn_1.set_child_end(mid_point_1)
conn_2 = Edge('conn_2')
mid_point_1.set_child_edge(conn_2)
conn_2.set_child_end(mid_point_2)
conn_3 = Edge('conn_3')
conn_4 = Edge('conn_4')
mid_point_2.set_child_edge(conn_3)
mid_point_2.set_child_edge(conn_4)
conn_3.set_child_end(mid_point_3)
conn_4.set_child_end(mid_point_4)
conn_5 = Edge('conn_5')
mid_point_4.set_child_edge(conn_5)
conn_5.set_child_end(mid_point_5)

tree_1.
