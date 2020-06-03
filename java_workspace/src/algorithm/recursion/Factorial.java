package algorithm.recursion;

public class Factorial {

	public static void main(String[] args) {
		for(int i = 1 ; i < 10; ++i)
			System.out.print(fact(i)+" ");
	}

	public static int fact(int n) {
		if (n == 1)
			return 1;
		return fact(n - 1) * n;
	}
}
