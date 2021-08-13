def outer(x):
    def inner(y):
        # Outer returns inner which is a function/callable.
        # Inner has access to x.
        # x inside of inner will be whatever it was once inner was defined.
        # If outer is called multiple time, inner is defined multiple times
        # and each inner will remember x from that time.
        # This is useful when x is something that you won't have access to
        # when calling inner() but is also not static.
        print(x, y)

    # We return the inner function or do something with it otherwise it disappears
    return inner

reference_to_inner = outer('foo')
reference_to_inner_2 = outer('bar')

reference_to_inner('baz')
reference_to_inner_2('baz')

#### OUTPUT
#> foo baz
#> bar baz
####