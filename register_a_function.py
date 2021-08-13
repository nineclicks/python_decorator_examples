from time import sleep
from threading import Thread

# Using an annotation to register a function for something like an event
# The annotation saves a reference to the annotated function, but it just
# returns the same function, so no change is made

class Timer:

    def __init__(self):
        self.timer_thread = Thread(target=self.timer_tick, daemon=True)
        self.registered_fn = None

    def timer_tick(self):
        while True:
            sleep(2)
            self.registered_fn()

    def start(self):
        print('Starting timer')
        self.timer_thread.start()

    # This is the annotation function. Notice we are just saving a
    # reference to it and returning the same function back
    def register(self, fn):
        print('Registering function to timer')
        self.registered_fn = fn
        return fn


timer = Timer()

@timer.register
def say_hi():
    print('hi')

timer.start()
sleep(999)