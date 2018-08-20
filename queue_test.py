import time
import threading
import queue

class Worker(threading.Thread):
  def __init__(self, queue, num, lock):
    threading.Thread.__init__(self)
    self.queue = queue
    self.num = num
    self.lock = lock

  def run(self):
    while self.queue.qsize() > 0:
      msg = self.queue.get()

      # Get Lock
      lock.acquire()
      print("Lock acquired by Worker %d" % self.num)

      # Can't let multi-thread do same work at the same time.
      print("Worker %d: %s" % (self.num, msg))
      time.sleep(1)

      # Release lock
      print("Lock released by Worker %d" % self.num)
      self.lock.release()

my_queue = queue.Queue()
for i in range(5):
  my_queue.put("Data %d" % i)

# Create lock
lock = threading.Lock()

worker1 = Worker(my_queue, 1, lock)
worker2 = Worker(my_queue, 2, lock)

worker1.start()
worker2.start()

worker1.join()
worker2.join()

print("Done.")