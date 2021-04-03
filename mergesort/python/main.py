import sys,math


def partition_array(sequence):
	if len(sequence) == 1:
		return

	mid_of_array = math.ceil(len(sequence)/2)
	L = sequence[:mid_of_array]
	R = sequence[mid_of_array:]

	partition_array(L)
	partition_array(R)
	
	i = j = k = 0

	while i < len(L) and j < len(R):
			if L[i] < R[j]:
				sequence[k] = L[i]
				i += 1
			else:
				sequence[k] = R[j]
				j += 1
			k += 1

		# When we run out of elements in either L or M,
		# pick up the remaining elements and put in A[p..r]
	while i < len(L):
		sequence[k] = L[i]
		i += 1
		k += 1

	while j < len(R):
		sequence[k] = R[j]
		j += 1
		k += 1

def initiate(sequence):
	partition_array(sequence)



if __name__ == '__main__':
	list_to_be_sorted = list(map(int,sys.argv[1:]))
	initiate(list_to_be_sorted)