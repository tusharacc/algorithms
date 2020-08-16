#include<stdio.h> 
void divide(int array[],int low, int right);
void sort_merge(int arr[],int low, int mid, int right);

int main(int argc, char* argv){
	int array[10] = {4,8,1,3,9,7,5,6,2,10};
        int len = *(&array + 1) - array;
	divide(array,0,len-1);
	for (int i = 0; i < len; i++)
	{
		printf("%d\n",array[i]);
	}
	return 0;
}

void divide(int array[],int low, int right)
{
	if (low < right) 
	{
		int mid = low + (right - low)/2;
		divide(array,low,mid);
		divide(array,mid+1,right);
		sort_merge(array,low,mid,right);
	}
	else 
	{
		return;
	}
}

void sort_merge(int arr[],int low,int mid,int right)
{
	int i,j,k;
	int l_len = mid - low + 1;
	int r_len = right - mid;
	int l_arr[l_len], r_arr[r_len];
	//Populate Left Array
	for ( i = 0; i < l_len; i++)
	{
		l_arr[i] = arr[low + i];
	}

	for ( i = 0; i < r_len; i++)
	{
		r_arr[i] = arr[mid + 1 + i];
	}
	
	i = 0;
	j = 0;
	k = low;
	while (i < l_len && j < r_len)
	{
		if (l_arr[i] < r_arr[j])
		{
			arr[k] = l_arr[i];
			i++;
		}
		else 
		{
			arr[k] = r_arr[j];
			j++;
		}
		k++;
	}

	while (i < l_len)
	{
		arr[k] = l_arr[i];
		i++;
		k++;
	}

	while (j < r_len)
	{
		arr[k] = r_arr[j];
		j++;
		k++;
	}

}
