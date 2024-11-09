#### Threading benifits the IO bound tasks, multiprocessing helps CPU bound tasks
import threading
import time

start_time = time.perf_counter()


def func():
    print("Sleep for 1 sec")
    time.sleep(1)
    print("Done somehitng")

threads = []
for i in range(10):
    t = threading.Thread(target=func)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

    
end_time = time.perf_counter()
print(f"Finished the program in {end_time-start_time}:2.2f seconds")