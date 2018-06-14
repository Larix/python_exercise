# -*- coding: utf-8 -*-
import os
import pickle


def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

data = {"a": 1, "b": 2, "c": 3}
path = "//pickle_data"
pickle_file_path = os.path.split(os.path.realpath(__file__))[0]  + path
#print(os.path.dirname(__file__)) 在commmand用完整路徑執行 就是印檔案所在的路徑 用相對路徑執行 則只印相對的路徑
#print(os.path.split(os.path.realpath(__file__))[0]):完整的路徑=>[0]:檔案所在位置 [1]:取執行檔案名稱

ensure_dir(pickle_file_path)
file_name = 'filename.pickle'

with open(pickle_file_path + '//' + file_name, 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(pickle_file_path + '//' + file_name, 'rb') as handle:
    obj = pickle.load(handle)
  
print (obj)