# Generally it may make more sense to use a closure (basic_wrapper_closure.py). This example is an attempt to demonstrate
# annotationions without closures as learning both at the same time is confusing.

def annotation_fn(fn): # the annotation function takes the annotated function as a param
    print('annotation_fn')

    # Using a lambda here so we can pass "fn" into wrapper_fn at the time of calling wrapper_fn.
    # If we were to do "return wrapper_fn(fn)" then wrapper_fn would run once when @annotation_fn is called
    return lambda: wrapper_fn(fn)

def wrapper_fn(fn):
    print('wrapper start')
    fn()
    print('wrapper end')

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

# If annotation_fn were to "return wrapper_fn(fn)" without the lambda we would get the expected output, but only once
# when @annotation_fn is called and after that we would get an error when origin_fn() was called because it has been
# replaced by the None return of wrapper_fn(fn)