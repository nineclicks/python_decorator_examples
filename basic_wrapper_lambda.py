# Generally it may make more sense to use a closure (basic_wrapper_closure.py). This example is an attempt to demonstrate
# decorators without closures as learning both at the same time is confusing.

def decorator_fn(fn): # the decorator function takes the decorated function as a param
    print('decorator_fn')

    # Using a lambda here so we can pass "fn" into wrapper_fn at the time of calling wrapper_fn.
    # If we were to do "return wrapper_fn(fn)" then wrapper_fn would run once when @decorator_fn is called
    return lambda: wrapper_fn(fn)

def wrapper_fn(fn):
    print('wrapper start')
    fn()
    print('wrapper end')

print('- Calling @decorator_fn')
@decorator_fn
def original_fn():
    print('original_fn')

print('- Calling original_fn()')
original_fn()

# decorator_fn is ONLY called once when the code reaches @decorator_fn. Therefore we must return a "Callable" (function, lambda)

#### OUTPUT:
#> - Calling @decorator_fn
#> decorator_fn
#> - Calling original_fn()
#> wrapper start
#> original_fn
#> wrapper end
####

# If decorator_fn were to "return wrapper_fn(fn)" without the lambda we would get the expected output, but only once
# when @decorator_fn is called and after that we would get an error when origin_fn() was called because it has been
# replaced by the None return of wrapper_fn(fn)
