#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

int main() {
	bool yes = true;
	
	if(yes){
		string_set set;
		
		set.add("ba");
		set.add("ab");
	}
	
	string_set set2;
	
	int ret = set2.contains("ba");
	
	cout << "Checking if 'ba' is in set2 returns " << ret << endl;
	
	ret = set2.contains("ab");
	
	cout << "Checking if 'ab' is in set2 returns " << ret << endl;
}