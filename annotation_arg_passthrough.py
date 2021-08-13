def generic_annotation_fn(fn):
    # We capture all positional and named args and pass them into the original function
    def wrapper_fn(*args, **kwargs):
        print('wrapper start')
        fn(*args, **kwargs)
        print('wrapper end')

    return wrapper_fn

def specific_annotation_fn(fn):
    # We know and care what specific params will be passed into this fn
    def wrapper_fn(message):
        fn(message.upper() + '!!!!!!')

    return wrapper_fn

@generic_annotation_fn
def original_fn_1(message):
    print(message)

@specific_annotation_fn
def original_fn_2(message):
    print(message)

original_fn_1('This is my message')
original_fn_2('This is my message')