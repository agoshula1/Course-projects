#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

int main() {
	string_set set1;
	int n;
	
	
	
	cout << "adding \"e\"" << endl;
	set1.add("e");
	
	
	cout << "adding \"f\"" << endl;
	set1.add("f");
	

	
	cout << "adding \"df\"" << endl;
	set1.add("df");
	

	string_set set2(set1);
	cout << "DB: copy constructed" << endl;
	n = set2.contains("e");
	cout << "\tcontains(\"e\") returns " << n << endl;
	
	n = set2.contains("f");
	cout << "\tcontains(\"f\") returns " << n << endl;
	
	n = set2.contains("df");
	cout << "\tcontains(\"df\") returns " << n << endl;
	
	cout << "\tcheck if deep copy" << endl;	
	set1.remove("e");
	n = set2.contains("e");
	cout << "\tcontains(\"e\") on copied set returns " << n << endl;

}
