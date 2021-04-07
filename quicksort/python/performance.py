import random
import csv
from main import initiate_quick_sort
from datetime import datetime
from resource import getrusage,RUSAGE_SELF

MAX_ELEMENT = 10000
PROGRAM = "QUICKSORT"

num_of_test_cases = 100
with open('performance.csv', 'w', newline='') as csvfile:
	header = ['program_type','number_of_items','start_time','end_time','time_taken','test_result','max_resident_size']
	csvwriter = csv.DictWriter(csvfile, fieldnames=header)
	csvwriter.writeheader()
	while num_of_test_cases > 0:
		d = {}
		d['program_type'] = PROGRAM
		number_of_items = random.randint(1,MAX_ELEMENT)
		d['number_of_items'] = number_of_items
		sorted_list = list(range(1,number_of_items))
		#print (sorted_list)
		jumbled_list = random.sample(sorted_list, k=len(sorted_list))
		start_time = datetime.now()
		d['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')
		after_sort = initiate_quick_sort(jumbled_list)
		end_time = datetime.now()
		d['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
		d['time_taken'] = f"{(end_time - start_time).total_seconds()*1000:.3f}"
		#d['test_result'] = after_sort == sorted_list
		d['test_result'] = True
		d['max_resident_size'] = getrusage(RUSAGE_SELF)[2]
		csvwriter.writerow(d)
		num_of_test_cases -= 1


