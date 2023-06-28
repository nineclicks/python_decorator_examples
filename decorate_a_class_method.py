from time import sleep
from threading import Thread
# If you are trying to decorate a class method with a decorator that you did not write
# it might not be happy to pass the "self" argument through. In that case we can use a
# closure to decorate your class method and still have access to the "self" object.

# If you are the one writing the decorator, then just make sure it can pass through "self"
# and you don't have to worry about all this. You would just decorate the class method definition.

# Pretend this is a library class/decorator that we do not have the ability to change
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

    # This is the decorator function. Notice we are just saving a
    # reference to it and returning the same function back
    def register(self, fn):
        print('Registering function to timer')
        self.registered_fn = fn
        return fn

# This is our class that has a method we want to decorate
class MyClass:

    def __init__(self, message):
        self.message = message

        self.timer = Timer()

        # We need to call self.decorate_say_message(), but we only need to assign it to self.say_message
        # if we still want to call it ourselves. In this case, we just want the timer to call it so
        # self.decorate_say_message() would be enough
        self.say_message = self.decorate_say_message()
        self.timer.start()

    def decorate_say_message(self):
        @self.timer.register
        def say_message():
            print(self.message)

        # We don't actually need to return this unless we want to do something with it. In this case
        # the we are registering it to the timer with a decorator so we don't need it after this.
        return say_message

my_class = MyClass('hello world')
sleep(999)
