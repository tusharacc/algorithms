#include <iostream>
#include <selectionsort.h>
#include <stdlib.h>
#include <ctime> 
#include <fstream>

using namespace std;

#define MAX_CASES 100;
#define MAX_ITEMS 100000;
#define MAX  100000;

void sortArray(int *arr, int length){
	int temp;

	for (int i = 0; i < length; i++){
		cout << "Processing ith item " << i << endl;
		int index = i;
		for (int j = i + 1; j < length; j++){
			if (arr[i] > arr[j]){
				index = j;
			}
		}
		temp = arr[i];
		arr[i] = arr[index];
		arr[index] = temp;
	}
}

int main (int argc, char *argv[])
{
	int caseCount = 1;
	
	ofstream myfile;
    myfile.open ("../performance.csv");

    myfile << "program_type,number_of_items,start_time,end_time,time_taken,result\n";

	while (caseCount > 0)
	{
		int itemCount = rand() % MAX_ITEMS + 1; 
		int arr[itemCount] ={0};
		for (int i = 0; i < itemCount; i++)
		{	
			arr[i] = rand() % MAX + 1;
		}
		cout << "The itemCount is " << itemCount << endl;
		time_t start = time(0);
		sortArray(arr,itemCount);
		time_t end = time(0);
		myfile << "SELSORT.CPP," << itemCount << "," << start << "," << end << "," << end - start << ",TRUE\n";
		caseCount--;
	}
	myfile.close();
	return 0;
} 