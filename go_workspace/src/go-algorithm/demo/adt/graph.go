// +build ignore

package main

import (
	"fmt"
	"go-algorithm/adt/graph"
)

func main() {
	v1 := graph.NewVertex("v1")
	v2 := &graph.Vertex{"v2"}
	v3 := &graph.Vertex{"v3"}
	v4 := &graph.Vertex{"v4"}
	v5 := &graph.Vertex{"v5"}
	v6 := &graph.Vertex{"v6"}
	v7 := &graph.Vertex{"v7"}
	fmt.Println(">>>graph")
	g := graph.NewGraph()
	g[v1] = graph.VertexList{v2, v3, v4}
	g[v2] = graph.VertexList{v4, v5}
	g[v3] = graph.VertexList{v6}
	g[v4] = graph.VertexList{v3, v6, v7}
	g[v5] = graph.VertexList{v4, v7}
	g[v6] = graph.VertexList{}
	g[v7] = graph.VertexList{v6}
	g.Describe()
	fmt.Println(">>>topological sort")
	sortRes, err := graph.TopSort(g)
	if err == nil {
		sortRes.Describe()
	} else {
		fmt.Println(err)
	}
	fmt.Println(">>>bfs")
	bfs := graph.BreadthFirstSearch(g, v1)
	bfs.Describe()
	fmt.Println(">>>dfs")
	dfs := graph.DepthFirstSearch(g)
	dfs.Describe()
}
