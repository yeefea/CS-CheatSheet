package exception;

public class UnderflowException extends Exception {
	
	public UnderflowException() {
		super();
	}
	
	public UnderflowException(String msg){
		super(msg);
	}
	
	@Override
	public String toString() {
		return "Underflow exception.";
	}
}
