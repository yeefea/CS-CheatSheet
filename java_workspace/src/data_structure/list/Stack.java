package data_structure.list;

public class Stack<T>{

private final int DEFAULT_CAPACITY = 8;
	
	private int size;
	private T[] items;
	
	public Stack(){
		size = 0;
		ensureCapacity(DEFAULT_CAPACITY);		
	}

	public void push(T item){
		if(items.length == size){
			ensureCapacity(size*2+1);
		}
		items[size]=item;
		size++;//don't forget size++ --
	}
	
	public T pop(){
		if(size == 0)
			throw new IndexOutOfBoundsException((size-1) + "");
		return items[--size];
	}
	
	public T top(){
		if(size > 0)
			return items[size-1];
		return null;
		
	}
	
	public int size(){
		return size;
	}
	
	private void ensureCapacity(int capacity){
		if(capacity < size){
			return;
		}
		T[] oldItems = items;
		items = (T[])new Object[capacity];
		for(int i = 0; i < size() ; i++){
			items[i] = oldItems[i];
		}
		oldItems = null;
	}

}
