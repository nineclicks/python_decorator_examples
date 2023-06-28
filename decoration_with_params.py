# Decoration with parameters
# Use a double closure. The outer closure handles the parameters and
# the inner closure.
# You need to return both inner functions.:w

def repeat_function_call(number_of_calls):
    def do_repeat_function_call(fn):
        def wrapper():
            for i in range(number_of_calls):
                fn()

        return wrapper
    return do_repeat_function_call

@repeat_function_call(5)
def say_hi():
    print('hi')

say_hi()
