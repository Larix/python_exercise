import threading
import time

class Thread_Generator(threading.Thread):
  def __init__(self, num):
    threading.Thread.__init__(self)
    self.num = num

  def run(self):
    print("Thread", self.num)
    time.sleep(1)

def main():
	# Create Sub Threads
	threads = []
	for i in range(10):
	    threads.append(Thread_Generator(i))
	    threads[i].start()

	# Main Thread....
	

	# Wait for all sub thread done.
	for i in range(10):
	    threads[i].join()

	print("All sub threads Done.")
		
if __name__ == '__main__': 
	main()