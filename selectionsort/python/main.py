import sys


def __select_minimum_value(sequence, start_pos):
	min_value_index = start_pos

	for j in range(start_pos+1, len(sequence)):
		if sequence[min_value_index] > sequence[j]:
			min_value_index = j

	return min_value_index

def initiate_sel_sort(sequence):
	start_pos = 0
	for i in range(len(sequence)):
		min_value_index = __select_minimum_value(sequence, start_pos)
		sequence[start_pos],sequence[min_value_index] = sequence[min_value_index],sequence[start_pos]
		start_pos += 1

if __name__ == '__main__':
	list_to_be_sorted = list(map(int,sys.argv[1:]))
	initiate_sel_sort(list_to_be_sorted)
