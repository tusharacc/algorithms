from main import initiate
import unittest,random

class TestSelSortFunction(unittest.TestCase):
 
	def test_1(self):
		sequence = [5,4,3,2,1]
		initiate(sequence)
		self.assertEqual(sequence,[1,2,3,4,5])

	def test_2(self):
		sequence = [1,2,3,4,5]
		initiate(sequence)
		self.assertEqual(sequence,[1,2,3,4,5]) 

	def test_3(self):
		sequence = [5,5,2,2,1]
		initiate(sequence)
		self.assertEqual(sequence,[1,2,2,5,5])  

	def test_random_list(self):

		step = random.randint(1,10)
		number_of_items = random.randint(1,1000)
		list_of_items = list(range(number_of_items,0,step*-1))
		sorted_list = sorted(list_of_items)
		initiate(list_of_items)
		self.assertEqual(list_of_items,sorted_list)

 
if __name__ == '__main__':
	unittest.main()
