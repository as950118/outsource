import time

def func_1():
    print("Start func 1")
    print("Sleep func 1")
    time.sleep(3)
    print("Stop func 1")

def func_2():
    print("Start func 2")
    print("Sleep func 2")
    time.sleep(2)
    print("Stop func 2")

if __name__ == "__main__":
    start_time = time.time()
    func_1()
    func_2()
    end_time = time.time()
    print("Run time :", end_time-start_time)