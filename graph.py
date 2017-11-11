from itertools import repeat
from collections import deque

class Vertex(object):

    def __init__(self, s):
        self.s=s
    def __str__(self):
        return self.s

class ColoredVertex(Vertex):

    def __init__(self, s, c):
        super(Vertex,self).__init__(s)
        self.c = c

class Edge(object):

    def __init__(self, v1,v2,):
        self.v1 = v1
        self.v2 = v2


class WeightedEdge(Edge):

    def __init__(self, v1,v2,w=0.0):
        super(WeightedEdge,self).__init__(v1,v2)
        self.w=w
    def __str__(self):
        return '{}--({})-->{}'.format(self.v1, self.w, self.v2)


class Graph(object):
    WHITE=0
    GRAY=1
    BLACK=2 
    def __init__(self, V=None, E=None, directed=False):
        self.c = {}
        self.d = {}
        self.p = {}
        if V is None:
            self.adj_list={}
        else:
            for v in V:
                self.adj_list[v]=[]
            if E is not None:
                for v1,v2 in E:
                    self.adj_list[v1].append(v2)
                    if not directed:
                        self.adj_list[v2].append(v1)

    def breadth_first_search(self, s):
        """
        O(V+E) complexity,  shortest path
        FIFO queue
        """
        c={}
        d={}
        p={}
        for u in self.adj_list.keys():
            c[u] = WHITE
            d[u] = float('inf')
            p[u] = None
        c[s]=GRAY
        d[s]=0.0
        p[s]=None
        q = deque([s])
        while len(q)>0:
            u = q.popleft()
            print('{} distance {}'.format(u,d[u]))
            for v in self.adj_list[u]:
                if c[v] == WHITE:
                    c[v] = GRAY
                    d[v] = d[u]+1
                    p[v] = u
                    q.append(v)
                    print(q)
            c[u]=BLACK
        self.c = c
        self.d = d
        self.p = p

    def print_path(self, s, v):
        if s==v:
            print(s)
        elif self.p[v] is None:
            print('no path from {} to {}'.format(s,v))
        else:
            self.print_path(s,self.p[v])
            print(v)

    def depth_first_search(self, s):
        self.c = {}
        self.p = {}
        self.f = {}
        for u in self.adj_list.keys():
            self.c[u] = self.WHITE
            self.p[u] = None
            self.f[u] = 0
        self.time = 0
        for u in self.adj_list.keys():
            if self.c[u] ==self.WHITE:
                self.dfs_visit(u)

    def dfs_visit(self, u):
        """
        O(V+E) complexity,  shortest path
        """
        self.c[u] = self.GRAY
        self.time += 1
        self.d[u] = self.time
        for v in self.adj_list[u]:
            if self.c[v] == self.WHITE:
                self.p[v] = u
                self.dfs_visit(v)
        self.c[u] = self.BLACK
        self.time += 1
        self.f[u] = self.time


def test_bfs():
    adj_list = {
        'A':{'F','G'},
        'B':{'S','F'},
        'C':{'D','E','Z'},
        'D':{'C','S'},
        'E':{'F','C'},
        'F':{'E','B','A'},
        'G':{'A'}, 
        'S':{'B','D'},
        'Z':{'C'}
    }
    g = Graph()
    g.adj_list = adj_list
    g.breadth_first_search('A')
    g.print_path('A','Z')

def test_dfs():
    adj_list={'A':{'F','G'},
       'B':{'S','F'},
       'C':{'D','E','Z'},
       'D':{'C','S'},
       'E':{'F','C'},
       'F':{'E','B','A'},
       'G':{'A'}, 
       'S':{'B','D'},
       'Z':{'C'}
    }
    g = Graph()
    g.adj_list = adj_list
    g.depth_first_search('A')
    g.print_path('A','Z')


if __name__ == '__main__':
    # test_bfs()
    test_dfs()