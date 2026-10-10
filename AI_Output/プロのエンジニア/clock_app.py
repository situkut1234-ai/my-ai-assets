```python
import time
import datetime

class ClockApp:
    def __init__(self):
        self.running = False
        self.start_time = None

    def start(self):
        self.running = True
        self.start_time = time.time()

    def stop(self):
        self.running = False

    def reset(self):
        self.running = False
        self.start_time = None

    def get_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            current_time = datetime.datetime.now() + datetime.timedelta(seconds=elapsed_time)
            return current_time.strftime("%H:%M:%S")
        else:
            return datetime.datetime.now().strftime("%H:%M:%S")

def main():
    clock_app = ClockApp()
    while True:
        print(clock_app.get_time())
        if clock_app.running:
            time.sleep(1)
        else:
            user_input = input("Enter 's' to start, 'p' to pause, 'r' to reset, or 'q' to quit: ")
            if user_input == 's':
                clock_app.start()
            elif user_input == 'p':
                clock_app.stop()
            elif user_input == 'r':
                clock_app.reset()
            elif user_input == 'q':
                break

if __name__ == "__main__":
    main()
```