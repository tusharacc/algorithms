#include <iostream>
#include <selectionsort.h>
#include <stdlib.h>
#include <ctime> 
#include <fstream>
#include <sys/time.h>
#include <sys/resource.h>
#include <unistd.h>

using namespace std;

#define MAX_CASES 100;
#define MAX_ITEMS 90000;
#define MAX  100000;

void getMemoryUsage(){
	int who = RUSAGE_SELF;
	struct rusage usage;
	int ret = getrusage(who, &usage);
	cout << "Time Struct - microseconds" << usage.ru_utime.tv_usec << endl;
	cout << "Time Struct - seconds" << usage.ru_utime.tv_usec << endl;
	cout << "Time Struct - system microseconds" << usage.ru_stime.tv_usec << endl;
	cout << "Time Struct - system seconds" << usage.ru_stime.tv_usec << endl;
	cout << "maximum resident set size" << usage.ru_maxrss << endl;
	cout << "integral shared memory size" << usage.ru_ixrss << endl;
	cout << "integral unshared data size" << usage.ru_idrss << endl;
	cout << "integral unshared stack size" <<  usage.ru_isrss << endl;
	cout << "page faults (hard page faults)" <<  usage.ru_majflt << endl;
	cout << "swaps" <<  usage.ru_nswap << endl;
	cout << "block input operations" <<  usage.ru_inblock << endl;
	cout << "block output operations" <<  usage.ru_oublock << endl;
	cout << "voluntary context switches" <<  usage.ru_nvcsw << endl;
	cout << "involuntary context switches" <<  usage.ru_nivcsw << endl;
	cout << getpid() << endl;
	cout << getppid() << endl;
}

void sortArray(int *arr, int length){
	int temp;

	for (int i = 0; i < length; i++){
		//cout << "Processing ith item " << i << endl;
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
	getMemoryUsage();
}

int main (int argc, char *argv[])
{
	int caseCount = 1;
	
	cout << "Memory Usage Start" << endl;
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

	cout << "Memory Usage End" << endl;
	getMemoryUsage();
	return 0;
} 