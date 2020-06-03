package data_structure.list;

public class Queue<T>{

	private static final int DEFAULT_CAPACITY = 8;

	private T[] items;
	private int front;
	private int end;
	private int currentSize;

	public Queue() {
		clear();
	}

	public Queue(int capacity) {
		currentSize = 0;
		ensureCapacity(capacity);
	}

	public void clear() {
		currentSize = 0;
		ensureCapacity(DEFAULT_CAPACITY);
	}

	public void ensureCapacity(int capacity) {
		if (capacity < currentSize) {
			return;
		}
		T[] old = items;
		items = (T[]) new Object[capacity];

		for (int i = 0; i < size(); i++) {
			items[i] = old[(front + i) % old.length];
		}
		front = 0;
		end = currentSize;
		old = null;
	}

	public int size() {
		return currentSize;
	}

	public boolean isEmpty() {
		return currentSize == 0;
	}

	public void enqueue(T item) {
		if (currentSize >= items.length) {
			ensureCapacity(currentSize * 2 + 1);
		}
		items[end] = item;
		end = (end + 1) % items.length;
		currentSize++;
	}

	public T dequeue() {
		T item = items[front];
		front = (front + 1) % items.length;
		currentSize--;
		return item;
	}

	public String toString() {
		String s = "";
		for (int i = 0; i < items.length; i++) {
			s = s + (items[i] == null ? "_ " : items[i].toString() + " ");
		}
		return s;
	}

}
