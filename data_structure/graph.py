from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2


class Vertex(object):

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s


class ColoredVertex(Vertex):

    def __init__(self, s, c):
        super().__init__(s)
        self.c = c


class Edge(object):

    def __init__(self, v1, v2, ):
        self.v1 = v1
        self.v2 = v2


class WeightedEdge(Edge):

    def __init__(self, v1, v2, w=0.0):
        super(WeightedEdge, self).__init__(v1, v2)
        self.w = w

    def __str__(self):
        return '{}--({})-->{}'.format(self.v1, self.w, self.v2)


class AdjacentListGraph:

    def __init__(self, adj_list: dict):
        """
        O(V+E) space
        :param adj_list:
        """
        self._adj_list = adj_list

    @property
    def V(self):
        return list(self._adj_list.keys())

    @property
    def E(self):
        adjlist = self._adj_list
        return list((v, u) for v in adjlist for u in adjlist[v])

    def is_connected(self, u, v):
        if u in self._adj_list:
            return v in self._adj_list[u]
        return False

    def in_degree(self, v):
        """
        O(E) time
        :param v:
        :return:
        """
        return sum(1 for tmp in self._adj_list.values() for x in tmp if x == v)

    def out_degree(self, v):
        """
        O(1) time
        :param v:
        :return:
        """
        return len(self._adj_list[v])

    @property
    def T(self):
        t = {}
        for key, value in self._adj_list.items():
            for v in value:
                if v not in t:
                    t[v] = {key}
                else:
                    t[v].add(key)
        return AdjacentListGraph(t)


class AdjacentMatrixGraph:

    def __init__(self, matrix):
        """
        O(V^2) space
        :param matrix:
        """
        self._m = matrix

    @property
    def V(self):
        return list(range(len(self._m)))

    @property
    def E(self):
        e = []
        for i, u in enumerate(self._m):
            for j, v in enumerate(self._m[i]):
                if v != 0:
                    e.append((i, j))
        return e

    @property
    def T(self):
        """
        transposed graph
        :return:
        """
        if not self._m:
            return AdjacentMatrixGraph([])
        l = len(self._m)
        t = [
            [None for _ in range(l)] for _ in range(l)
        ]
        for i, tmp in enumerate(self._m):
            for j, v in enumerate(self._m[i]):
                t[j][i] = v
        return AdjacentMatrixGraph(t)


def breadth_first_search(g_adj_list: dict, source):
    """
    O(V+E)
    构造广度优先树，类似于树的层序遍历，要用到queue
    扩展 Prim算法 Dijkstra算法
    :param g_adj_list: adjacent list
    :param source: source vertex
    :return: vertex list, parent map, parent map
    """
    if source not in g_adj_list:
        raise ValueError(source)
    color = {}  # WHITE GRAY BLACK
    distance = {}
    parent = {}
    for u in g_adj_list.keys() - {source}:
        # 所有顶点初始值白色
        color[u] = WHITE
        distance[u] = float('inf')
        parent[u] = None

    color[source] = GRAY  # 第一次访问（发现顶点），变为灰色
    distance[source] = 0
    parent[source] = None
    queue = deque([source])
    vertices = [source]  # 记录返回值
    while len(queue) > 0:
        u = queue.popleft()
        for v in g_adj_list[u]:
            if color[v] == WHITE:
                color[v] = GRAY
                distance[v] = distance[u] + 1
                parent[v] = u
                queue.append(v)
                vertices.append(v)
        color[u] = BLACK
    return vertices, distance, parent


def print_path(parent_g, s, v):
    if v == s:
        print(s, end=' ')
    elif v in parent_g:
        print_path(parent_g, s, parent_g[v])
        print(v, end=' ')
    else:
        print(f'no path from {s} to {v}')


def depth_first_search(g_adj_list):
    """
    O(V+E)
    :param g_adj_list: adjacent list
    :return: vertex list
    """
    def _dfs_visit(_u):
        nonlocal color
        nonlocal parent
        nonlocal times
        nonlocal discover
        nonlocal finish
        nonlocal vertices
        color[_u] = GRAY
        vertices.append(_u)
        times += 1
        discover[_u] = times
        for v in g_adj_list[_u]:
            if color[v] == WHITE:
                parent[v] = _u
                _dfs_visit(v)
        color[_u] = BLACK
        times += 1
        finish[_u] = times

    vertices = []
    color = {}
    parent = {}
    discover = {}
    finish = {}
    for u in g_adj_list:
        color[u] = WHITE
        parent[u] = None
    times = 0
    for u in g_adj_list:
        if color[u] == WHITE:
            _dfs_visit(u)
    return vertices


def topological_sort(g_adj_list):
    """
    dfs
    :param g_adj_list:
    :return:
    """
    pass


def demo_bfs():
    adj_list = {
        'A': {'F', 'G'},
        'B': {'S', 'F'},
        'C': {'D', 'E', 'Z'},
        'D': {'C', 'S'},
        'E': {'F', 'C'},
        'F': {'E', 'B', 'A'},
        'G': {'A'},
        'S': {'B', 'D'},
        'Z': {'C'}
    }
    print(breadth_first_search(adj_list, 'A'))
    print(breadth_first_search(adj_list, 'B'))
    print(breadth_first_search(adj_list, 'C'))
    print(breadth_first_search(adj_list, 'A'))
    v, d, parent = breadth_first_search(adj_list, 'A')
    print(v, d, parent)
    # print_path(parent, 'A', 'Z')


def demo_dfs():
    adj_list = {'A': {'F', 'G'},
                'B': {'S', 'F'},
                'C': {'D', 'E', 'Z'},
                'D': {'C', 'S'},
                'E': {'F', 'C'},
                'F': {'E', 'B', 'A'},
                'G': {'A'},
                'S': {'B', 'D'},
                'Z': {'C'}
                }
    print(depth_first_search(adj_list))


def problem_22_1_1():
    adj_list = {'A': {'F', 'G'},
                'B': {'S', 'F'},
                'C': {'D', 'E', 'Z'},
                'D': {'C', 'S'},
                'E': {'F', 'C'},
                'F': {'E', 'B', 'A'},
                'G': {'A'},
                'S': {'B', 'D'},
                'Z': {'C'}
                }
    g = AdjacentListGraph(adj_list)
    print(g.in_degree('C'))  # O(E)
    print(g.out_degree('C'))  # O(1)


def problem_22_1_2():
    g = AdjacentMatrixGraph([
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])
    print(g.V, g.E)


def problem_22_1_3():
    g = AdjacentMatrixGraph([
        [0, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ])
    t = g.T
    print(t.V, t.E)
    adj_list = {'A': {'F', 'G'},
                'B': {'S', 'F'},
                'C': {'D', 'E', 'Z'},
                'D': {'C', 'S'},
                'E': {'F', 'C'},
                'F': {'E', 'B', 'A'},
                'G': {'A'},
                'S': {'B', 'D'},
                'Z': {'C'}
                }
    g = AdjacentListGraph(adj_list)
    t = g.T
    print(t.V, t.E)


def problem_22_1_4():
    # todo
    pass


if __name__ == '__main__':
    # problem_22_1_1()
    # problem_22_1_2()
    # problem_22_1_3()
    # demo_bfs()
    demo_dfs()
