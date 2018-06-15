# -*- coding: utf-8 -*-
import os
import pickle

FOLDER_NAME = "pickle_data"
PICKLE_FILE_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[0], FOLDER_NAME)
FILE_NAME = 'filename.pickle'

#print(os.path.dirname(__file__)) 在commmand用完整路徑執行 就是印檔案所在的路徑 用相對路徑執行 則只印相對的路徑
#print(os.path.split(os.path.realpath(__file__))[0]):完整的路徑=>[0]:檔案所在位置 [1]:取執行檔案名稱

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
	data = {"a": 1, "b": 2, "c": 3}
	ensure_dir(PICKLE_FILE_DIR)
	with open(os.path.join(PICKLE_FILE_DIR, FILE_NAME), 'wb') as handle:
	    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
	with open(os.path.join(PICKLE_FILE_DIR, FILE_NAME), 'rb') as handle:
	    obj = pickle.load(handle)
	print (obj)

if __name__ == '__main__':
	main()


  

