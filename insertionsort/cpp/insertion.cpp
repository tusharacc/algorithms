#include <iostream>
#include <stdlib.h> 
#include <time.h> 
#define MAX_SIZE 10
using namespace std;



int main(){
	srand (time(NULL));
	int array[MAX_SIZE];

	//Populating random numbers
	for (int i = 0; i < MAX_SIZE; i++){
		array[i] = rand() % 100 + 1;
	}

	//Print inital Array
	for (int i = 0; i < MAX_SIZE; i++){
		cout << array[i] << " ; ";
	}	

	cout << endl;

	for (int j = 1;j < MAX_SIZE; j++){
		int key = array[j];
		int i = j - 1;
		while (i >= 0 && array[i] > key){
			array[i+1] = array[i];
			i = i - 1;
		}
		array[i + 1] = key;
	}

	for (int j = 0; j < MAX_SIZE; j++){
		cout << array[j] << endl;
	}

}