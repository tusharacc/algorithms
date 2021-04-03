#include <iostream>
using namespace std;

int main (int argc, char *argv[])
{
	int foo [5] = { 16, 2, 77, 77, 71 };
	int temp;
	for (int i = 0; i < 5; i++){
		int index = i;
		for (int j = i + 1; j < 5; j++){
			if (foo[i] > foo[j]){
				index = j;
			}
		}
		temp = foo[i];
		foo[i] = foo[index];
		foo[index] = temp;
	}

	for (int i = 0; i < 5; i++){
		cout << foo[i] << endl;
	}
	return 0;
} 