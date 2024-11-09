#### Threading benifits the IO bound tasks, multiprocessing helps CPU bound tasks
import threading
import time

start_time = time.perf_counter()


def func(seconds=1):
    print(f"Sleep for {seconds} sec")
    time.sleep(seconds)
    print("Done somehitng")

threads = []
for i in range(10):
    t = threading.Thread(target=func, args=[10])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

    
end_time = time.perf_counter()
print(f"Finished the program in {end_time-start_time}:2.2f seconds")