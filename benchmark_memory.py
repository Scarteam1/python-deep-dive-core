import sys
import time

def run_allocation_benchmark():
    print("=== Running Systems Memory Scalability Benchmark ===")
    scales = [10, 100, 1000, 10000, 100000]
    
    with open("perf_telemetry.csv", "w") as log:
        log.write("element_count,list_heap_bytes\n")
        for scale in scales:
            test_list = list(range(scale))
            heap_size = sys.getsizeof(test_list)
            log.write(f"{scale},{heap_size}\n")
            print(f"Elements: {scale:6} | Heap Size: {heap_size:8} Bytes")
    
    print("\n[SUCCESS] Systems metric data compiled into: perf_telemetry.csv")

if __name__ == "__main__":
    run_allocation_benchmark()