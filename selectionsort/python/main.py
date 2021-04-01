import sys


def select_minimum_value(sequence, start_pos):
	min_value_index = start_pos

	for j in range(start_pos+1, len(sequence)):
		if sequence[min_value_index] > sequence[j]:
			min_value_index = j

	return min_value_index


list_to_be_sorted = sys.argv[1:]

length_of_list = len(list_to_be_sorted)

start_pos = 0
for i in range(length_of_list):
	min_value_index = select_minimum_value(list_to_be_sorted[start_pos:],start_pos)
	#temp = list_to_be_sorted[start_pos]
	list_to_be_sorted[start_pos],list_to_be_sorted[min_value_index] = list_to_be_sorted[min_value_index],list_to_be_sorted[start_pos]
	#list_to_be_sorted[min_value_index] = temp
	start_pos += 1

print (list_to_be_sorted)
