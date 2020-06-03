package data_structure.hash_table;

public class QuadraticProbingHashTable<T> implements IHashTable<T> {

	private static final int DEFAULT_SIZE = 101;

	private static class HashEntry<T> {
		public T value;
		public boolean isActive;

		public HashEntry(T value) {
			this(value, true);
		}

		public HashEntry(T value, boolean active) {
			this.value = value;
			this.isActive = active;
		}
	}

	private HashEntry<T>[] array;
	private int size;
	private int occupied;

	public QuadraticProbingHashTable() {
		this(DEFAULT_SIZE);
	}

	public QuadraticProbingHashTable(int size) {
		allocateArray(size);
		empty();
	}

	@SuppressWarnings("unchecked")
	private void allocateArray(int size) {
		array = new HashEntry[size];
	}

	@Override
	public void insert(T value) {
		int pos = findPos(value);
		
		array[pos] = new HashEntry<T>(value);
		++size;
		if(++size > array.length/2)
			rehash();

	}

	private void rehash() {
        HashEntry<T> [ ] oldArray = array;

        // Create a new double-sized, empty table
	    allocateArray( nextPrime( 2 * oldArray.length ) );
	    size = 0;
	
	        // Copy table over
	    for( int i = 0; i < oldArray.length; i++ )
	        if( oldArray[ i ] != null && oldArray[ i ].isActive )
	            insert( oldArray[ i ].value );
	}

	private static int nextPrime(int n) {
        if( n <= 0 )
            n = 3;

        if( n % 2 == 0 )
            n++;

        for( ; !isPrime( n ); n += 2 )
            ;

        return n;
	}

	private static boolean isPrime(int n) {
        if( n == 2 || n == 3 )
            return true;

        if( n == 1 || n % 2 == 0 )
            return false;

        for( int i = 3; i * i <= n; i += 2 )
            if( n % i == 0 )
                return false;

        return true;
	}

	@Override
	public void remove(T value) {
        int pos = findPos( value );
        if( isActive( pos ) ){
            array[ pos ].isActive = false;
            --size;
        }
	}

	@Override
	public boolean contains(T value) {
		int pos = findPos(value);
		return isActive(pos);
	}

	private boolean isActive(int pos) {
		return array[pos] != null && array[pos].isActive;
	}

	private int findPos(T value) {
		int offset = 1;
		int pos = myhash(value);
		while (array[pos] != null && !array[pos].value.equals(value)) {
			// keep the order of the conditions
			pos += offset;
			offset+=2;
			if(pos>=array.length)
				pos-=array.length;

		}
		return pos;
	}

	private int myhash(T value) {
        int hashVal = value.hashCode( );

        hashVal %= array.length;
        if( hashVal < 0 )
            hashVal += array.length;

        return hashVal;
	}

	@Override
	public void empty() {
		for (int i = 0; i < array.length; ++i) {
			array[i] = null;
		}
		size = 0;
	}

	@Override
	public int size() {
		return size;
	}

	public static void main(String[] args) {
		QuadraticProbingHashTable<String> H = new QuadraticProbingHashTable<String>( );

        final int NUMS = 400000;
        final int GAP  =   37;

        System.out.println( "Checking... (no more output means success)" );


        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            H.insert( ""+i );
        for( int i = 1; i < NUMS; i+= 2 )
            H.remove( ""+i );

        for( int i = 2; i < NUMS; i+=2 )
            if( !H.contains( ""+i ) )
                System.out.println( "Find fails " + i );

        for( int i = 1; i < NUMS; i+=2 )
        {
            if( H.contains( ""+i ) )
                System.out.println( "OOPS!!! " +  i  );
        }
	}

}
