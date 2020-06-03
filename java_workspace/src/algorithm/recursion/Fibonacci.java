package algorithm.recursion;

public class Fibonacci {

	public static void main(String[] args) {
		for(int i = 1 ; i < 10; ++i)
			System.out.print(fibonacci(i)+" ");

	}
	public static int fibonacci(int n) {
        if (n <= 1) return n;
        else return fibonacci(n-1) + fibonacci(n-2);
    }

}
