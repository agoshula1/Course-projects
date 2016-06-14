/*
 * Program Name: Mirror of an Ordered Forest
 * Program Description: Given the binary tree that corresponds to a certain ordered forest,
 * produces the binary tree that corresponds to the vertically-mirrored image of the original forest.
 * Notes: Some of the code was provided by the professor (F.R.) as an outline to the assignment
 */

public class MirrorTree {

	//<code by F.R.>
   public BT tree, mirror; // A tree and its mirror

   private char[] a;       // 0/1 array for tree
   private int k;          // used by build()

   MirrorTree( String s ) {
      a = s.toCharArray(); //binary string of BT
	  
	  k = -1;
      tree = build();
	  mirror = mirrorTree( clone( tree ) ); //construct the BT of the mirrored forest
   }
	//construct the BT from the binary string input
   BT build() { return( a[++k] == '0' ? null : new BT( build(), build() )); }
	//</code by F.R.>
   
   //Produces the binary string of BT t that results from a preorder traversal
   public String preord ( BT t ) { 
	  if(t != null){
	    //add "1" to the string and then find strings of subtrees
		return "1" + preord(t.L) + preord(t.R);
	  }
	  
	  //t is empty
	  return "0";
   }
   
   //Outputs the binary strings for tree and mirror
   public String toString() {
	  //separate the two strings with a new line
	  return preord(tree) + "\n" + preord(mirror);
   }
    
   //Produces a clone of the BT t
   public BT clone( BT t ) {
	  if(t != null){
		return new BT(clone(t.L), clone(t.R));
	  }
	  
	  return null;
   }
   
   //Creates the binary tree of the mirrored forest corresponding to t
   public BT mirrorTree( BT t ) {
	  if(t != null){
		//the left subtree stays the left subtree
		t.L = mirrorTree(t.L);
		
		if(t.R != null){
		  //find mirror for right subtree
		  BT submirror = mirrorTree(t.R);
		  
		  //root and right subtree switch
		  t.R.R = t;
		  t.R = null;
		  
		  return submirror;
		}
	  }
	  
	  return t;
   }
	
	//<code by F.R.>
   // YOU CAN OMIT MAIN OR NOT. USE IT FOR TESTING.
   public static void main ( String[] args ) {
      MirrorTree mt = new MirrorTree( args[0] );
      System.out.println( mt+"\ntree and mirror" );
      System.out.println( new MirrorTree( mt.preord( mt.mirror ) ) ); // sanity check	  
   }
   //</code by F.R.>
}
