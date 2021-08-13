# This example is not very useful, it is meant to demonstrate the most basic function of an annotation
# An annotation function is a function that accepts a Callable as a parameter and returns a Callable
# When you use an annoation function on a function declaration, that function will be replaced with the
# return value of the annotation

def annotation_fn(fn): # the annotation function takes the annotated function as a param
    print('annotation_fn')
    # We replace the annotated function with the function that is returned here.
    return new_fn # no (), we are not calling it, we are returning it.

def new_fn():
    # This new function does nothing interesting.
    print('new_fn')

@annotation_fn
def original_fn():
    print('original_fn')

original_fn()
original_fn()
original_fn()

#### output:
#> annotation_fn
#> new_fn
#> new_fn
#> new_fn
####

# The annotation_fn function is ONLY run when we call @annotation_fn
# The annotated function (original_fn) is replaced by whatever function that annotation_fn returns