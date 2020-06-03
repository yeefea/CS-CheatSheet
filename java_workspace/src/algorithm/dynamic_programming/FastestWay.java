package algorithm.dynamic_programming;

import java.util.Arrays;

public class FastestWay {

	public int l_star, f_star;
	private int[] f1;
	private int[] f2;
	private int[] l1;
	private int[] l2;

	public FastestWay(int e1, int e2, int x1, int x2, int[] a1, int[] a2, int[] t1, int[] t2) throws Exception {
		if (a1.length != a2.length)
			throw new Exception();
		int n = a1.length;
		f1 = new int[n];
		f2 = new int[n];
		l1 = new int[n];
		l2 = new int[n];
		f1[0] = e1 + a1[0];
		f2[0] = e2 + a2[0];
		for (int j = 1; j < n; ++j) {
			if (f1[j - 1] + a1[j] <= f2[j - 1] + t2[j - 1] + a1[j]) {
				f1[j] = f1[j - 1] + a1[j];
				l1[j] = 1;
			} else {
				f1[j] = f2[j - 1] + t2[j - 1] + a1[j];
				l1[j] = 2;
			}
			if (f2[j - 1] + a2[j] <= f1[j - 1] + t1[j - 1] + a2[j]) {
				f2[j] = f2[j - 1] + a2[j];
				l2[j] = 2;
			} else {
				f2[j] = f1[j - 1] + t1[j - 1] + a2[j];
				l2[j] = 1;
			}
		}
		if (f1[n - 1] + x1 <= f2[n - 1] + x2) {
			f_star = f1[n - 1] + x1;
			l_star = 1;
		} else {
			f_star = f2[n - 1] + x2;
			l_star = 2;
		}
	}

	public void print() {
		int i = l_star;
		System.out.println("station " + (f1.length - 1) + ", line " + i);
		for (int j = f1.length - 1; j > 0; --j) {
			if (i == 1) {
				i = l1[j];
				System.out.println("station " + (j - 1) + ", line " + i);
			} else if (i == 2) {
				i = l2[j];
				System.out.println("station " + (j - 1) + ", line " + i);
			}
		}
	}

	public void print_r() {
		System.out.println(Arrays.toString(f1));
		System.out.println(Arrays.toString(f2));
		System.out.println(Arrays.toString(l1));
		System.out.println(Arrays.toString(l2));
		print(f1.length - 1, l_star);
	}

	public void print(int station, int l) {
		if (station == 0) {
			System.out.println("station " + station + ", line " + l);
			return;
		}
		if (l == 1) {
			print(station - 1, l1[station]);
			System.out.println("station " + station + ", line " + l);
		} else if (l == 2) {
			print(station - 1, l2[station]);
			System.out.println("station " + station + ", line " + l);
		}
	}

	public static void main(String[] args) {
		int[] a1 = { 7, 9, 3, 4, 8, 4 };
		int[] a2 = { 8, 5, 6, 4, 5, 7 };
		int[] t1 = { 2, 3, 1, 3, 4 };
		int[] t2 = { 2, 1, 2, 2, 1 };
		int e1 = 2, e2 = 4, x1 = 3, x2 = 2;
		FastestWay fw;
		try {
			fw = new FastestWay(e1, e2, x1, x2, a1, a2, t1, t2);
			fw.print_r();
		} catch (Exception e) {
			e.printStackTrace();
		}


	}
}
