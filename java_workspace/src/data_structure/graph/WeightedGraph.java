package data_structure.graph;

public class WeightedGraph {

	public static void main(String[] args) {
		Vertex<String> v1= new Vertex<>("test");
		v1.connect(new Vertex<String>("v1"),2.0);
		v1.connect(new Vertex<String>("v2"),-1.0);
		v1.connect(new Vertex<String>("v5"),3.0);
		Vertex<String> v3 = new Vertex<>("v3");
		v3.connect("v4");
		v3.connect(v1,100.05);
		System.out.println(v3);

	}

}
