import threading
from queue import Queue
import time

print_lock = threading.Lock()

q = Queue()



def exampleJob(worker):
    time.sleep(.5)
    with print_lock:
        print(threading.current_thread().name, worker)


def threader():
    while True:
        # get a worker from the queue
        worker = q.get()


        exampleJob(worker)

        q.task_done()



for x in range(20):
    t = threading.Thread(target=threader)

    # classifying as a daemon, so they will die when the main dies
    t.daemon = True

    # begins, must come after daemon definition
    t.start()

start = time.time()

for worker in range(100):
    q.put(worker)

q.join()

print("Entire job took:", time.time() - start)

