package data_structure.list;

public class ArrayList<T> implements IList<T> {

	private static final int DEFAULT_CAPACITY = 8;
	
	private int size;
	private T[] items;
	
	public ArrayList(){
		//or use ensureCapacity(DEFAULT_CAPACITY); to initialize items
		clear();
		
	}
	
	public ArrayList(int capacity){
		size=0;
		ensureCapacity(capacity);
	}
	
	public void clear(){
		size=0;
		ensureCapacity(DEFAULT_CAPACITY);
	}
	


	public int size() {
		return size;
	}
	
	public boolean isEmpty(){
		return size() == 0;
	}
	
	public void trimToSize(){
		ensureCapacity(size());		
	}
	
	public T get(int index){
		if(index < 0 || index >= size()){//add throws ArrayIndexOutOfBoundsException if want to catch it.
			throw new ArrayIndexOutOfBoundsException();//the program stops here
		}
		return items[index];
	}
	
	/*@SuppressWarnings("unchecked")*/
	public void ensureCapacity(int capacity){
		if(capacity < size){
			return;
		}
		T[] old = items;
		items = (T[]) new Object[capacity];
		for(int i = 0; i< size();i++){
			items[i] = old[i];
		}
		old=null;
	}
	
	public boolean add(T item){
		insert(size(),item);
		return true;
	}
	
	public void insert(int index, T item){
		if(items.length == size()){
			ensureCapacity(size()*2+1);
		}
		for(int i = size; i>index;i--){
			items[i] = items[i-1];
		}
		items[index]=item;
		size++;
	}
	@Override
	public T remove(int index){
		T item = items[index];
		for(int i = index; i<size();i++){
			items[i]=items[i+1];
		}
		size--;
		return item;
	}


	@Override
	public boolean contains(T value) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public java.util.Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public boolean remove(T value) {
		// TODO Auto-generated method stub
		return false;
	}
}
