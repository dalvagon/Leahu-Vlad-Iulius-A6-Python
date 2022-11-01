def multiply_by_two(x):
    return x * 2


def add_numbers(a, b):
    return a + b


def multiply_by_three(x):
    return x * 3


def print_arguments(function):
    return lambda *args, **argvs: exec(
        open("file", "r").read(),
    )


def multiply_output(function):
    return lambda *args, **argvs: function(*args, **argvs) * 2


def augment_function(function, decorators):
    # return lambda *args, **argvs: decorator(duntion(*args, *argvs)) for decorator in decorators
    return 0
