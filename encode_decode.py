import sys
content = "轉換的方式很簡單"
with open("traditional.txt", "r", encoding = "utf-8") as Corpus:
	for i,sentence in enumerate(Corpus):
		sentence = sentence.strip("\n")
		print(i,sentence.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
