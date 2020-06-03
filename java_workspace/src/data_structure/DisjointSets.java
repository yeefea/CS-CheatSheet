package data_structure;

import java.util.Arrays;

public class DisjointSets {
	private int[] arr;

	public DisjointSets(int n) {
		arr = new int[n];
		for (int i = 0; i < n; ++i) {
			arr[i] = -1;
		}
	}

	/**
	 * @param rt1
	 *            root of set 1
	 * @param rt2
	 *            root of set 2
	 */
	public void union(int rt1, int rt2) {
		if (rt1 == rt2)
			return;
		if (arr[rt1] < arr[rt2]) // rt2 is deeper
			arr[rt1] = rt2;
		else {
			if (arr[rt1] == arr[rt2]) // if same depth, make rt1 deeper
				--arr[rt1];
			arr[rt2] = rt1; // here rt1 is deeper
		}
	}

	/**
	 * path compression finding
	 * 
	 * @param x
	 * @return
	 */
	public int find(int x) {
		if( x > arr.length-1) throw new ArrayIndexOutOfBoundsException();
		if (arr[x] < 0)
			return x;
		else
			return arr[x] = find(arr[x]);
	}
	
	public String toString(){
		int[] tmp = new int[arr.length];
		for(int i = 0 ; i < arr.length ; ++i)
			tmp[i] = find(i);
		return Arrays.toString(tmp);
	}

	public static void main(String[] args) {
		int n = 16;
        DisjointSets ds = new DisjointSets( n );
        System.out.println(Arrays.toString(ds.arr));
        // test union
        ds.union(0, 1);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(1, 2);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(2, 3);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(3, 5);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(4, 6);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(5, 7);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(7, 8);
        System.out.println(Arrays.toString(ds.arr));
        ds.union(8, 9);
        System.out.println(Arrays.toString(ds.arr));
        // test find
        System.out.println(Arrays.toString(ds.arr));
        ds.find(9);
        System.out.println(Arrays.toString(ds.arr));
        ds.find(6);
        System.out.println(Arrays.toString(ds.arr));
	}
}
