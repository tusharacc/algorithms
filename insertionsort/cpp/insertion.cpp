#include <iostream>
using namespace std;

int main(){
	int array[6] = {5,2,4,6,1,3};
	for (int j = 1;j < 6; j++){
		int key = array[j];
		int i = j - 1;
		while (i >= 0 && array[i] > key){
			array[i+1] = array[i];
			i = i - 1;
		}
		array[i + 1] = key;
	}

	for (int j = 0; j < 6; j++){
		cout << array[j] << endl;
	}

}