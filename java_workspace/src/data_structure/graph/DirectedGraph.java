package data_structure.graph;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class DirectedGraph<T> {

	private Map<T, Set<T>> vertexMap;

	public DirectedGraph() {
		vertexMap = new HashMap<>();
	}

	public boolean addVertex(T v) {
		if (vertexMap.containsKey(v))
			return false;
		vertexMap.put(v, new HashSet<>());
		return true;
	}

	public Set<T> getVertices() {
		return new HashSet<>(vertexMap.keySet());
	}

	public boolean connect(T v1, T v2) {
		if (!vertexMap.containsKey(v1) || !vertexMap.containsKey(v2))
			return false;
		return vertexMap.get(v1).add(v2);
	}
	
	public boolean disconnect(T v1, T v2){
		if(!vertexMap.containsKey(v1)||!vertexMap.containsKey(v2))
			return false;
		return vertexMap.get(v1).remove(v2);
	}

	public boolean isConnected(T v1, T v2) {
		if (!vertexMap.containsKey(v1) || !vertexMap.containsKey(v2))
			return false;
		return vertexMap.get(v1).contains(v2);
	}
	
	public int size(){
		return vertexMap.size();
	}

	@Override
	public String toString() {
		StringBuffer sb = new StringBuffer();
		for(T k : vertexMap.keySet()){
			sb.append(k+"->");
			for(T v : vertexMap.get(k)){
				sb.append(" "+v);
			}
			sb.append("\n");
		}
		
		return sb.toString();
	}

	public static void main(String[] args) {
		DirectedGraph<String> g = new DirectedGraph<>();
		g.addVertex("v1");
		g.addVertex("v2");
		g.addVertex("v3");
		g.connect("v1", "v2");
		System.out.println(g);
		g.connect("v2", "v3");
		System.out.println(g);
		g.connect("v1", "v3");
		g.connect("v1", "v4");
		System.out.println(g);
		g.disconnect("v2", "v3");
		System.out.println(g);
	}
}
