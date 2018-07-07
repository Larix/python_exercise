# -*- coding: utf-8 -*-
import os
class Overlap(object):
	def __init__(self):
		FOLDER_NAME = "numbers"
		NUMBERS_FILE_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[0], FOLDER_NAME)
		self.prime_list = self.file_to_list(NUMBERS_FILE_DIR + '\\prime_numbers.txt')
		self.happy_list = self.file_to_list(NUMBERS_FILE_DIR + '\\happy_numbers.txt')

	def file_to_list(self, filename):
		list_to_return = []
		with open(filename) as f:
			line = f.readline()
			while line:
				list_to_return.append(int(line))
				line = f.readline()
		return list_to_return

	def get_overlap_list(self):
		overlap_list = [element for element in self.prime_list if element in self.happy_list]
		return overlap_list

def main():
	overlap = Overlap()
	print(overlap.get_overlap_list())
	

if __name__ == '__main__':
	main()
