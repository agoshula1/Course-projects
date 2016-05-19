/*
 * Alison Goshulak
 * V00806939
 */
 
/* TripleSum.java
   CSC 225 - Spring 2016
   Programming Assignment 1 - Template for TripleSum
   
   This template includes some testing code to help verify the implementation.
   To interactively provide test inputs, run the program with
	java TripleSum
	
   To conveniently test the algorithm with a large input, create a 
   text file containing space-separated integer values and run the program with
	java TripleSum file.txt
   where file.txt is replaced by the name of the text file.

   B. Bird & M. Simpson - 05/01/2014
*/

import java.util.Scanner;
import java.util.Vector;
import java.util.Arrays;
import java.io.File;

//Do not change the name of the TripleSum class
public class TripleSum{
	/* TripleSum225()
		The input array A will contain non-negative integers. The function
		will search the array A for a triple of elements which sum to 225.
		If such a triple is found, return true. Otherwise, return false.
		The function may modify the array A.
		Do not change the function signature (name/parameters).
	*/
	public static boolean TripleSum225(int[] A){
		
		int n = A.length;
		
		//membership array that indicates the number of instances
		//of each integer in [0, 225] in A
		int[] T = new int[226];
		
		//initializes T by scanning A (Time: O(n)) 
		for(int i = 0; i < n; i++){
			int val = A[i];
			
			//integers > 225 are not recorded
			if(val <= 225){
				T[val]++;
			}
		}
		
		int first, second, third, remainder;
		
		//scan T for triples in A that sum to 225 (Time: O(1))
		for(int i = 225; i >= 0; i--){
			if(T[i] > 0){
				first = i;
				
				//scan from same position for second element
				for(int j = i; j >= 0; j--){
				
					//calculate the remainder if we sum first potential element and current element
					remainder = 225-(first+j);
					
					if(T[j] > 0 && remainder >= 0){
					
						//current element is present and remainder is not larger than 225
						if(j == first && T[j] < 2){
						
							//two numbers are duplicates but only one instance of the value exists
							continue;
						}
						
						second = j;
						third = remainder;
						
						if(T[third] > 0){
						
							//third element is present
							if(T[third] < 2 && (third == first || third == second)){
							
								//third element is duplicate of first or second but only one instance of the value exists
								continue;								
							}else if(T[third] < 3 && (third == second && second == first)){
							
								//all elements are duplicates but less than 3 instances of the value exist
								continue;
							}
							
							return true;						
						}
					}		
				}
			}
		}
		
		return false;		
	}

	/* main()
	   Contains code to test the TripleSum225 function. Nothing in this function 
	   will be marked. You are free to change the provided code to test your 
	   implementation, but only the contents of the TripleSum225() function above 
	   will be considered during marking.
	*/
	public static void main(String[] args){
		Scanner s;
		if (args.length > 0){
			try{
				s = new Scanner(new File(args[0]));
			} catch(java.io.FileNotFoundException e){
				System.out.printf("Unable to open %s\n",args[0]);
				return;
			}
			System.out.printf("Reading input values from %s.\n",args[0]);
		}else{
			s = new Scanner(System.in);
			System.out.printf("Enter a list of non-negative integers. Enter a negative value to end the list.\n");
		}
		Vector<Integer> inputVector = new Vector<Integer>();
		
		int v;
		while(s.hasNextInt() && (v = s.nextInt()) >= 0)
			inputVector.add(v);
		
		int[] array = new int[inputVector.size()];
		
		for (int i = 0; i < array.length; i++)
			array[i] = inputVector.get(i);

		System.out.printf("Read %d values.\n",array.length);
		
		
		long startTime = System.currentTimeMillis();
		
		boolean tripleExists = TripleSum225(array);
		
		long endTime = System.currentTimeMillis();
		
		double totalTimeSeconds = (endTime-startTime)/1000.0;
		
		System.out.printf("Array %s a triple of values which sum to 225.\n",tripleExists? "contains":"does not contain");
		System.out.printf("Total Time (seconds): %.4f\n",totalTimeSeconds);
	}
}
