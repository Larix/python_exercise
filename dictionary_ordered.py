cntArtists = dict()
from collections import OrderedDict

MyDict = {0: {'Score': 80.0, 'studentName': 'dan'},
          1: {'Score': 92.0, 'studentName': 'rob'},
          2: {'Score': 10.0, 'studentName': 'xyz'}}
cntArtists = OrderedDict(sorted(MyDict.items(), key=lambda t: t[1]['Score'], reverse = True))

for Score, studentName in cntArtists.items():
	print(Score, studentName)