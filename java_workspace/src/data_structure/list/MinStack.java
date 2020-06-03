package data_structure.list;

public class MinStack {
	Stack<Integer> stack;
	Stack<Integer> minTrack;
	Stack<Integer> maxTrack;

    public MinStack() {
    	stack = new Stack<>();
    	minTrack = new Stack<>();
    	maxTrack = new Stack<>();
    }
    
    public void push(int x) {
    	stack.push(x);
    	if(minTrack.size()==0||x<minTrack.top()){
    		minTrack.push(x);
    	}
    	if(maxTrack.size()==0||x>maxTrack.top()){
    		maxTrack.push(x);
    	}
    }
    
    public int pop() {
    	int tmp = stack.pop();
    	if(tmp == minTrack.pop())
    		minTrack.pop();
    	if(tmp==maxTrack.pop())
    		maxTrack.pop();
    	return tmp;
    }
    
    public int top() {
    	return stack.top();
    }
    
    public int getMin() {
        return minTrack.top();
    }
    
    public int getMax(){
    	return maxTrack.top();
    }

	public static void main(String[] args) {
		MinStack s = new MinStack();
		s.push(1);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
		s.push(-1);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
		s.push(2);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
		s.push(3);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
		s.push(4);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
		s.push(-5);
		System.out.println(s.top());
		System.out.println(s.getMin());
		System.out.println(s.getMax());
	}

}
