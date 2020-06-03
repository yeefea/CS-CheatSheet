package data_structure.tree;

import java.util.Comparator;
import java.util.Iterator;

import exception.UnderflowException;

public class BinarySearchTree<T> extends AbstractSearchTree<T> {

	private static class BinaryNode<T> {

		T element;
		BinaryNode<T> left;
		BinaryNode<T> right;

		BinaryNode(T element) {
			this(element, null, null);
		}

		BinaryNode(T element, BinaryNode<T> lt, BinaryNode<T> rt) {
			this.element = element;
			left = lt;
			right = rt;
		}
	}

	private BinaryNode<T> root;

	private int size;
	
	public BinarySearchTree() {
		root = null;
		size = 0;
	}

	public BinarySearchTree(Comparator<? super T> c) {
		root = null;
		cmp = c;
		size = 0;
	}

	@SuppressWarnings("unchecked")
	public int compare(T lhs, T rhs) {
		if (cmp != null) {
			return cmp.compare(lhs, rhs);
		} else {
			return ((Comparable<T>) lhs).compareTo(rhs);
		}
	}

	public boolean isEmpty() {
		return root == null;
	}

	public boolean contains(T x) {
		return contains(x, root);
	}

	public T findMin() {
		try {
			if (isEmpty()) {
				throw new UnderflowException();
			}
		} catch (UnderflowException e) {
			e.printStackTrace();
			System.exit(1);
		}
		return findMin(root).element;
	}

	public T findMax() {
		try {
			if (isEmpty()) {
				throw new UnderflowException();
			}
		} catch (UnderflowException e) {
			e.printStackTrace();
			System.exit(1);
		}
		return findMax(root).element;
	}

	public void insert(T x) {
		root = insert(x, root);
		++size;
	}

	public boolean remove(T x) {
		root = remove(x, root);
		--size;
		return true;
	}

	public void printTree() {
		if (root != null)
			printNode(root);
	}

	private void printNode(BinaryNode<T> t) {
		System.out.println(t.element);
		if (t.left != null) {
			printNode(t.left);
		}
		if (t.right != null) {
			printNode(t.right);
		}
	}

	private boolean contains(T x, BinaryNode<T> t) {
		if (t == null) {
			return false;
		}

		int compareResult = compare(x, t.element);

		if (compareResult < 0) {
			return contains(x, t.left);
		} else if (compareResult > 0) {
			return contains(x, t.right);
		} else {
			return true;
		}

	}

	private BinaryNode<T> findMin(BinaryNode<T> t) {
		if (t == null) {
			return null;
		} else if (t.left == null) {
			return t;
		}
		return findMin(t.left);
	}

	private BinaryNode<T> findMax(BinaryNode<T> t) {
		if (t != null) {
			while (t.right != null) {
				t = t.right;
			}
		}
		return t;
	}

	private BinaryNode<T> insert(T x, BinaryNode<T> t) {
		if (t == null) {
			return new BinaryNode<T>(x, null, null);
		}

		int compareResult = compare(x, t.element);

		if (compareResult < 0) {
			t.left = insert(x, t.left);
		} else if (compareResult > 0) {
			t.right = insert(x, t.right);
		}

		return t;
	}

	private BinaryNode<T> remove(T x, BinaryNode<T> t) {

		if (t == null) {
			return t;// do nothing
		}

		int compareResult = compare(x, t.element);

		if (compareResult < 0) {
			t.left = remove(x, t.left);
		} else if (compareResult > 0) {
			t.right = remove(x, t.right);
		} else if (t.left != null && t.right != null) {
			t.element = findMin(t.right).element;
			t.right = remove(t.element, t.right);
		} else
			t = (t.left != null) ? t.left : t.right;
		return t;
	}

	@Override
	public void clear() {
		root = null;
		size=0;
	}

	@Override
	public int size() {
		return size;
	}

	@Override
	public String toString() {
		if (root == null)
			return "empty tree";
		StringBuilder sb = new StringBuilder();
		outputNode(0, root, sb);
		return sb.toString();
	}

	private static <T> void outputNode(int indent, BinaryNode<T> node, StringBuilder sb) {
		outputIndentString(indent, sb);
		sb.append('(').append(node.element.toString()).append(")\n");
		if (node.left != null) {
			outputNode(indent + 1, node.left, sb);
		} else {
			outputIndentString(indent + 1, sb);
			sb.append("null\n");
		}

		if (node.right != null) {
			outputNode(indent + 1, node.right, sb);
		} else {
			outputIndentString(indent + 1, sb);
			sb.append("null\n");
		}
	}

	private static void outputIndentString(int indent, StringBuilder sb) {
		for (int i = 0; i < indent; ++i) {
			sb.append("|  ");
		}
		sb.append("+--");
	}

	public static void main(String[] args) {
		BinarySearchTree<Integer> bst = new BinarySearchTree<>();
		for (int i = 0; i < 20; ++i) {
			bst.insert(i);
		}
		bst.insert(-1);
		bst.remove(3);
		bst.remove(3);
		bst.remove(9);
		System.out.println(bst);
	}

	@Override
	public boolean add(T x) {
		// TODO Auto-generated method stub
		return false;
	}

	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}
}
