package data_structure.priority_queue;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;


import data_structure.tree.AbstractSearchTree;
// TODO
public class BinaryHeap<T> extends AbstractSearchTree<T> {

	private static final int DEFAULT_CAPACITY = 10;
	private int size;
	private List<T> array;
	public BinaryHeap() {
		this(DEFAULT_CAPACITY);
	}
	public BinaryHeap(int capacity){
		array = new ArrayList<>(10);
	}

	@Override
	public int size() {
		return size;
	}

	@Override
	public boolean isEmpty() {
		return size==0;
	}

	@Override
	public void clear() {
		array.clear();
		size = 0;
	}

	@Override
	public boolean contains(T x) {
		return array.contains(x);
	}

	@Override
	public boolean add(T x) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public boolean remove(T x) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}
	
	private void percolateDown(int hole){
		
	}
	
	private void buildHeap(){
		
	}

}
