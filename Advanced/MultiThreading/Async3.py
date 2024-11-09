import concurrent.futures
import time

start_Time = time.perf_counter()

def func(secs=1):
    print(f"Sleep for {secs} seconds")
    time.sleep(secs)
    return(f"Done executing function in {secs}")


with concurrent.futures.ThreadPoolExecutor() as exec:
    ### Approach 1, for single execution
    '''t = exec.submit(func, 10)
    print(t.result())'''
    ### Approach 2, for multiple execution
    '''secs = [5,4,3,2,1]
    results = [exec.submit(func, sec) for sec in reversed(secs)]
    for f in concurrent.futures.as_completed(results):
        print(f.result())'''
    
    ### Approach 3, for multiple execution but getting all results at same time
    secs = [5,4,3,2,1]
    results = exec.map(func, secs)
    for r in results:
        print(r)

end_Time = time.perf_counter()
print(f"The time taken for the execution of the program is {float(end_Time-start_Time):2.3f}")