package algorithm.recursion;

public class HanoiTower {
	
	static int counter = 0;
	
	public static void main(String[] args)
	{
		move(3,'A','C');
	}
	
	// 2^n - 1 minimum moves
	public static void move(int n, char s, char d){
		if(n==1){
			++counter;
			System.out.println(counter+": "+s+"->"+d);
			return;
		}
		char tmp='t';
		if('A'!=s && 'A'!=d){
			tmp = 'A';
		}else if('B'!=s && 'B'!=d){
			tmp = 'B';
		}else if('C'!=s && 'C'!=d){
			tmp = 'C';
		}
		move(n-1,s,tmp);
		move(1,s,d);
		move(n-1,tmp,d);
	}
}
