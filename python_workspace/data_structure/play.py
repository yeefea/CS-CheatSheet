from collections import deque

WHITE = 0
GRAY = 1
BLACK = 2


def breadth_first_search(g_adj_list: dict, source):
    """
    广度优先 O(V+E)
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

    color[source] = GRAY  # 第一次访问，变为灰色
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


def depth_first_search(g_adj_list):
    """
    深度优先 O(V+E)
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


if __name__ == '__main__':
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
    v_list, d_list, p_list = breadth_first_search(adj_list, 'A')
    print('bfs', v_list, d_list, p_list)
    v_list = depth_first_search(adj_list)
    print('dfs', v_list)
