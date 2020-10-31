package graph

func DepthFirstSearch(g Graph) VertexList {
	// 遍历结果
	res := make(VertexList, 0)
	color := make(map[*Vertex]int)
	// 闭包
	var dfsVisit func(u *Vertex)
	dfsVisit = func(u *Vertex) {
		// 白色变为灰色
		color[u] = GRAY
		res = append(res, u)
		adjList := g[u]
		for _, v := range adjList {
			if color[v] == WHITE {
				// 递归
				dfsVisit(v)
			}
		}
		color[u] = BLACK
	}
	for v := range g {
		// 所有节点初始化为白色
		color[v] = WHITE
	}
	for v := range g {
		if color[v] == WHITE {
			dfsVisit(v)
		}
	}
	return res
}
