from multiprocessing import Process, cpu_count
import time
import os

from threading import Thread


class MuchCPU(Thread):
    def run(self):
        print(os.getpid())
        for i in range(200000000):
            pass


if __name__ == "__main__":
    procs = [MuchCPU() for f in range(cpu_count())]
    t = time.time()
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    print("work took {} seconds".format(time.time() - t))

