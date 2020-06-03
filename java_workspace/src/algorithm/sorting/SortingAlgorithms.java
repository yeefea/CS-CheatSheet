/**
 * 
 */
package algorithm.sorting;

import java.util.Arrays;
import java.util.Random;

/**
 * @author shen
 *
 */
public class SortingAlgorithms {
	/**
	 * stable sorting worst O(N^2) comparisons, O(N^2) swaps, O(N^2) time best
	 * O(N) comparisons, O(1) swaps, O(N) time average O(N^2) comparisons,
	 * O(N^2) swaps, O(N^2) time; O(1) auxiliary space
	 * 
	 * @param a
	 *            array
	 */
	public static void bubbleSort(int[] a) {
		int i, j, len = a.length;
		int tmp;
		for (i = 0; i < len - 1; ++i) {
			for (j = 0; j < len - 1 - i; ++j) {
				if (a[j] > a[j + 1]) {
					tmp = a[j];
					a[j] = a[j + 1];
					a[j + 1] = tmp;
				}
			}
		}
	}

	/**
	 * stable sorting worst O(N^2) comparisons, O(N^2) swaps, O(N^2) time best
	 * O(N) comparisons, O(1) swaps, O(N) time average O(N^2) comparisons,
	 * O(N^2) swaps, O(N^2) time; O(1) auxiliary space
	 * 
	 * @param a
	 *            array
	 * @return sorted array
	 */
	public static void insertionSort(int[] a) {
		int j, len = a.length;
		int tmp;
		for (int p = 1; p < len; ++p) {
			tmp = a[p];
			for (j = p; j > 0 && tmp < a[j - 1]; --j)
				a[j] = a[j - 1];
			a[j] = tmp;
		}
	}

	/**
	 * unstable sorting; O(N^2) worst time; O(NlogN) best time; average depends on
	 * the gap sequence, can be O(N(logN)^2); O(1) auxiliary space
	 * 
	 * @param a
	 *            array
	 */
	public static void shellSort(int[] a) {
		int j;
		int tmp;
		for (int gap = a.length >>> 1; gap > 0; gap >>>= 1) {
			for (int i = gap; i < a.length; ++i) {
				tmp = a[i];
				for (j = i; j >= gap && tmp < a[j - gap]; j -= gap)
					a[j] = a[j - gap];
				a[j] = tmp;
			}
		}
	}

	/**
	 * unstable sorting; O(NlogN) average, best and worst time; O(1) auxiliary space (temporary
	 * variable)
	 * 
	 * @param a
	 *            array
	 */
	public static void heapSort(int[] a) {
		// build heap
		for (int i = (a.length >>> 1) - 1; i >= 0; i--) // length/2-1 important
														// !!
			percDown(a, i, a.length);
		// delete
		int tmp;
		for (int i = a.length - 1; i > 0; i--) {
			tmp = a[0];
			a[0] = a[i];
			a[i] = tmp;
			percDown(a, 0, i);
		}
	}

	private static void percDown(int[] a, int i, int n) {
		int child;
		int tmp;
		for (tmp = a[i]; leftChild(i) < n; i = child) {
			child = leftChild(i);
			// compare left child and right child
			if (child != n - 1 && a[child] < a[child + 1])
				child++;
			if (tmp < a[child])
				a[i] = a[child];
			else
				break;
		}
		a[i] = tmp;
	}

	private static int leftChild(int i) {
		return 2 * i + 1;
	}

	/**
	 * stable sorting; O(NlogN) best, average and worst time; O(N) space
	 * 
	 * @param a
	 *            array
	 */
	public static void mergeSort(int[] a) {
		int[] tmp = new int[a.length];
		mergeSort(a, tmp, 0, a.length - 1);
	}

	private static void mergeSort(int[] a, int[] tmpArray, int left, int right) {
		if (left < right) {
			int center = (left + right) >>> 1;
			mergeSort(a, tmpArray, left, center);
			mergeSort(a, tmpArray, center + 1, right);
			merge(a, tmpArray, left, center, right);
		}
	}

	private static void merge(int[] a, int[] tmpArray, int left, int center, int right) {
		int tmpPos = left;
		int rightStart = center + 1;
		int numElements = right - left + 1;
		while (left <= center && rightStart <= right)
			if (a[left] <= a[rightStart])
				tmpArray[tmpPos++] = a[left++];
			else
				tmpArray[tmpPos++] = a[rightStart++];
		while (left <= center)
			tmpArray[tmpPos++] = a[left++];
		while (rightStart <= right)
			tmpArray[tmpPos++] = a[rightStart++];
		for (int i = 0; i < numElements; ++i, --right)
			a[right] = tmpArray[right];

	}

	/**
	 * unstable sorting; O(NlogN) best time; O(NlogN) average time; O(N^2) worst
	 * time; O(logN) average space; O(N) worst space
	 * 
	 * @param a
	 *            array
	 */
	public static void quickSort(int[] a) {
		quicksort(a, 0, a.length - 1);
	}

	private static final int CUTOFF = 10;

	private static void quicksort(int[] a, int left, int right) {
		if (left + CUTOFF < right) {
			int pivot = median3(a, left, right);
			int tmp;
			int i = left, j = right - 1;
			for (;;) {
				for (; a[++i] < pivot;) {
				}
				for (; a[--j] > pivot;) {
				}
				if (i < j) {
					tmp = a[j];
					a[j] = a[i];
					a[i] = tmp;
				} else
					break;
			}
			// Restore pivot to a[i]
			tmp = a[i];
			a[i] = a[right - 1];
			a[right - 1] = tmp;
			quicksort(a, left, i - 1); // Sort small elements
			quicksort(a, i + 1, right); // Sort large elements
		} else
			insertionSort(a, left, right);

	}

	/**
	 * sort the left, right and middle element
	 * 
	 * @param a
	 *            array
	 * @param left
	 * @param right
	 * @return pivot element, which is stored in a[right-1]
	 */
	private static int median3(int[] a, int left, int right) {
		// center = (left+right)/2
		int center = (left + right) >>> 1;
		// sort a[center] a[left] and a[right]
		int tmp;
		if (a[center] < a[left]) {
			// swap elements
			tmp = a[center];
			a[center] = a[left];
			a[left] = tmp;
		}
		if (a[right] < a[left]) {
			tmp = a[left];
			a[left] = a[right];
			a[right] = tmp;
		}
		if (a[right] < a[center]) {
			tmp = a[right];
			a[right] = a[center];
			a[center] = tmp;
		}
		// put pivot at a[right-1]
		tmp = a[center];
		a[center] = a[right - 1];
		a[right - 1] = tmp;
		return a[right - 1];
	}

	private static void insertionSort(int[] a, int left, int right) {
		for (int p = left + 1; p <= right; p++) {
			int tmp = a[p];
			int j;
			for (j = p; j > left && tmp < a[j - 1]; j--)
				a[j] = a[j - 1];
			a[j] = tmp;
		}

	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		final int LEN = 10000;
		long startTime, endTime;
		int[] arr = new int[LEN];
		int[] tmp;
//		Random rand = new Random();
		for (int i = 0; i < LEN; ++i)
			arr[i] = LEN - i;
//			arr[i] = rand.nextInt();
		tmp = arr.clone();
		startTime = System.nanoTime();
		bubbleSort(tmp);
		endTime = System.nanoTime();
		// System.out.println(Arrays.toString(tmp));
		System.out.format("Bubble sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
		tmp = arr.clone();
		startTime = System.nanoTime();
		insertionSort(tmp);
		endTime = System.nanoTime();
		// System.out.println(Arrays.toString(tmp));
		System.out.format("Insertion sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
		tmp = arr.clone();
		startTime = System.nanoTime();
		mergeSort(tmp);
		endTime = System.nanoTime();
		// System.out.println(Arrays.toString(tmp));
		System.out.format("Merge sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
		tmp = arr.clone();
		startTime = System.nanoTime();
		heapSort(tmp);
		endTime = System.nanoTime();
		// System.out.println(Arrays.toString(tmp));
		System.out.format("Heap sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
		tmp = arr.clone();
		startTime = System.nanoTime();
		shellSort(tmp);
		endTime = System.nanoTime();
		// System.out.println(Arrays.toString(tmp));
		System.out.format("Shell sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
		tmp = arr.clone();
		startTime = System.nanoTime();
		quickSort(tmp);
		endTime = System.nanoTime();
//		System.out.println(Arrays.toString(tmp));
		System.out.format("Quick sort:\t%.5f ms%n", (endTime - startTime) * 1.0e-6);
	}
}
