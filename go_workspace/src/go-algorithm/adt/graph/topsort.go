package graph

import (
	"errors"
)

// TopSort topological sort 拓扑排序, 复杂度O(|V|+|E|)
func TopSort(g Graph) (VertexList, error) {
	// 入度表
	indegreeMap := make(map[*Vertex]int)
	// 所有节点入度初始化为0
	for v := range g {
		indegreeMap[v] = 0
	}
	// 计算入度
	for _, adjList := range g {
		for _, v := range adjList {
			indegreeMap[v]++
		}
	}
	// 入度为0的顶点列表
	queue := VertexList{}
	var v *Vertex
	for {
		v = findVertexOfIndegreeZero(indegreeMap)
		if v == nil {
			break
		}
		queue = append(queue, v)
		// 从入度表里删除顶点
		delete(indegreeMap, v)
	}
	counter := 0
	res := VertexList{}
	for len(queue) > 0 {
		// 出队
		v = queue[0]
		queue = queue[1:]
		res = append(res, v)
		// 计数
		counter++
		for _, adjV := range g[v] {
			indegreeMap[adjV]--
			// 更新后入度为0的顶点
			if indegreeMap[adjV] == 0 {
				// 入队
				queue = append(queue, adjV)
				// 从入度表里删除顶点
				delete(indegreeMap, adjV)
			}
		}
	}
	if counter != len(g) {
		return nil, errors.New("graph has a cycle")
	}
	return res, nil
}

// TopSortNaive naive topological sort 简易拓扑排序,复杂度O(|V|^2)
func TopSortNaive(g Graph) (VertexList, error) {
	// 入度表
	indegreeMap := make(map[*Vertex]int)
	// 所有节点入度初始化为0
	for v := range g {
		indegreeMap[v] = 0
	}
	// 计算入度
	for _, adjList := range g {
		for _, v := range adjList {
			indegreeMap[v]++
		}
	}
	// 排序结果列表
	var res VertexList
	// 循环的次数=顶点个数
	for i := 0; i < len(g); i++ {
		// 找入度为0的顶点
		v := findVertexOfIndegreeZero(indegreeMap)
		if v == nil {
			// 找不到说明是有环图,无法拓扑排序
			return nil, errors.New("graph has a cycle")
		}
		// 添加到排序结果中
		res = append(res, v)
		// v相邻的节点入度都-1
		for _, adjV := range g[v] {
			indegreeMap[adjV]--
		}
		// 从入度表中删除v,下次不会重复寻找
		delete(indegreeMap, v)
	}
	return res, nil
}

func findVertexOfIndegreeZero(indegreeMap map[*Vertex]int) *Vertex {
	for v, indegree := range indegreeMap {
		if indegree == 0 {
			return v
		}
	}
	return nil
}
