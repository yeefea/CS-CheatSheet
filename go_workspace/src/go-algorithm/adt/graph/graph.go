package graph

import (
	"fmt"
)

const (
	WHITE = iota
	GRAY
	BLACK
)

// Vertex vertex
type Vertex struct {
	Value interface{}
}

// VertexList vertex list
type VertexList []*Vertex

// Graph graph
type Graph map[*Vertex]VertexList

// NewVertex vertex pointer
func NewVertex(val interface{}) *Vertex {
	return &Vertex{val}
}

// NewGraph create new Graph
func NewGraph() Graph {
	return make(Graph)
}

// Describe nicely print values in the vertex list
func (vList VertexList) Describe() {
	fmt.Printf("[")
	for _, v := range vList {
		fmt.Printf(" %v", v.Value)
	}
	fmt.Printf(" ]\n")
}

// Describe nicely print the graph
func (g Graph) Describe() {
	for v1, vList := range g {
		fmt.Printf("%v -> [", v1.Value)
		for _, v2 := range vList {
			fmt.Printf(" %v", v2.Value)
		}
		fmt.Printf(" ]\n")
	}
}

// GetInDegree in degree of vertex
func (g Graph) GetInDegree(v *Vertex) int {
	indegree := 0
	for _, adjList := range g {
		if adjList == nil {
			continue
		}
		for _, x := range adjList {
			if v == x.Value {
				indegree++
			}
		}
	}
	return indegree
}

// GetOutDegree out degree of vertex
func (g Graph) GetOutDegree(v *Vertex) int {
	adjList := g[v]
	if adjList == nil {
		return 0
	}
	return len(adjList)
}
