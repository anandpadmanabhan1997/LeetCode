import threading
import time

# 🧠 CPU-bound task: heavy computation   
# There will be slight difference in time for CPU tasks because OF GIL
def cpu_task():
    start = time.time()
    count = 0
    for _ in range(11**7):  # Increased to make the CPU load noticeable
        count += 1
    print(f"[CPU] Done in {time.time() - start:.2f}s")

# ⚡ I/O-bound task: simulates waiting for external resource
def io_task():
    start = time.time()
    time.sleep(2)  # Simulates I/O wait (e.g., file read, network call)
    print(f"[I/O] Done in {time.time() - start:.2f}s")

# 🔁 Create threads for both types
cpu_threads = [threading.Thread(target=cpu_task) for _ in range(4)]
io_threads = [threading.Thread(target=io_task) for _ in range(4)]

print("Starting CPU-bound threads...")
for t in cpu_threads:
    t.start()
for t in cpu_threads:
    t.join()

print("\nStarting I/O-bound threads...")
for t in io_threads:
    t.start()
for t in io_threads:
    t.join()





from multiprocessing import Process
import time

def cpu_task():
    start = time.time()
    count = 0
    for _ in range(11**7):
        count += 1
    print(f"[Process] Done in {time.time() - start:.2f}s")

processes = [Process(target=cpu_task) for _ in range(4)]

start_all = time.time()
for p in processes:
    p.start()
for p in processes:
    p.join()

print(f"Multi process otal time with processes: {time.time() - start_all:.2f}s")
