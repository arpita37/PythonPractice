import time

start_time = time.perf_counter()


def func():
    print("Sleep for 1 sec")
    time.sleep(1)
    print("Done somehitng")

for i in range(10):
    func()

end_time = time.perf_counter()
print(f"Finished the program in {end_time-start_time} seconds")