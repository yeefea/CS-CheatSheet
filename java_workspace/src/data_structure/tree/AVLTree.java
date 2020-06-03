package data_structure.tree;

import java.util.Comparator;
import java.util.Iterator;

import exception.UnderflowException;

public class AVLTree<T> extends AbstractSearchTree<T> {

	private static class AVLNode<T> {

		int height;
		AVLNode<T> left;
		AVLNode<T> right;
		T value;

		AVLNode(T value) {
			this(value, null, null);
		}

		AVLNode(T value, AVLNode<T> left, AVLNode<T> right) {
			this.value = value;
			this.left = left;
			this.right = right;
			height = 0;
		}
	}

	public static void main(String[] args) {
		AVLTree<String> avl = new AVLTree<>();
		for (int i = 0; i < 31; ++i) {
			avl.insert(String.valueOf(i)+String.valueOf(i));
		}
		avl.insert(String.valueOf(-1));
		System.out.println(avl);

		avl.clear();
		for (int i = 31; i > 0; --i) {
			avl.insert(String.valueOf(i));
		}
		avl.remove(String.valueOf(21));
		System.out.println(avl);
		System.out.println(avl.size);

	}

	private static void outputIndentString(int indent, StringBuilder sb) {
		for (int i = 0; i < indent; ++i) {
			sb.append("|  ");
		}
		sb.append("+--");
	}

	private static <T> void outputNode(int indent, AVLNode<T> node, StringBuilder sb) {
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

	private Comparator<? super T> cmp;

	private AVLNode<T> root;

	private int size;

	public AVLTree() {
		root = null;
		cmp = null;
		size = 0;
	}

	public AVLTree(Comparator<? super T> cmp) {
		root = null;
		this.cmp = cmp;
		size = 0;
	}

	private AVLNode<T> balance(AVLNode<T> node) {
		if (node == null)
			return node;
		if (height(node.left) - height(node.right) > 1) {
			if (height(node.left.left) >= height(node.left.right))
				node = rotateWithLeftChild(node);
			else
				node = doubleWithLeftChild(node);
		} else if (height(node.right) - height(node.left) > 1) {
			if (height(node.right.right) >= height(node.right.left))
				node = rotateWithRightChild(node);
			else
				node = doubleWithRightChild(node);
		}
		node.height = Math.max(height(node.left), height(node.right)) + 1;
		return node;
	}



	@Override
	public boolean contains(T value) {
		return contains(value, root);
	}

	private boolean contains(T value, AVLNode<T> node) {
		while (node != null) {
			int compareResult = compare(value, node.value);

			if (compareResult < 0)
				node = node.left;
			else if (compareResult > 0)
				node = node.right;
			else
				return true;
		}
		return false;
	}

	private AVLNode<T> doubleWithLeftChild(AVLNode<T> k3) {
		k3.left = rotateWithRightChild(k3.left);
		return rotateWithLeftChild(k3);
	}

	private AVLNode<T> doubleWithRightChild(AVLNode<T> k1) {
		k1.right = rotateWithLeftChild(k1.right);
		return rotateWithRightChild(k1);
	}

	public T findMax() {
		if (isEmpty())
			try {
				throw new UnderflowException();
			} catch (UnderflowException e) {
				System.err.println("empty tree");
				e.printStackTrace();
			}
		return findMax(root).value;
	}

	private AVLNode<T> findMax(AVLNode<T> node) {
		if (node == null)
			return node;
		while (node.right != null) {
			node = node.right;
		}
		return node;
	}

	public T findMin() {
		if (isEmpty())
			try {
				throw new UnderflowException();
			} catch (UnderflowException e) {
				System.err.println("empty tree");
				e.printStackTrace();
			}
		return findMin(root).value;
	}

	private AVLNode<T> findMin(AVLNode<T> node) {
		if (node == null)
			return node;
		while (node.left != null) {
			node = node.left;
		}
		return node;
	}

	// height of an empty node = -1
	private int height(AVLNode<T> node) {
		return node == null ? -1 : node.height;
	}

	public void insert(T value) {
		root = insert(value, root);
		++size;
	}

	private AVLNode<T> insert(T value, AVLNode<T> node) {
		if (node == null)
			return new AVLNode<T>(value, null, null);

		int result = compare(value, node.value);
		if (result < 0) {
			node.left = insert(value, node.left);
		} else if (result > 0) {
			node.right = insert(value, node.right);
		}
		return balance(node);
	}

	public boolean isEmpty() {
		return root == null;
	}

	@Override
	public boolean remove(T value) {
		root = remove(value,root);
		--size;
		return true;
	}
	
	private AVLNode<T> remove(T value, AVLNode<T> node){
        if( node == null )
            return node;
            
        int result = compare( value, node.value );
            
        if( result < 0 )
            node.left = remove( value, node.left );
        else if( result > 0 )
            node.right = remove( value, node.right );
        else if( node.left != null && node.right != null ) // Two children
        {
        	// replace current node by the minimum value in the right child 
            node.value = findMin( node.right ).value; 
            node.right = remove( node.value, node.right );
        }
        else // single child
            node = ( node.left != null ) ? node.left : node.right;
        return balance( node );
	}

	private AVLNode<T> rotateWithLeftChild(AVLNode<T> k2) {
		AVLNode<T> k1 = k2.left;
		k2.left = k1.right;
		k1.right = k2;
		k2.height = Math.max(height(k2.left), height(k2.right)) + 1;
		k1.height = Math.max(height(k1.left), k2.height) + 1;
		return k1;
	}

	private AVLNode<T> rotateWithRightChild(AVLNode<T> k1) {
		AVLNode<T> k2 = k1.right;
		k1.right = k2.left;
		k2.left = k1;
		k1.height = Math.max(height(k1.left), height(k1.right)) + 1;
		k2.height = Math.max(height(k2.right), k1.height) + 1;
		return k2;
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

	@Override
	public void clear() {
		root=null;
		size=0;
	}

	@Override
	public boolean add(T x) {
		insert(x);
		return true;
	}

	@Override
	public Iterator<T> iterator() {
		// TODO Auto-generated method stub
		return null;
	}
}
