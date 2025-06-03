
import time

class StopWatch:
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            print("Stopwatch started.")
        else:
            print("Stopwatch is already running.")

    def stop(self):
        if self.running:
            self.end_time = time.time()
            self.elapsed_time = self.end_time - self.start_time
            self.running = False
            print("Stopwatch stopped.")
        else:
            print("Stopwatch is not running.")

    def reset(self):
        self.start_time = 0
        self.end_time = 0
        self.elapsed_time = 0
        self.running = False
        print("Stopwatch reset.")

    def lap(self):
        if self.running:
            current_time = time.time()
            lap_time = current_time - self.start_time
            print(f"Lap time: {lap_time:.2f} seconds")
        else:
            print("Stopwatch is not running.")

    def elapsed(self):
        if self.running:
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
        else:
            print(f"Elapsed time: {self.elapsed_time:.2f} seconds")

def main():
    stopwatch = StopWatch()
    while True:
        print("\n1. Start")
        print("2. Stop")
        print("3. Reset")
        print("4. Lap")
        print("5. Elapsed")
        print("6. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            stopwatch.stop()
        elif choice == "3":
            stopwatch.reset()
        elif choice == "4":
            stopwatch.lap()
        elif choice == "5":
            stopwatch.elapsed()
        elif choice == "6":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()

