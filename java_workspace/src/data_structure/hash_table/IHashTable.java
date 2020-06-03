package data_structure.hash_table;

public interface IHashTable<T> {

	public void insert(T value);

	public void remove(T value);

	public boolean contains(T value);

	public void empty();

	public int size();
}
