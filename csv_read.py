import csv
import os

FOLDER_NAME = ''    
DOCUMENT = 'data.csv'
FILE_DIR = os.path.join(os.path.split(os.path.realpath(__file__))[0], FOLDER_NAME)

def main():
    csvfile = open(FILE_DIR + '\\' + DOCUMENT, 'r', encoding = 'utf8')
    for row in csv.reader(csvfile, delimiter=','):
        print (row)

if __name__ == '__main__': 
	main()