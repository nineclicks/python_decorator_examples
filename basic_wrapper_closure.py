def decoration_fn(fn): # the decorator function takes the decorated function as a param
    print('decoration_fn')

    def wrapper_fn():
        print('wrapper start')
        # Notice there is no fn argument passed in to this function.
        # fn() is referencing the argument from the outer, decoration_fn.
        # This is a "closure" and we need it to access "fn" because when original_fn()
        # is called, it will actually be caling wrapper_fn() so wrapper_fn() will only
        # get whatever parameters were going to be passed in to original_fn()
        fn()
        print('wrapper end')

    return wrapper_fn

print('- Calling @decoration_fn')
@decoration_fn
def original_fn():
    print('original_fn')

print('- Calling original_fn()')
original_fn()

# decoration_fn is ONLY called once when the code reaches @decoration_fn. Therefore we must return a "Callable" (function, lambda)

#### OUTPUT:
#> - Calling @decoration_fn
#> decoration_fn
#> - Calling original_fn()
#> wrapper start
#> original_fn
#> wrapper end
####
