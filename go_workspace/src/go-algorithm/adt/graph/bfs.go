package graph

// BreadthFirstSearch .
func BreadthFirstSearch(g Graph, src *Vertex) VertexList {
	// 记录颜色
	color := make(map[*Vertex]int)
	for v := range g {
		// 所有节点初始化为白色
		color[v] = WHITE
	}
	// 遍历需要的队列
	queue := VertexList{src}
	// 遍历结果
	res := make(VertexList, 0)
	var u *Vertex
	for len(queue) > 0 {
		// 第一个元素出队
		u = dequeue(&queue)
		// 添加到返回结果中
		res = append(res, u)
		adjList := g[u]
		for _, v := range adjList {
			if color[v] == WHITE {
				// 白色节点变成灰色
				color[v] = GRAY
				// 入队
				queue = append(queue, v)
			}
			// 灰色和黑色节点不处理
		}
		// u相邻的元素都处理完了,变成黑色
		color[u] = BLACK
	}
	return res
}

func dequeue(queue *VertexList) *Vertex {
	u := (*queue)[0]
	*queue = (*queue)[1:]
	return u
}
