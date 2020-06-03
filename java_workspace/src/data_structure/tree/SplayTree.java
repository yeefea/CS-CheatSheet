package data_structure.tree;

import java.util.Comparator;
import java.util.Iterator;

public class SplayTree<T> extends AbstractSearchTree<T> {

	private static class SplayNode<T> {

		SplayNode<T> left;
		SplayNode<T> parent;
		SplayNode<T> right;
		T value;

		SplayNode(T value) {
			this(value, null, null, null);
		}

		SplayNode(T value, SplayNode<T> left, SplayNode<T> right, SplayNode<T> parent) {
			this.value = value;
			this.left = left;
			this.right = right;
			this.parent = parent;
		}
	}

	public static void main(String[] args) {
		SplayTree<Integer> st = new SplayTree<>();
		System.out.println(st);
		st.add(1);
		System.out.println(st);
		st.add(2);
		System.out.println(st);
		st.add(3);
		System.out.println(st);
		st.add(-2);
		System.out.println(st);
		st.add(-1);
		System.out.println(st);
		st.remove(1);
		System.out.println(st);
		st.remove(1);
		System.out.println(st);
		st.remove(-2);
		System.out.println(st);
		st.contains(3);
		System.out.println(st);
		st.contains(2);
		System.out.println(st);
	}
	
	private static void outputIndentString(int indent, StringBuilder sb) {
		for (int i = 0; i < indent; ++i) {
			sb.append("|  ");
		}
		sb.append("+--");
	}
	
	private static <T> void outputNode(int indent, SplayNode<T> node, StringBuilder sb) {
		outputIndentString(indent, sb);
		sb.append('(').append(node.value.toString()).append(")\n");
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


	private SplayNode<T> root;

	private int size;

	public SplayTree() {
		root = null;
		cmp = null;
		size = 0;
	}

	public SplayTree(Comparator<? super T> cmp) {
		root = null;
		this.cmp = cmp;
		size = 0;
	}

	@Override
	public boolean contains(T value) {
		SplayNode<T> node = find(value);
		if (node == null)
			return false;
		splay(node);
		return true;
	}

	@Override
	public void clear() {
		root = null;
		size = 0;
	}

	private SplayNode<T> find(T value) {

		SplayNode<T> tmpNode = root;
		int result;
		while (tmpNode != null) {
			result = compare(value, tmpNode.value);
			if (result < 0)
				tmpNode = tmpNode.left;
			else if (result > 0)
				tmpNode = tmpNode.right;
			else
				return tmpNode;
		}
		return null;
	}

	private SplayNode<T> findMin(SplayNode<T> t) {
		if (t == null) {
			return null;
		} else if (t.left == null) {
			return t;
		}
		return findMin(t.left);
	}

	@Override
	public boolean add(T value) {
		SplayNode<T> tmp = root;
		SplayNode<T> tmpParent = null;
		while (tmp != null) {
			tmpParent = tmp;
			if (compare(value, tmp.value) < 0) {
				tmp = tmp.left;
			} else if (compare(value, tmp.value) > 0) {
				tmp = tmp.right;
			} else {
				splay(tmp);
				return true; // TODO
			}
		}
		tmp = new SplayNode<>(value);
		if (tmpParent == null)
			root = tmp;
		else if (compare(value, tmpParent.value) < 0) {
			tmpParent.left = tmp;
			tmp.parent = tmpParent;
		} else {
			tmpParent.right = tmp;
			tmp.parent = tmpParent;
		}
		splay(tmp);
		++size;
		return true;
	}

	public boolean isEmpty() {
		return root == null;
	}

	@Override
	public boolean remove(T value) {
		SplayNode<T> node = find(value);
		if (node == null)
			return false;
		if (size == 1) {
			clear();
			return true;
		}
		splay(node);
		if (node.left == null)
			replace(node, node.right);
		else if (node.right == null)
			replace(node, node.left);
		else {
			SplayNode<T> minNode = findMin(node.right);
			if (minNode.parent != node) {
				replace(minNode, minNode.right);
				minNode.right = node.right;
				minNode.right.parent = minNode;
			}
			replace(node, minNode);
			minNode.left = node.left;
			minNode.left.parent = minNode;
		}
		--size;
		return true;
	}

	private void replace(SplayNode<T> n1, SplayNode<T> n2) {
		if (n1.parent == null)
			root = n2;
		else if (n1 == n1.parent.left)
			n1.parent.left = n2;
		else
			n1.parent.right = n2;
		if (n2 != null)
			n2.parent = n1.parent;
	}

	private void rotateLeft(SplayNode<T> node) {
		SplayNode<T> y = node.right;
		node.right = y.left;
		if (y.left != null)
			y.left.parent = node;
		// else do nothing
		y.parent = node.parent;
		if (node.parent == null)
			root = y;
		else if (node.parent.left == node)
			node.parent.left = y;
		else
			node.parent.right = y;
		y.left = node;
		node.parent = y;
	}

	private void rotateRight(SplayNode<T> node) {
		SplayNode<T> y = node.left;
		node.left = y.right;
		if (y.right != null)
			y.right.parent = node;
		y.parent = node.parent;
		if (node.parent == null)
			root = y;
		else if (node.parent.left == node)
			node.parent.left = y;
		else
			node.parent.right = y;
		y.right = node;
		node.parent = y;

	}

	@Override
	public int size() {
		return size;
	}

	// bottom up splay
	private void splay(SplayNode<T> node) {
		while (node.parent != null) {
			if (node.parent.parent == null) {
				// root
				if (node.parent.left == node)
					rotateRight(node.parent);
				else
					rotateLeft(node.parent);
			} else if (node.parent.left == node && node.parent.parent.left == node.parent) {
				rotateRight(node.parent.parent);
				rotateRight(node.parent);

			} else if (node.parent.right == node && node.parent.parent.right == node.parent) {
				rotateLeft(node.parent.parent);
				rotateLeft(node.parent);
			} else if (node.parent.left == node && node.parent.parent.right == node.parent) {
				rotateRight(node.parent);
				rotateLeft(node.parent);
			} else {
				rotateLeft(node.parent);
				rotateRight(node.parent);
			}
		}
	}

	@Override
	public String toString() {
		if (root == null)
			return "empty tree\nsize: 0";
		StringBuilder sb = new StringBuilder();
		outputNode(0, root, sb);
		sb.append("size: " + size);
		return sb.toString();
	}

	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}
}
