package data_structure;

public interface Collection<T> extends Iterable<T> {
	int size();
	boolean isEmpty();
	void clear();
	boolean contains(T x);
	boolean add(T x);
	boolean remove(T x);
	java.util.Iterator<T> iterator();
}
