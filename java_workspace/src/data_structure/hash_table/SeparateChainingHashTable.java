package data_structure.hash_table;

import java.util.LinkedList;
import java.util.List;

public class SeparateChainingHashTable<T> implements IHashTable<T> {

	private static final int DEFAULT_SIZE = 101;
	private int size;
	private List<T>[] lists;
	public SeparateChainingHashTable() {
		this(DEFAULT_SIZE);
	}

	@SuppressWarnings("unchecked")
	public SeparateChainingHashTable(int size) {
		lists = new LinkedList[nextPrime(size)]; // object, type erase
		for(int i = 0 ; i < lists.length ; ++i){
			lists[i] = new LinkedList<>();
		}
	}

	@Override
	public void insert(T value) {
		List<T> list = lists[myhash(value)];
		if(!list.contains(value)){
			list.add(value);
			if(++size>lists.length)
				rehash();
		}
	}

	@Override
	public void remove(T value) {
		List<T> list = lists[myhash(value)];
		if(list.contains(value)){
			list.remove(value);
			--size;
		}
	}

	@Override
	public boolean contains(T value) {
		List<T> list = lists[myhash(value)];
		return list.contains(value);
	}

	@Override
	public void empty() {
		for(int i = 0 ; i < lists.length ; ++i)
			lists[i].clear();
		size = 0;
	}

	@Override
	public int size() {
		return size;
	}

	private void rehash(){
        List<T> [ ]  oldLists = lists;
        //Create new double-sized, empty table
	    lists = new List[ nextPrime( 2 * lists.length ) ];
	    for( int j = 0; j < lists.length; j++ )
	        lists[ j ] = new LinkedList<>( );
	    // Copy table over
	    size = 0;
	    for( List<T> list : oldLists )
	        for( T item : list )
	            insert( item );
	}
	
	private int myhash(T value){
		int hashVal = value.hashCode()%lists.length;
		if(hashVal < 0)
			hashVal += lists.length;
		return hashVal;
	}
	
	private static int nextPrime(int n){
        if( n % 2 == 0 )
            n++;

        for( ; !isPrime( n ); n += 2 )
            ;

        return n;
	}
	
	private static boolean isPrime(int n){
        if( n == 2 || n == 3 )
            return true;

        if( n == 1 || n % 2 == 0 )
            return false;

        for( int i = 3; i * i <= n; i += 2 )
            if( n % i == 0 )
                return false;

        return true;
	}
	
	public static void main(String[] args) {
        SeparateChainingHashTable<Integer> H = new SeparateChainingHashTable<>( );

        long startTime = System.currentTimeMillis( );
        
        final int NUMS = 2000000;
        final int GAP  =   37;

        System.out.println( "Checking... (no more output means success)" );

        for( int i = GAP; i != 0; i = ( i + GAP ) % NUMS )
            H.insert( i );
        for( int i = 1; i < NUMS; i+= 2 )
            H.remove( i );

        for( int i = 2; i < NUMS; i+=2 )
            if( !H.contains( i ) )
                System.out.println( "Find fails " + i );

        for( int i = 1; i < NUMS; i+=2 )
        {
            if( H.contains( i ) )
                System.out.println( "OOPS!!! " +  i  );
        }
        
        long endTime = System.currentTimeMillis( );
        
        System.out.println( "Elapsed time: " + (endTime - startTime) );

	}

}
