# Chapter 20 Problems

import threading
import time

# Problem 20.3

class CountThread(threading.Thread):

    def __init__(self, mode, count_access):
        threading.Thread.__init__(self)
        self.mode = mode
        self.count_access = count_access
        self.count = 1 if mode == "odd" else 2

    def run(self):
        while self.count < 101:
            self.count_access.waitTurn(self.mode)
            print self.count
            self.count += 2
            self.count_access.doneTurn(self.mode)

class CountLock():

    def __init__(self):
        self.condition = threading.Condition()
        self.turn = "odd"

    def waitTurn(self, mode):
        while(self.turn != mode):
            with self.condition:
                self.condition.wait()

    def doneTurn(self, mode):
        self.turn = "odd" if self.turn == "even" else "even"
        with self.condition:
            self.condition.notify(n = 1)


def test_20_3():
    count_lock = CountLock()
    count_odd = CountThread("odd", count_lock)
    count_even = CountThread("even", count_lock)

    print "Should count to 100 in order."

    count_even.start()
    count_odd.start()

# Problem 20.6
class FileAccess:
    def __init__(self, name):
        self.name = name
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock()
        self.write_cond = threading.Condition()
        self.read_count = 0
        self.mode = None

    def open(self, mode):
        if mode == "read":
            self.read_lock.acquire()
            self.mode = mode
            self.read_count += 1
            self.read_lock.release()
        else:
            # write
            self.read_lock.acquire()
            if self.read_count > 0:
                self.read_lock.release()
                with self.write_cond:
                    self.write_cond.wait()
                self.read_lock.acquire()
            self.write_lock.acquire()
            self.mode = mode

    def close(self):
        if self.mode == "read":
            self.read_lock.acquire()
            self.read_count -= 1
            if self.read_count == 0:
                with self.write_cond:
                    self.write_cond.notify(1)
            self.read_lock.release()
        else:
            self.read_lock.release()
            self.write_lock.release()

class ReaderWriter(threading.Thread):
    def __init__(self, name, mode, sleep_time, rw_file):
        threading.Thread.__init__(self)
        self.name = name
        self.mode = mode
        self.sleep_time = sleep_time
        self.rw_file = rw_file

    def run(self):
        self.rw_file.open(self.mode)
        print "Thread %s is %s from/to %s for %d seconds..." % (self.name, self.mode, self.rw_file.name, self.sleep_time)
        time.sleep(self.sleep_time)
        self.rw_file.close()
        print "Thread %s is done %s from/to %s" % (self.name, self.mode, self.rw_file.name)

def test_20_6():
    rw_file = FileAccess("test_file")
    threads = [ReaderWriter("Write1","write",1, rw_file),
               ReaderWriter("WriteFast","write", 1, rw_file),
               ReaderWriter("Read1","read",2, rw_file)]#, ReaderWriter("Read2","read", 1, rw_file),
               # ReaderWriter("Write2","write",2, rw_file),
               # ReaderWriter("Write3", "write", 1, rw_file)]

    for thread in threads:
        thread.start()

def main():
    # test_20_3()
    test_20_6()

if __name__ == '__main__':
    main()