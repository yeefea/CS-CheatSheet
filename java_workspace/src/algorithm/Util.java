package algorithm;

public class Util {

	/**
	 * O(logN) time
	 * 
	 * @param n
	 * @return
	 */
	public static boolean isPowerOfTwo_1(int n) {
		int tmp = 1;
		while (tmp <= n) {
			if (tmp == n)
				return true;
			tmp <<= 1;
		}
		return false;
	}

	/**
	 * O(1) time, bitwise operator
	 * 
	 * @param n
	 * @return
	 */
	public static boolean isPowerOfTwo_2(int n) {
		return (n & (n - 1)) == 0;
	}
	/**
	 * O(number of ones), bitwise operator
	 * @param n
	 * @return
	 */
	public static int countBinaryOnes(int n) {
		int count = 0;
		while (n != 0) {
			n &= (n - 1);
			++count;
		}
		return count;
	}

	public static void main(String[] args) {
		System.out.println(isPowerOfTwo_2(0));
		System.out.println(isPowerOfTwo_2(1));
		System.out.println(isPowerOfTwo_2(2));
		System.out.println(isPowerOfTwo_2(3));
		System.out.println(isPowerOfTwo_2(4));
		System.out.println(isPowerOfTwo_2(6));
		System.out.println(isPowerOfTwo_2(7));
		System.out.println(isPowerOfTwo_2(8));
		System.out.println(isPowerOfTwo_2(9));
		System.out.println(isPowerOfTwo_2(1023));
		System.out.println(isPowerOfTwo_2(1024));
		System.out.println(isPowerOfTwo_2(1025));
		System.out.println(countBinaryOnes(0));
		System.out.println(countBinaryOnes(1));
		System.out.println(countBinaryOnes(2));
		System.out.println(countBinaryOnes(3));
		System.out.println(countBinaryOnes(6));
		System.out.println(countBinaryOnes(7));
		System.out.println(countBinaryOnes(8));
		System.out.println(countBinaryOnes(1022));
		System.out.println(countBinaryOnes(1023));
		System.out.println(countBinaryOnes(1024));
	}

}
