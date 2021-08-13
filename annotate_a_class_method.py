from time import sleep
from threading import Thread
# If you are trying to annotate a class method with an annotation that you did not write
# it might not be happy to pass the "self" argument through. In that case we can use a
# closure to annotate your class method and still have access to the "self" object.

# If you are the one writing the annotation, then just make sure it can pass through "self"
# and you don't have to worry about all this. You would just annotate the class method definition.

# Pretend this is a library class/annoation that we do not have the ability to change
# Skip down to MyClass
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

# This is our class that has a method we want to annotate
class MyClass:

    def __init__(self, message):
        self.message = message

        self.timer = Timer()

        # We need to call self.annotate_say_message(), but we only need to assign it to self.say_message
        # if we still want to call it ourselves. In this case, we just want the timer to call it so
        # self.annotate_say_message() would be enough to make an annotate the function
        self.say_message = self.annotate_say_message()
        self.timer.start()

    def annotate_say_message(self):
        @self.timer.register
        def say_message():
            print(self.message)

        # We don't actually need to return this unless we want to do something with it. In this case
        # the we are registering it to the timer with an annotation so we don't need it after this.
        return say_message

my_class = MyClass('hello world')
sleep(999)