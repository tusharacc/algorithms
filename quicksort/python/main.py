

def initiate_quick_sort(sequence):
	elements = len(sequence)
	
	if elements < 2:
		return sequence
	
	current_position = 0

	for i in range(1, elements): #Partitioning loop
		if sequence[i] <= sequence[0]:
			current_position += 1
			sequence[i],sequence[current_position] = sequence[current_position],sequence[i]

	sequence[0],sequence[current_position] = sequence[current_position],sequence[0]
	
	left = initiate_quick_sort(sequence[0:current_position]) 
	right = initiate_quick_sort(sequence[current_position+1:elements]) 

	arr = left + [sequence[current_position]] + right 
	
	return arr


if __name__ == '__main__':
	import sys
	input_list = list(map(int,sys.argv[1:]))
	print (initiate_quick_sort(input_list))
