#include <iostream>
#include <stdlib.h> 
#include <time.h> 
#include <vector>
#define MAX_SIZE 10

using std::cout;
using std::endl;
using std::vector;



int main(int argc, char* argv[])
{
	if (argc <= 1){
		cout << "Incorrect argument number " << endl;
		return EXIT_FAILURE;
	}
	
	vector<int> v;

	int number_of_arguments = atoi(argv[1]);

	for (int i = 0; i < number_of_arguments; i++){
		v.push_back(atoi(argv[i+2]));
	}

	//Print inital Array
	// for (int i = 0; i < number_of_arguments; i++){
	// 	cout << v.at(i) << " ; ";
	// }	

	cout << endl;

	for (int j = 1;j < number_of_arguments; j++){
		int key = v.at(j);
		int i = j - 1;
		while (i >= 0 && v.at(i) > key){
			v.at(i+1) = v.at(i);
			i = i - 1;
		}
		v.at(i + 1) = key;
	}

	for (int j = 0; j < number_of_arguments; j++){
		cout << v.at(j) << ";";
	}

}