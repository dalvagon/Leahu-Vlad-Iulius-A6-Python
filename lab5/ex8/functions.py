def print_arguments(function):
    return lambda *args, **argvs: ret_print_arguments(function, *args, **argvs)


def ret_print_arguments(function, *args, **argvs):
    print(
        "Arguments are: "
        + str(args)
        + ", "
        + str({key: argvs[key] for key in argvs.keys()})
    )

    return function(*args, **argvs)


def multiply_output(function):
    return lambda *args, **argvs: function(*args, **argvs) * 2


def augment_function(function, decorators):
    for decorator in decorators:
        function = decorator(function)

    return lambda *args, **argvs: function(*args, **argvs)
