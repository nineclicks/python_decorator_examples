def annotation_fn(fn): # the annotation function takes the annotated function as a param
    print('annotation_fn')

    def wrapper_fn():
        print('wrapper start')
        # Notice there is no fn argument passed in to this function.
        # fn() is referencing the argument from the outer, annotation_fn.
        # This is a "closure" and we need it to access "fn" because when original_fn()
        # is called, it will actually be caling wrapper_fn() so wrapper_fn() will only
        # get whatever parameters were going to be passed in to original_fn()
        fn()
        print('wrapper end')

    return wrapper_fn

print('- Calling @annotation_fn')
@annotation_fn
def original_fn():
    print('original_fn')

print('- Calling original_fn()')
original_fn()

# annotation_fn is ONLY called once when the code reaches @annotatin_fn. Therefore we must return a "Callable" (function, lambda)

#### OUTPUT:
#> - Calling @annotation_fn
#> annotation_fn
#> - Calling original_fn()
#> wrapper start
#> original_fn
#> wrapper end
####
