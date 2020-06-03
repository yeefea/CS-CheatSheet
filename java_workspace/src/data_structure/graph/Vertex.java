package data_structure.graph;

import java.util.HashMap;

public class Vertex<T> {
	private T label;
	private HashMap<Vertex<T>,Double> adjList;
//	private boolean visitied;
//	private Vertex<T> previousVertex;
//	private double cost;
	
	public Vertex(T label){
		this.label = label;
		adjList = new HashMap<>();
//		visited = false;
//		previousVertex = null;
//		cost = 0;
	}
	public boolean connect(T endVertex, double weight){
		if(label!=endVertex){
			adjList.put(new Vertex<>(endVertex), weight);
			return true;
		}
		return false;
	}
	public boolean connect(T endVertex){
		return connect(endVertex, 0.0);
	}
	
	public boolean connect(Vertex<T> endVertex, double weight){
		if(label!=endVertex.label){
			adjList.put(endVertex, weight);
			return true;
		}
		return false;
	}
	
	public boolean connect(Vertex<T> endVertex){
		return connect(endVertex,0.0);
	}
	
	@Override
	public String toString() {
		StringBuilder sb = new StringBuilder();
		sb.append("[" + label + "] ->");
		
		for(Vertex<T> v : adjList.keySet()){
			sb.append(" ["+v.label+"("+adjList.get(v)+")]");
		}
		return sb.toString();
	}
	
	@Override
	public int hashCode() {
		return label.hashCode();
	}
	
	@Override
	public boolean equals(Object obj){
		if(obj==null || getClass()!=obj.getClass()){
			return false;
		}else{
			try{
				Vertex<T> v = (Vertex<T>)obj;
				return label==v.label;
			}catch(Exception e){
				return false;
			}
			
		}
	}

	protected class Edge{
		private Vertex<T> endVertex;
		private double weight;
		protected Edge(Vertex<T> endVertex, double weight){
			this.endVertex = endVertex;
			this.weight = weight;
		}
		public double getWeight() {
			return weight;
		}
		public void setWeight(double weight) {
			this.weight = weight;
		}
		public Vertex<T> getEndVertex() {
			return endVertex;
		}
	}
}
