import time
import matplotlib.pyplot as plt

def linear_search(arr,n,key):
    for i in range(n):
        if arr[i]==key:
            return i
    return -1
        
def linear_search_experiment(r):
    results=[]
    for _ in range(r):
        n = int(input("Enter the number of elements :"))
        arr = list(map(int,input("Enter the elements of an array :").split()))
        key = int(input("Enter the key element to be searched :"))
        repeat = 10000
        result=-1
        start = time.time()
        for _ in range(repeat):
            result = linear_search(arr,n,key)
        end=time.time()

        if result != -1:
            print(f"Key {key} found at position{result}")
        else:
            print(f"Key {key} not found ")

        time_taken = (end - start) * 1000
        print(f"Time taken to search a key element = {time_taken:.10f} milliseconds \n ")
        results.append((n,time_taken))
    return results                                                                                                                                                                                                                               
            
def plot_results(results):
    n_values=[result[0]for result in results]
    times=[result[1]for result in results]
    plt.figure()
    plt.plot(n_values,times,'o-')
    plt.xlabel("Number of Elements(n)")
    plt.ylabel("Time Taken (milliseconds)")
    plt.title("Linear Search Time Complexity")
    plt.grid(True)
    plt.show()
    
r=int(input("Enter the number of runs :"))
results = linear_search_experiment(r)
plot_results(results)