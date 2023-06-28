# This example is not very useful, it is meant to demonstrate the most basic function of a decoration
# A decorator function is a function that accepts a Callable as a parameter and returns a Callable
# When you use a decorator function on a function declaration, that function will be replaced with the
# return value of the decoration

def decorator_fn(fn): # the decorator function takes the decorated function as a param
    print('decorator_fn')
    # We replace the decorated function with the function that is returned here.
    return new_fn # no (), we are not calling it, we are returning it.

def new_fn():
    # This new function does nothing interesting.
    print('new_fn')

@decorator_fn
def original_fn():
    print('original_fn')

original_fn()
original_fn()
original_fn()

#### output:
#> decorator_fn
#> new_fn
#> new_fn
#> new_fn
####

# The decorator_fn function is ONLY run when we call @decorator_fn
# The decorated function (original_fn) is replaced by whatever function that decorator_fn returns
