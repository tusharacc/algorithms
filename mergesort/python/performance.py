import random
import csv
from main import initiate
from datetime import datetime

MAX_ELEMENT = 1000000
PROGRAM = "MERGESORT"

num_of_test_cases = 1
with open('python_performance.csv', 'w', newline='') as csvfile:
	header = ['program_type','number_of_items','start_time','end_time','time_taken','test_result']
	csvwriter = csv.DictWriter(csvfile, fieldnames=header)
	csvwriter.writeheader()
	while num_of_test_cases > 0:
		d = {}
		d['program_type'] = PROGRAM
		number_of_items = random.randint(100000,MAX_ELEMENT)
		#number_of_items = 5
		d['number_of_items'] = number_of_items
		sorted_list = list(range(1,number_of_items))
		#print (sorted_list)
		jumbled_list = random.sample(sorted_list, k=len(sorted_list))
		start_time = datetime.now()
		print (start_time)
		d['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')
		initiate(jumbled_list)
		end_time = datetime.now()
		print (end_time)
		d['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
		d['time_taken'] = (end_time - start_time).seconds
		d['test_result'] = jumbled_list == sorted_list
		csvwriter.writerow(d)
		num_of_test_cases -= 1


