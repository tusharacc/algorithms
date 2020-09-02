#include<stdio.h>

void quicksort(int *arr, int min, int len);

int main(int argc, char *argv[])
{
	int array[10] = {9,3,7,1,2,6,5,4,10,8};
	quicksort(array,0,10);
}

void quicksort(int *arr,int min, int len)
{
	if (len == 0)
	{
		return;
	}
	if (len == 2)
	{
		if (arr[min] > arr[len])
		{
			int temp = arr[min];
			arr[min] = arr[len];
			arr[len] = temp;
			return;
		}
	}
	int pivot = arr[min+len - 1];
	int swap_a, swap_b;
	int left_index = min;
	int right_index = len - 2;
	int left_found = 0;
	int right_found = 0;
	int swap_index;
	while (1 == 1)
	{
		if (arr[left_index] > pivot)
		{
			swap_a = arr[left_index];
			left_found = 1;
		} else 
		{
			left_index++;
		}

		if (arr[right_index] < pivot)
		{
			swap_b = arr[right_index];
			right_found = 1;
			swap_index = right_index;
		} else 
		{
			right_index--;
		}

		if (left_found && right_found)
		{
			arr[left_index] = swap_b;
			arr[right_index] = swap_a;
			left_found = 0;
			right_found = 0;
		}

		if (right_index < left_index )
		{
			int temp = arr[left_index];
			arr[left_index] = pivot;
		        arr[len - 1] = temp;	
			printf ("The min is %d and left_index is %d, len is %d\n",min,left_index,len);
			quicksort(arr,min,left_index);
			quicksort(arr,left_index + 1,len-1);
			break;
		}
	}
}
