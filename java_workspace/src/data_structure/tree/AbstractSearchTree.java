package data_structure.tree;

import java.util.Comparator;

import data_structure.Collection;

public abstract class AbstractSearchTree<T> implements Collection<T> {

	protected Comparator<? super T> cmp;

	@SuppressWarnings("unchecked")
	protected int compare(T lhs, T rhs) {
		if (cmp != null) {
			return cmp.compare(lhs, rhs);
		} else {
			return ((Comparable<T>) lhs).compareTo(rhs);
		}
	}
}
