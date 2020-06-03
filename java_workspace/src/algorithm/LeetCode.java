package algorithm;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Stack;

public class LeetCode {
	/**
	 * O(N) time, hash table, dynamically add key-value pairs, submitted
	 * 
	 * @param nums
	 * @param target
	 * @return
	 */
	public static int[] twoSum(int[] nums, int target) {
		int[] result = null;
		HashMap<Integer, Integer> map = new HashMap<>();
		for (int i = 0; i < nums.length; ++i) {
			if (map.containsKey(target - nums[i])) {
				result = new int[2];
				result[0] = map.get(target - nums[i]);
				result[1] = i;
				break;
			}
			map.put(nums[i], i);
		}
		return result;
	}

	/**
	 * two pass hash table also works; slower
	 * 
	 * @param nums
	 * @param target
	 * @return
	 */
	public int[] twoSum_2(int[] nums, int target) {
    		Map<Integer, Integer> map = new HashMap<>();
    		for (int i = 0; i < nums.length; i++) {
        		map.put(nums[i], i);  // if a number occurs more than once in the array, the value is the last index
    		}
    		for (int i = 0; i < nums.length; i++) {
        		int complement = target - nums[i];
        		if (map.containsKey(complement) && map.get(complement) != i) {  // here i is the first index of complement, while the hash map stores the last one.
            			return new int[] { i, map.get(complement) };  // if they are not the same index, then return
        		}
    		}
    		return null;
	}

	public static final long inv_divisor = 0x1999999A;
	public static final int max = (int) (Integer.MAX_VALUE * inv_divisor >> 32);

	/**
	 * modulus; bitwise shift is faster than division
	 * 
	 * @param x
	 * @return
	 */
	public static int reverseInteger(int x) {
		int result = 0;
		int tmp_x = Math.abs(x);
		for (; tmp_x != 0; tmp_x = (int) (tmp_x * inv_divisor >>> 32)) {
			// for (; tmp_x != 0;tmp_x /=10) {
			if (result > max)
				return 0;
			result = result * 10 + tmp_x % 10;
		}
		return x < 0 ? -result : result;
	}

	/**
	 * best solution
	 * 
	 * @param x
	 * @return
	 */
	public static boolean isPalindrome(int x) {
		if (x < 0 || (x != 0 && x % 10 == 0))
			return false;
		int rev = 0;
		while (x > rev) {
			rev = rev * 10 + x % 10;
			x /= 10;
		}
		return (x == rev || x == rev / 10);
	}

	/**
	 * trick
	 * 
	 * @param x
	 * @return
	 */
	public static boolean isPalindrome_2(int x) {
		if (x < 0)
			return false;
		long x_1 = x;
		long x_2 = 0;
		while (x != 0) {
			x_2 = x_2 * 10 + x % 10;
			x /= 10;
		}
		return x_2 == x_1;
	}

	public static class ListNode {
		int val;
		ListNode next;

		ListNode(int x) {
			val = x;
		}

		public String toString() {
			if (next == null)
				return "" + val;
			else
				return next.toString() + "_" + val;
		}
	}

	/**
	 * traversal linked lists
	 * 
	 * @param l1
	 * @param l2
	 * @return
	 */
	public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
		ListNode res = new ListNode(0);
		ListNode tmp = res;
		int n = l1.val + l2.val;
		tmp.val = n % 10;
		tmp.next = new ListNode(n / 10);
		while (l1.next != null && l2.next != null) {
			tmp = tmp.next;
			l1 = l1.next;
			l2 = l2.next;
			n = tmp.val + l1.val + l2.val;
			tmp.next = new ListNode(n / 10);
			tmp.val = n % 10;
		}
		while (l1.next != null) {
			l1 = l1.next;
			tmp = tmp.next;
			n = tmp.val + l1.val;
			tmp.next = new ListNode(n / 10);
			tmp.val = n % 10;
		}
		while (l2.next != null) {
			l2 = l2.next;
			tmp = tmp.next;
			n = tmp.val + l2.val;
			tmp.next = new ListNode(n / 10);
			tmp.val = n % 10;
		}
		if (tmp.next.val == 0)
			tmp.next = null;
		return res;
	}

	/**
	 * the other approach: use String.indexOf()
	 * 
	 * @param strs
	 * @return
	 */
	public static String longestCommonPrefix(String[] strs) {
		if (strs == null || strs.length == 0)
			return "";
		StringBuilder sb = new StringBuilder();
		char c;
		for (int i = 0; i < strs[0].length(); ++i) {
			c = strs[0].charAt(i);
			for (int j = 1; j < strs.length; ++j) {
				if (i == strs[j].length() || strs[j].charAt(i) != c)
					return sb.toString();
			}
			sb.append(c);
		}
		return sb.toString();
	}

	/**
	 * stack, check if a stack is empty
	 * 
	 * @param s
	 * @return
	 */
	public static boolean isValid(String s) {
		char c;
		Stack<Character> stack = new Stack<>();
		for (int i = 0, n = s.length(); i < n; i++) {
			c = s.charAt(i);
			switch (c) {
			case '(':
			case '[':
			case '{':
				stack.push(c);
				break;
			case ')':
				if (stack.isEmpty() || stack.pop() != '(')
					return false;
				break;
			case ']':
				if (stack.isEmpty() || stack.pop() != '[')
					return false;
				break;
			case '}':
				if (stack.isEmpty() || stack.pop() != '{')
					return false;
				break;
			}
		}
		return stack.isEmpty();
	}

	/**
	 * Queue, add(last), poll(first), while (q.poll() != tmp); sliding window
	 * 
	 * @param s
	 * @return
	 */
	public static int lengthOfLongestSubstring(String s) {
		if (s == null)
			return 0;
		ArrayDeque<Character> q = new ArrayDeque<>(s.length());
		int max = 0;
		char tmp;
		for (int i = 0; i < s.length(); ++i) {
			tmp = s.charAt(i);
			if (q.contains(tmp)) {
				while (q.poll() != tmp)
					;
				q.add(tmp);
			} else {
				q.add(tmp);
				if (q.size() > max)
					max = q.size();
			}
		}
		return max;
	}
	/**
	 * two pointers problem; O(N) time complexity, O(1) space complexity
	 * 
	 * @param nums
	 * @return length of subarray
	 */
    public static int removeDuplicates(int[] nums) {
        int l = nums.length,j=0;
        for(int i = 1; i<l;++i){
        	if(nums[i]!=nums[j])
	        	nums[++j]=nums[i];
        }
    	return j+1;
    }
	
	public static String zigzagConversion(String s, int numRows){
		if(s==null || s.length()==0 || numRows==0) return "";
		char[] res = new char[s.length()];
		int[] ls = new int[numRows];
		int half_t = numRows-1,t = half_t<<1 , r=s.length()%t;
		ls[ls.length-1] = ls[0] = s.length()/t;
		for(int i=1;i<half_t;++i){
			ls[i]=ls[0]<<1;
		}
		for(int i = 0 ; i < r; ++i){
			ls[i%half_t]+=1;
		}
		for(int i = 0 ; i < half_t; ++i){
			ls[i+1]+=ls[i];
		}
		for(int i = 0; i < s.length();++i){
			
		}
		return String.valueOf(res);
	}
	/**
	 * TODO hard
	 * 
	 * @param nums1
	 * @param nums2
	 * @return
	 */
	public double findMedianSortedArrays(int[] nums1, int[] nums2) {
		// int l = nums1.length + nums2.length;
		// if (l == 0)
		// return 0.0;
		// boolean even = (l & 1) == 0;
		// int i, p1, p2, tmp = 0;
		// for (i = 0, p1 = 0, p2 = 0; i < (l >>> 1); ++i) {
		// if (nums1[p1] < nums2[p2]) {
		// tmp = nums1[p1];
		// ++p1;
		//
		// } else {
		// tmp = nums2[p2];
		// ++p2;
		// }
		// }
		// if (even) {
		// if (nums1[p1] < nums2[p2]) {
		// tmp += nums1[p1];
		// } else {
		// tmp += nums2[p2];
		// }
		// }
		return 0.0;
	}

	public static void main(String[] args) {
		// System.out.println("Two sum:");
		// System.out.println(Arrays.toString(twoSum(new int[] { 1, 3, 6, 8, 9
		// }, 12)));
		// System.out.println(Arrays.toString(twoSum(new int[] { 10, 4, 4, 4, 4
		// }, 8)));
		// System.out.println(Arrays.toString(twoSum(new int[] { 10, 3, 6, 8, 9
		// }, 19)));
		// System.out.println(Arrays.toString(twoSum(new int[] { 10, 10, 10, 10,
		// 7 }, 12)));
		// System.out.println("Reverse integer");
		// System.out.println(reverseInteger(65493813));
		// System.out.println(reverseInteger(100000009));
		// System.out.println(reverseInteger(-123456789));
		// System.out.println("Is palindrome:");
		// System.out.println(isPalindrome_2(123321));
		// System.out.println(isPalindrome_2(12321));
		// System.out.println(isPalindrome_2(123322));
		// System.out.println("Add two numbers:");
		// ListNode l1 = new ListNode(8);
		// ListNode l2 = new ListNode(6);
		// l1.next = new ListNode(6);
		// l2.next = new ListNode(4);
		// l2.next.next = new ListNode(8);
		// System.out.println(l1 + " + " + l2 + " = " + addTwoNumbers(l1, l2));
		// System.out.println("Longest common prefix:");
		// String[] s = {"Android","An","AndroiD","Andrew","And"};
		// System.out.println(longestCommonPrefix(s));
		// System.out.println("Valid parentheses:");
		// System.out.println(isValid("(((([[]]))))){}{]"));
		// System.out.println(isValid("((((([[]]))))){}{}"));
//		System.out.println(lengthOfLongestSubstring("aab"));
		int[] arr={1,2,3,4,5,5};
		System.out.println(removeDuplicates(arr));
		System.out.println(Arrays.toString(arr));
		arr=new int[]{1,1,1,4,5,5};
		System.out.println(removeDuplicates(arr));
		System.out.println(Arrays.toString(arr));
		arr=new int[]{1,1};
		System.out.println(removeDuplicates(arr));
		System.out.println(Arrays.toString(arr));
	}
}
