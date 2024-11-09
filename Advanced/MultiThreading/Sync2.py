import time

start_time = time.perf_counter()


def func():
    print("Sleep for 10 sec")
    time.sleep(10)
    print("Done somehitng")

for i in range(10):
    func()

end_time = time.perf_counter()
print(f"Finished the program in {end_time-start_time} seconds")