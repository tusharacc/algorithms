#include <stdio.h>
#include <stdbool.h>
int find_greater(int *arr, int i, int j, int pivot);
int find_lesser(int *arr, int i, int j, int pivot);
void swap(int *arr, int i, int j);
void quicksort(int *arr,int min,int max);

int main(int argc, char *argv[])
{
	int arr[10] = {1,4,3,2,6,7,5,8,10,9};
	quicksort(arr,0,9);
	for (int i = 0; i < 10; i++)
	{
		printf ("%d\n",arr[i]);
	}
}
void swap(int *arr, int i, int j)
{
	int temp = arr[i];
	arr[i] = arr[j];
	arr[j] = temp;
}

void quicksort(int *arr,int min,int max)
{
	int pivot = arr[max];
	int i = min;
	int j = max-1;
	if (max - min <= 1)
	{
		return;
	}

	while (1)
	{
		while (1)
		{
			if (arr[i] > pivot)
			{
				break;
			}
			else if (i == j)
			{
				break;
			}
			else 
			{
				i++;
			}
		}	
		while (1)
		{
			if (arr[j] < pivot)
			{
				break;
			}
			else if (i == j)
			{
				swap(arr,i,max);
				break;
			}
			else
			{
				j--;
			}
		}
		if (i >= j)
		{
			break;
		}
		swap(arr,i,j);
	}
	quicksort(arr,min,i);
	quicksort(arr,i,max);
}
