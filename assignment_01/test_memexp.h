#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

int main() {
	string_set set;
	int n;

	cout << "\ncheck/add \"many\"" << endl;
	
	int i = 32;
	
	while(i < 127){
	
		set.add(i);
		i++;
	}
	

	cout << "\ncheck/add \"e\"" << endl;
	n = set.contains("e");
	cout << "\tcontains(\"e\") returns " << n << endl;
	cout << "adding \"e\"" << endl;
	set.add("e");
	n = set.contains("e");
	cout << "\tcontains(\"e\") returns " << n << endl;
}
