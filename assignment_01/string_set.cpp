/*
 * Program Name: String Set
 * Program Description: A class that stores a set of strings in each instance.
 * Includes operations for adding, removing, and checking for membership of a string in a set.
 */

#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#include "string_set.h"

using namespace std;

//initialize the set
string_set::string_set() {
	//make the set empty to begin with
	for(int i = 0; i < HASH_TABLE_SIZE; i++){
            hash_table[i] = NULL;
    	}
	
	//start iterator at first index
	iterator_index = 0;
	
	//no element yet in first index
	iterator_node = NULL; 
}

//create copy of a set
string_set::string_set(string_set &s0){
	node *p;
	
	//fill up new set with same strings
	for(int i = 0; i < HASH_TABLE_SIZE; i++){
		p = s0.hash_table[i];
		
		//go through linked list in each slot of the original table
		while(p != NULL){
			add(p->s);
			p = p->next;
		}
	}
	
}

//add s to the set
void string_set::add(const char *s) {
	//s is already in the set
	if(contains(s) == 1){
		throw duplicate_exception();

	}else{
		node *p = new node;
		
		if(p == NULL){
			//memory allocation for the node has failed
			throw memory_exception();
			
		}else{
			p->s = new char[strlen(s)+1];
			
			if(p->s == NULL){
				//memory allocation for the string has failed
				delete p;
				throw memory_exception();
				
			}else{
				//adds the string to the set
				strcpy(p->s, s);
				
				//place s in appropriate slot
				int index = hash_function(s);
				p->next = hash_table[index];
				hash_table[index] = p;
				
				//reset the iterator after insertion
				reset();
			}
		}
	}
}

//remove s from the set
void string_set::remove(const char *s) {
	//find slot where s should be
	int index = hash_function(s);
	
	//var to indicate if s has been found
	bool found = false;
	
	node *pre = hash_table[index];	
	if(pre != NULL){
		node *cur = pre->next;
		
		if(strcmp(s, pre->s) == 0){	
			//the string we want is at the head of the list (special case)
			delete pre->s;
			delete pre;
			hash_table[index] = cur;
			found = true;

		}else{		
			while((cur != NULL) && !found){
				if(strcmp(s, cur->s) == 0){
					//the string we want is somewhere in the middle or at the end of the list (normal case)
					pre->next = cur->next;
					delete cur->s;
					delete cur;
					found = true;

				}else{				
					//still looking for s
					pre = cur;
					cur = cur->next;
				}
			}
		}
	}if(!found){
		//the string is not in the set
		throw not_found_exception();

	}else{		
		//reset the iterator after removal
		reset();
	}
}

//checks for membership of s in the set
int string_set::contains(const char *s) {
	//find slot where s should be
	int i = hash_function(s);

    //go through liked list of the slot s hashes to
    for(node *p = hash_table[i]; p != NULL; p = p->next){
        if(strcmp(s, p->s) == 0){
        		 //the string already exists in the set
			return 1;
        }
    }
	
    //the string does not exist in the set
    return 0;
}

//reset the iterator to the first element
void string_set::reset() {
	iterator_index = 0;
	iterator_node = hash_table[iterator_index];
}

//return a pointer to the next element
const char *string_set::next() {
	node *p;
	
	//finds the next string of the set if not yet found
	while((iterator_node == NULL) && (iterator_index < HASH_TABLE_SIZE-1)){		
		iterator_index++;
		iterator_node = hash_table[iterator_index];
	}
	
	if(iterator_node == NULL){
		//no more strings to return
		return NULL;
	}
	
	//returns next string and points iterator to next node
	p = iterator_node;
	iterator_node = iterator_node->next;
	return p->s;
}

//delete dynamically allocated memory
string_set::~string_set() {
	node *p1;
	node *p2;
	
	//go through each slot of the table to delete memory
	for(int i = 0; i < HASH_TABLE_SIZE; i++){
		if(hash_table[i] != NULL){
			p1 = hash_table[i];
			
			//uses two pointers to free memory while moving along in the set
			while(p1 != NULL){				
				delete p1->s;
				p2 = p1->next;
				delete p1;
				p1 = p2;
			}
		}
	}		
}

//calculate hash value of s
int string_set::hash_function(const char *s) {
    int h = 0;
	
    //adds up the ASCII values of each character in the string
    for(int i = 0; s[i] != '\0'; i++){            
			h += s[i];
    }
    
    //make sure 0 <= h < HASH_TABLE_SIZE
    return h % HASH_TABLE_SIZE;
}
